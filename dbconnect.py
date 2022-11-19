#!/usr/bin/python
import mysql.connector


def connect(hostname, user, password, database):
    db = mysql.connector.connect(
        host=hostname, user="root", password="", database="rendszamok")
    cursor = db.cursor()
# query = "SELECT * FROM adatok"
# cursor.execute(query)
# for (rendszam, ervenyesberlet, szektor) in cursor:
#     neme = "" if ervenyesberlet else " nem"
#     print(f"{rendszam} bérlete{neme} érvényes a '{szektor}' szektorra.")
