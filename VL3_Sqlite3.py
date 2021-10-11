import pymysql
import pymysql as sql
import csv


import pandas as pd

file = ('C:/Users/Danie/OneDrive/Desktop/Data Science Augaben Jupyter/Exercise_02_MySQL/USA_cars_datasets.csv')
cars = pd.read_csv(file, sep=",")
#select columns
cars = cars[["price", "brand"]]
print(cars.head(5))


#open connection to sql
#IN [4] Open Connection to database

#connection = pymysql.connect(host='localhost', user='root',port=8111 ,password='', db='example_db',
#                             cursorclass=pymysql.cursors.DictCursor)
#print("I got here")

#create a new table
#try:
#    with connection.cursor() as cursor:
#        sqlQuery = '''CREATE TABLE IF NOT EXISTS example_table(Brand VARCHAR(50),
#        Price DECIMAL(10,2))'''
#        cursor.execute(sqlQuery)
#finally:
#    connection.close()

#create Database
#try:
#    with connection.cursor() as cursor:
#        cursor.execute('CREATE DATABASE IF NOT EXISTS example_db')
#finally:
#        connection.close()
#        print("Im Done")

#open connection
