# LOGS ANALYSIS PROJECT
##### UDACITY FSND PROJECT

Source code for the Logs Analysis project. This project is part of Full Stack Academy Nanodegree Program, made by Mario A. Carlos.

Python3 program that connects to a PostgresSQL database and  returns 3 reports from the news database:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Notes 
In order for the python program to work you will have to run the following views:

1. Fetches the 3 most popular articles.
```sql 
create view popular3 as
  select count(*) as num, articles.title 
    from articles join log 
      on log.path like '%' || articles.slug || '%' 
    where log.status = '200 OK' 
    group by articles.title 
    order by num desc limit 3;
```
    
2. Fetches the most popular authors.
```sql 
create view popularauth as
  select count(*) as num, authors.name
    from
      articles join authors
        on authors.id = articles.author
      join log 
        on log.path like '%' || articles.slug || '%'
    where log.status = '200 OK'
    group by authors.name
    order by num desc;
```

3.1 Fetches the time column and gets rid of the time, so it only displays the date.
```sql
create view normal_date as
  select substring('%' || time from 2 for 10) as day, status
    from log;
```

### Installation
With the PostgresSQL database already installed in your enviroment, and after running the previous views:
1. Clone this repo to your computer
2. From terminal go to the local file path where you cloned this repo.
3. Run the following command in your terminal once, you are in the correct path: `python3 newsdatareport.py`

### License
This project is released under the [MIT License](https://opensource.org/licenses/MIT).

