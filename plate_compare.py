#!/usr/bin/python
from dbconnect import connecttodb
from send_email import start_email_process


def can_car_come_in(plate, sector):
    plate = plate.upper()
    sector = sector.upper()
    cursor.execute(
        "SELECT * FROM adatok WHERE rendszam = %(plate)s AND szektor = %(sector)s AND ervenyesberlet = 1", {"plate": plate, "sector": sector})


def get_email_by_plate(plate):
    plate = plate.upper()
    cursor.execute("SELECT email FROM adatok WHERE rendszam = %(plate)s", {
                   "plate": plate})


SECTOR = 'A'
PLATE = "AAAA123"
db = connecttodb("localhost", "root", "", "rendszamok")
cursor = db.cursor()
can_car_come_in(PLATE, SECTOR)
if (cursor.fetchone()):
    print("Itt világít a LED, bejöhet a kocsi")
else:
    # itt majd külön kell venni, hogy rossz a szektor, vagy a bérlet járt le, illetve benne van-e egyáltalán a rendszám a db-ben
    get_email_by_plate(PLATE)
    dest_email = cursor.fetchone()[0]
    print(dest_email)
    print("Itt villog a LED, email-t kap az illető")
    # emailnél a case-el lehet szórakozni
    start_email_process(dest_email, PLATE)
