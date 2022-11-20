#!/usr/bin/python
from datetime import datetime


def add_detection(sector, successful, cursor, db):
    sector = sector.upper()
    cursor.execute("INSERT INTO detections (szektor, idobelyeg, sikerese) VALUES (%(sector)s, %(datetime)s, %(successful)s)", {
                   "sector": sector, "datetime": datetime.today(), "successful": successful})
    db.commit()
    print("Detekció felvéve")
