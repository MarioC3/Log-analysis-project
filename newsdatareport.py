#! /usr/bin/env python3

'''
News Data Report
    Program made by Beto Carlos for Udacity's FSND
Python program that returns 3 reports from the newsdata.sql database:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
'''

import psycopg2


# Connects to the database and executes the function.
def query_exec(query):
    '''
    Function to connect to the database and execute the query
    '''
    try:
        conn = psycopg2.connect("dbname=news")
        cursor = conn.cursor()
    except:
        print("Couldn't connect to Database")
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()

    return result


# 1. What are the most popular three articles of all time?
def reporting_3_popular():
    '''
    Function that connects to the newsdata sql database and returns
    the most popular 3 articles of all time.
    '''
    # To execute the query you will need to create the view 'popular3'
    # (See README - Notes 1)
    # Loops over the dict to show the 3 most popular articles
    for articles in query_exec('select * from popular3;'):
        print('Article: "{}" with {} views'.format(articles[1], articles[0]))


# 2. Who are the most popular article authors of all time?
def reporting_popular_authors():
    '''
    Function that connects to the newsdata sql database and returns
    the authors in popularity descending order (views).
    '''
    # To execute the query you will need to create the view 'popularauth'
    # (See README - Notes 2)
    # Loops over the dict and prints the most popular books
    for authors in query_exec('select * from popularauth;'):
        print('Author: "{}" with {} views'.format(authors[1], authors[0]))


# 3. On which days did more than 1% of requests lead to errors?
def error_day():
    '''
    Function that connects to the newsdata sql database and returns
    the days with more than 1% of requests that lead to errors:.
    '''
    # To execute the query you will need to create the view 'status'
    # (See README - Notes 3)
    # Loop to check if the 404 errors were more than 1%
    for date in query_exec('select * from status;'):
        if (date[1] * .01) < date[2]:
            print("{} - {:0.2f}% of error"
                  "requests".format(date[0], (date[2]*100) / (date[1])))

if __name__ == "__main__":
    print()
    print("1. The most popular 3 articles of all time are:")
    reporting_3_popular()
    print()
    print("2. The most popular authors are:")
    reporting_popular_authors()
    print()
    print("3. Day(s) with more than 1% of requests that lead to errors:")
    error_day()
    print()
