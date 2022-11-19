#!/usr/bin/python
from dbconnect import connecttodb


def can_car_come_in(plate, sector):
    plate = plate.upper()
    sector = sector.upper()
    cursor.execute(
        "SELECT * FROM adatok WHERE rendszam = %(plate)s AND szektor = %(sector)s", {"plate": plate, "sector": sector})


def get_email_by_plate(plate):
    plate = plate.upper()
    cursor.execute("SELECT email FROM adatok WHERE rendszam = %(plate)s", {
                   "plate": plate})


SECTOR = 'A'
PLATE = "AAA111"
db = connecttodb("localhost", "root", "", "rendszamok")
cursor = db.cursor()
can_car_come_in(PLATE, SECTOR)
if (cursor.fetchone()):
    print("Itt világít a LED, bejöhet a kocsi")
else:
    print("Itt villog a LED, email-t kap az illető")
