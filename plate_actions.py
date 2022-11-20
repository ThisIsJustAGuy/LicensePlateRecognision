#!/usr/bin/python


def car_is_in_correct_sector(plate, sector, cursor):
    plate = plate.upper()
    sector = sector.upper()
    cursor.execute(
        "SELECT rendszam FROM plates WHERE rendszam = %(plate)s AND ervenyesberlet = 1 AND szektor = %(sector)s", {"plate": plate, "sector": sector})
    return (bool)(cursor.fetchone())


def car_has_valid_ticket(plate, cursor):
    plate = plate.upper()
    cursor.execute(
        "SELECT rendszam FROM plates WHERE rendszam = %(plate)s AND ervenyesberlet = 1", {"plate": plate})
    return (bool)(cursor.fetchone())


def plate_in_db(plate, cursor):
    plate = plate.upper()
    cursor.execute("SELECT rendszam FROM plates WHERE rendszam = %(plate)s", {
                   "plate": plate})
    return (bool)(cursor.fetchone())


def get_email_by_plate(plate, cursor):
    plate = plate.upper()
    cursor.execute("SELECT email FROM plates WHERE rendszam = %(plate)s", {
                   "plate": plate})
    return cursor.fetchone()[0]
