#!/usr/bin/env python3
"""Logs Analysis Project - Paul Tillman"""
import psycopg2

DBNAME = "news"

def connect_to_database():
  try:
    db = psycopg2.connect(database= DBNAME)
    cursor = db.cursor()
    return cursor
  except:
    print("Failed to connect to PostgreSQL database.")

def view_comboT(db_cursor):
    create_view = """
            CREATE OR REPLACE VIEW comboT AS
            SELECT articles.title, articles.slug, authors.name, authors.id, log.time::date as date
            FROM articles, authors, log WHERE log.path = '/article/' || articles.slug and articles.author = authors.id;
            """

def view_pviews(db_cursor):
    create_view = """
            CREATE OR REPLACE VIEW page_views AS 
            SELECT count(*) AS page_views, time::date AS date 
            FROM log WHERE status = '200 OK' GROUP BY date;
            """

def view_errors(db_cursor):
    create_view = """
            CREATE OR REPLACE VIEW errors AS SELECT count(*) AS errors, time::date AS date 
            FROM log WHERE status != '200 OK' GROUP BY date ORDER BY count(*) DESC;
            """

def view_frate(db_cursor):
    create_view = """
        CREATE OR REPLACE VIEW fail_rate AS SELECT round((errors.errors*1.0/(page_views.page_views+errors.errors)*100, 1) AS percent_errors, errors.date 
        FROM errors, page_views WHERE errors.date = page_views.date;
            """

def top_three_articles(db_cursor):
  #Queries for 3 most popular articles and returns the title and views
    query = """
            SELECT title, count(*)
            FROM   comboT
            GROUP BY title
            ORDER BY count(*) DESC LIMIT 3;
            """
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    print('')
    print('--------------------------------------------')
    print('The three most popular articles of all time:')
    print('--------------------------------------------')
    print('')

    for result in results:
        print('"{title}" - {count} views'
              .format(title=result[0], count=result[1]))
    print('')
    return

def most_popular_authors(db_cursor):
    #Queries for and prints out the most popular authors and views
    
    query = """
            SELECT name, count(*)
            FROM   comboT
            GROUP BY name
            ORDER BY count(*) DESC;
    """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('')
    print('-------------------------------------')
    print('The most popular authors of all time:')
    print('-------------------------------------')
    print('')

    for result in results:
        print('{author} - {count} views'
              .format(author=result[0], count=result[1]))
    print('')
    return

def plus_1percent_error_rate(db_cursor):
    #Queries and prints out day(s) & error rate where the error rate is +1%
    query = """
            SELECT * FROM fail_rate WHERE percent_errors > 1;
            """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('')
    print('--------------------------------')
    print('Days with greater than 1% errors')
    print('--------------------------------')
    print('')

    for result in results:
        print('{date:%B %d, %Y} - {fail_rate}% errors'.format(
            date=result[1],
            fail_rate=result[0]))
    print('')

    return

if __name__ == "__main__":
    CURSOR = connect_to_database()
    if CURSOR:
        top_three_articles(CURSOR)
        most_popular_authors(CURSOR)
        plus_1percent_error_rate(CURSOR)
        CURSOR.close()
