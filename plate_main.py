#!/usr/bin/python
from dbconnect import connecttodb
from send_email import bad_sector_email, no_ticket_email
from plate_actions import get_email_by_plate, plate_in_db, car_has_valid_ticket, car_is_in_correct_sector
from detection_actions import add_detection
from bs4 import BeautifulSoup

# TODO dokumentáció, használati útmutató, readme.md

db = connecttodb("localhost", "root", "", "rendszamok")
cursor = db.cursor()
SECTOR = 'D'
PLATE = "ZYX987"

HTMLFile = open("email_template.html", "r", encoding="utf8")
index = HTMLFile.read()
msgHTML = BeautifulSoup(index, features="html.parser")
title1 = msgHTML.find(id="title1")
title2 = msgHTML.find(id="title2")
description = msgHTML.find(id="description1")
subdescription = msgHTML.find(id="subdescription")

if (plate_in_db(PLATE, cursor)):
    print("A rendszám benne van az adatbázisban")
    dest_email = get_email_by_plate(PLATE, cursor)
    if (car_has_valid_ticket(PLATE, cursor)):
        print("Az autónak érvényes bérlete van")
        if (car_is_in_correct_sector(PLATE, SECTOR, cursor)):
            print("Az autónak érvényes bérlete van az adott szektorra")
            print(
                "Az autó bejöhet, LED folyamatosan világít, detectionsbe sikeres belépés kezdeményezés")
            add_detection(SECTOR, 1, cursor, db)
        else:
            print("Az autó rossz szektorban van, 2 LED villanás, email- és detectionsbe sikertelen belépés kezdeményezés")
            bad_sector_email(dest_email, title1, title2,
                             description, subdescription, msgHTML)
            add_detection(SECTOR, 0, cursor, db)
    else:
        print("Az autónak nincs érvényes bérlete, 3 LED villanás, email- és detectionsbe sikertelen belépés kezdeményezés")
        no_ticket_email(dest_email, title1, title2,
                        description, subdescription, msgHTML)
        add_detection(SECTOR, 0, cursor, db)
else:
    print("A rendszám nincs az adatbázisban, 4 LED villanás, detectionsbe sikertelen belépés kezdeményezés")
    add_detection(SECTOR, 0, cursor, db)
