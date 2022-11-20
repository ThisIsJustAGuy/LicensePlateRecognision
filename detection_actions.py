#!/usr/bin/python
from datetime import datetime


def add_detection(sector, successful, cursor, db):
    sector = sector.upper()
    query = "INSERT INTO detections (szektor, idobelyeg, sikerese) VALUES(%s, %s, %s)"
    record = (sector, datetime.today(), successful)
    cursor.execute(query, record)
    db.commit()
    print("Detekció felvéve")
