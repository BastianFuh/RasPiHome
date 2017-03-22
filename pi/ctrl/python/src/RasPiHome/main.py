#!/usr/bin/python

import time

import json
import os
import mysql.connector

import i2cCom


dirPath = "/opt/RasPiHome/dev/"

db  = mysql.connector.connect(
            host      = "localhost",
            user      = "root",
            password  = "root",
            db        = "RasPiHome" )

dbcur = db.cursor()

addSensor_wert = "INSERT INTO sensor_wert " \
                 "(address, port, value)" \
                 "VALUES (%s, %s, %s)"

while 1:

    for dirNum in range(0x08, 0x078):
        try:
            subDir = hex(dirNum) + "/"
            dirContent = os.listdir(dirPath + subDir)

            fileContent = None
            js = None

            for fileName in dirContent:
                with open(dirPath + subDir + fileName, 'r') as f:
                    js = json.load(f)
                    if js['type'] < 0x70:
                        addr  = js['conn']['addr']
                        port  = js['conn']['port']
                        value = i2cCom.readSensor(addr, port)

                        data = (str(addr), str(port), str(value))

                        dbcur.execute(addSensor_wert, data)
                        db.commit()

        except OSError:
            pass

        except IOError:
            pass

    time.sleep(300)
