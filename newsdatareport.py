'''
News Data Report
    Program made by Beto Carlos for Udacity's FSND
Python program that returns 3 reports from the newsdata.sql database:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
'''

import psycopg2

# 1. What are the most popular three articles of all time?
def reporting_3_popular():
    '''
    Function that connects to the newsdata sql database and returns
    the most popular 3 articles of all time.
    '''
    #Connects to database news
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()

    # To execute the query you will need to create the view 'popular3' (See README 1.2)
    cursor.execute('select * from popular3;')
    result_3_popular = cursor.fetchall()
    conn.close()

    # Loops over the dict and prints the most popular books
    for articles in result_3_popular:
        print('Article: "{}" with {} views'.format(articles[1], articles[0]))

# 2. Who are the most popular article authors of all time?
def reporting_popular_authors():
    '''
    Function that connects to the newsdata sql database and returns
    the authors in popularity descending order (views).
    '''
    #Connects to database news
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()

    # To execute the query you will need to create the view 'popularauth' (See README 1.3)
    cursor.execute('select * from popularauth;')
    result_popular_authors = cursor.fetchall()
    conn.close()

    # Loops over the dict and prints the most popular books
    for authors in result_popular_authors:
        print('Author: "{}" with {} views'.format(authors[1], authors[0]))

# 3. On which days did more than 1% of requests lead to errors?
def error_day():
    '''
    Function that connects to the newsdata sql database and returns
    the days with more than 1% of requests that lead to errors:.
    '''
    #Connects to database news
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()

    # Modify the query so you can have only the date and not the time:
    # view 'normal_date' (README 1.4)

    # Query that gets the ammount of requests per day:
    cursor.execute("select count(*), day from normal_date group by day;")
    total_requests = cursor.fetchall()

    # Query that gets the ammount of error requests per day:
    cursor.execute("select count(*), day from normal_date "
                   "where status = '404 NOT FOUND' group by day order by day;")
    error_requests = cursor.fetchall()

    conn.close()

    # Loop to check if the 404 errors were more than 1%
    # This will loop in all 31 days of the log
    i = 0
    for days in total_requests:
        #Checking if the 404 status are more than 1% in each day
        if error_requests[i][0] > (days[0] * .01):
            # If the statement is true assign a variable on
            # how much the percentage was actually that day.
            error_per = (error_requests[i][0]*100) / (days[0])
            print("{} - {:0.2f}% of error requests".format(days[1], error_per))
        i += 1

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
