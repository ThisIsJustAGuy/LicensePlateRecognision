#!/usr/bin/python
import mysql.connector


def connecttodb(hostname, username, pwd, dbname):
    db = mysql.connector.connect(
        host=hostname, user=username, password=pwd, database=dbname)
    return db
