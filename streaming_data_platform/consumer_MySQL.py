#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:11:56 2022

@author: nilsheilemann
"""
from kafka import KafkaConsumer
import mysql.connector

# Create empty list
msgList = []


# Connect to MySQL
cnx = mysql.connector.connect(user='p625051d1',
                              password='y5!,t1oAasthnj',
                              host='db4407.mydbserver.com',
                              database='usr_p625051_1')

mycursor = cnx.cursor()

#mycursor.execute("CREATE TABLE phData (datetime DATETIME, output FLOAT, basicConsumption FLOAT, managementConsumption FLOAT, productionConsumption FLOAT)")

consumer = KafkaConsumer('phOutput',
                         group_id='consumer_mysql',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    msgList.append(message.key)

# consume earliest available messages, don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# Select Data and save them to a DataFrame
mycursor.execute("SELECT * FROM phData")
myresult = mycursor.fetchall()
#df = pd.DataFrame(myresult, columns =['dateTime', 'output', 'bConsum', 'mConsum', 'pConsum'])