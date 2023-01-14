#!/usr/bin/python
import mariadb

def connecttodb(hostname, username, pwd, dbname):
    db = mariadb.connect(
        host=hostname, user=username, password=pwd, database=dbname)
    return db
