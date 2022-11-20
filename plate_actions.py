#!/usr/bin/python
from dbconnect import connecttodb
from send_email import start_email_process


# def can_car_come_in(plate, sector, cursor):
#     plate = plate.upper()
#     sector = sector.upper()
#     cursor.execute(
#         "SELECT * FROM plates WHERE rendszam = %(plate)s AND szektor = %(sector)s AND ervenyesberlet = 1", {"plate": plate, "sector": sector})
#     return (bool)(cursor.fetchone())

def car_is_in_correct_sector(plate, sector, cursor):
    plate = plate.upper()
    sector = sector.upper()


def car_has_valid_ticket(plate, cursor):
    plate = plate.upper()


def plate_in_db(plate, cursor):
    plate = plate.upper()
    cursor.execute("SELECT email FROM plates WHERE rendszam = %(plate)s", {
                   "plate": plate})
    return (bool)(cursor.fetchone())


def get_email_by_plate(plate, cursor):
    plate = plate.upper()
    cursor.execute("SELECT email FROM plates WHERE rendszam = %(plate)s", {
                   "plate": plate})
    return cursor
