# LOGS ANALYSIS PROJECT
##### UDACITY FSND PROJECT

Source code for the Logs Analysis project. This project is part of Full Stack Academy Nanodegree Program, made by Mario A. Carlos.

Python3 program that connects to a PostgresSQL database and returns 3 reports from the news database:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Installation
You will need to have python3, pyscopg2 and PostgresSQL installed in order for this program to work correctly.
1. Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. From your terminal run `psql -d news -f newsdata.sql`.
3. You can connect to the database using `psql -d news`.
4. Once you are connected to the database run the views found in the notes section.
1. Clone this repo to your computer.
2. From terminal go to the local file path where you cloned this repo.
3. Run the following command in your terminal once, you are in the correct path: `python3 newsdatareport.py`

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

3. Fetches the time column and gets rid of the time, so it only displays the date, it also sums all the requests and the 404 errors and puts them in each column.
```sql
create view status as
  select substring('%' || time from 2 for 10) as day,
    count(*) as total,
    sum(case when status = '404 NOT FOUND' then 1 else 0 end) as sum404
  from log
  group by day;
```

### License
This project is released under the [MIT License](https://opensource.org/licenses/MIT).

