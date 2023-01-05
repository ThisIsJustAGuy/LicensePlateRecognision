#!/usr/bin/python
from dbconnect import connecttodb
from send_email import start_email_process
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
    if (car_has_valid_ticket(PLATE, cursor)):
        print("Az autónak érvényes bérlete van")
        if (car_is_in_correct_sector(PLATE, SECTOR, cursor)):
            print("Az autónak érvényes bérlete van az adott szektorra")
            print(
                "Az autó bejöhet, LED folyamatosan világít, detectionsbe sikeres belépés kezdeményezés")
            add_detection(SECTOR, 1, cursor, db)
        else:
            print("Az autó rossz szektorban van, 2 LED villanás, email- és detectionsbe sikertelen belépés kezdeményezés")
            dest_email = get_email_by_plate(PLATE, cursor)
            title1.string.replace_with("Rossz")
            title2.string.replace_with("szektor")
            description.string.replace_with(
                "Olyan szektorba próbált parkolni, ahova nincs érvényes bérlete. Az alábbi linken megtekintheti hova van érvényes bérlete:\nwww.example.com")
            subdescription.string.replace_with(
                "Az alábbi linken vásárolhat új bérletet:\nwww.example2.com")
            msgPLAIN = "Rossz szektor"
            msgSubject = "Rossz szektor"
            start_email_process(dest_email, msgHTML, msgPLAIN, msgSubject)
            add_detection(SECTOR, 0, cursor, db)
    else:
        print("Az autónak nincs érvényes bérlete, 3 LED villanás, email- és detectionsbe sikertelen belépés kezdeményezés")
        dest_email = get_email_by_plate(PLATE, cursor)
        title1.string.replace_with("Nincs érvényes")
        title2.string.replace_with("bérlet")
        description.string.replace_with(
            "Sajnos ennek az autójának egyáltalán nincs érvényes bérlete.")
        subdescription.string.replace_with(
            "Az alábbi linken vásárolhat új bérletet:\nwww.example2.com")
        msgPLAIN = "Nincs érvényes bérlete"
        msgSubject = "Nincs érvényes bérlete"
        start_email_process(dest_email, msgHTML, msgPLAIN, msgSubject)
        add_detection(SECTOR, 0, cursor, db)
else:
    print("A rendszám nincs az adatbázisban, 4 LED villanás, detectionsbe sikertelen belépés kezdeményezés")
    add_detection(SECTOR, 0, cursor, db)
