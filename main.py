from dbconnect import connecttodb
from send_email import start_email_process
from plate_actions import get_email_by_plate, plate_in_db, car_has_valid_ticket, car_is_in_correct_sector

SECTOR = 'A'
PLATE = "AAAA123"
db = connecttodb("localhost", "root", "", "rendszamok")
cursor = db.cursor()
if (plate_in_db(PLATE, cursor)):
    print("A rendszám benne van az adatbázisban")
    # car_can_come_in = can_car_come_in(PLATE, SECTOR, cursor)
    # if (car_can_come_in):
    #     print("Bejöhet a kocsi, a LED világít")
    # else:
    if (car_has_valid_ticket(PLATE, cursor)):
        print("Az autónak érvényes bérlete van")
        if (car_is_in_correct_sector(PLATE, SECTOR, cursor)):
            print(
                "Az autó bejöhet, LED folyamatosan világít, detectionsbe sikeres belépés")
        else:
            print(
                "Az autó rossz szektorban van, 2 LED villanás, email, detectionsbe sikertelen belépés")
    else:
        print("Az autónak nincs érvényes bérlete, 3 LED villanás, email, detectionsbe sikertelen belépés")
        cursor = get_email_by_plate(PLATE, cursor)
        dest_email = cursor.fetchone()[0]
        print(dest_email)
        start_email_process(dest_email, PLATE)
else:
    print("A rendszám nincs az adatbázisban, 4 LED villanás, detectionsbe sikertelen belépés")
