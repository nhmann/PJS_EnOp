#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:54:33 2022

@author: nilsheilemann
"""
from flask import Flask, render_template
from kafka import KafkaConsumer
import pandas as pd


msgList1 = []
msgList2 = []
msgList3 = []
msgList4 = []
   
""" Consumer 1 for phOutput """
consumer1 = KafkaConsumer('phOutput',
                         group_id='consumer_web',
                         bootstrap_servers=['localhost:9092'])
for message in consumer1:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    msgList1.append(message.key)
    



""" Consumer 2 for bConsumption """
consumer2 = KafkaConsumer('bConsum',
                         group_id='consumer_web',
                         bootstrap_servers=['localhost:9092'])
for message in consumer2:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    msgList2.append(message.key)




""" Consumer 3 for mConsumption """
consumer3 = KafkaConsumer('mConsum',
                         group_id='consumer_web',
                         bootstrap_servers=['localhost:9092'])
for message in consumer3:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    msgList3.append(message.key)
    
    
    
""" Consumer 4 for bConsumption """
consumer4 = KafkaConsumer('pConsum',
                         group_id='consumer_web',
                         bootstrap_servers=['localhost:9092'])
for message in consumer4:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    msgList4.append(message.key)


# consume earliest available messages, don't commit offsets
#KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)



# Convert DateDtime Series to string list
#dateTimeStr = df['dateTime'].dt.strftime('%Y-%m-%d %H:%M:%S').tolist()

# Create the Webserver
"""
app = Flask(__name__)
@app.route("/")

def home():
    return render_template("graph.html", labels=dateTimeStr, output=df['output'].tolist(), bConsum=df['bConsum'].tolist(), mConsum=df['mConsum'].tolist(), pConsum=df['pConsum'].tolist())
"""