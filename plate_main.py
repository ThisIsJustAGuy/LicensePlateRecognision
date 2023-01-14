#!/usr/bin/python
from dbconnect import connecttodb
from send_email import bad_sector_email, no_ticket_email
from plate_actions import get_email_by_plate, plate_in_db, car_has_valid_ticket, car_is_in_correct_sector
from detection_actions import add_detection
from bs4 import BeautifulSoup
from plate import plate_recognition
# from led import green_light,red_light, red_fast, red_slow

# TODO dokumentáció, használati útmutató, readme.md

db = connecttodb("localhost", "root", "", "rendszamok")
cursor = db.cursor(buffered=True)
SECTOR = 'A'
PLATE = plate_recognition() 

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
                "Az autó bejöhet, zöld világít, detectionsbe sikeres belépés kezdeményezés")
            # green_light()    
            add_detection(SECTOR, 1, cursor, db)
        else:
            print("Az autó rossz szektorban van, piros világít, email- és detectionsbe sikertelen belépés kezdeményezés")
            # red_light()
            bad_sector_email(dest_email, title1, title2,
                             description, subdescription, msgHTML)
            add_detection(SECTOR, 0, cursor, db)
    else:
        print("Az autónak nincs érvényes bérlete, piros lassan villog, email- és detectionsbe sikertelen belépés kezdeményezés")
        # red_slow()
        no_ticket_email(dest_email, title1, title2,
                        description, subdescription, msgHTML)
        add_detection(SECTOR, 0, cursor, db)
else:
    print("A rendszám nincs az adatbázisban, piros gyorsan villog, detectionsbe sikertelen belépés kezdeményezés")
    # red_fast()
    add_detection(SECTOR, 0, cursor, db)
