from dbconnect import connecttodb
from stat_actions import get_stats, display_stats

db = connecttodb("localhost", "root", "", "rendszamok")
cursor = db.cursor()
when = input("Mekkora időre levetítve szeretné lekérni a statisztikákat? (y = elmúlt egy év, m = elmúlt egy hónap, w = elmúlt egy hét; egy év az alapértelmezés)\n")
stats = get_stats(cursor, when)
print("Az elmúlt %s statisztikája:" %
      ("hét" if when == 'w' else ("hónap" if when == 'm' else "év")))
display_stats(stats)
