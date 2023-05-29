# JSON_DATABASE
### A simple program in python that acts as a database which stores data in python.
### It implements basic CRUD operations

## GETTING STARTED
- Get the source files from https://github.com/Gettco-o/JSON_DATABASE
- Clone the repository 
- cd into the JSON_DATABASE folder and create your files in the directory

### Alternatively
- Download the source code from https://github.com/Gettco-o/JSON_DATABASE
- copy the json_db folder into your project directory
- you are ready to use the database 😉

## Import requirements
import the database module with the following command

```python
from json_db import JsonDb 
```

## Initialize the database
Create an instance of the database

```python
db = JsonDb("Music") 
```

This command creates a json file Music.json. This is similar to creating a database in sql databases.
Put the database name as the argument of the class. In this case, the database name is Music.

## Create
The database implements basic CRUD operations.

The json file can be checked to see the updates on the database.

### Create tables in the database
use the create_tables() function with the table names to be created passed in as arguments

```python
db.create_tables("Artist", "Venue", "Show") 
```

This command creates three tables: Artist, Venue, Show. More can be created based on the number of arguments passed in.

When tables are created, an id is stored for each table of the database, it can be retrieved by using the get_table_id() method with the table name as an argument

```python 
db.get_table_id("Venue") 
```

The command return the id for Venue table (2) which is the second table in the database

`output: 2 `

### Insert columns in the database tables
To insert columns in the tables, the insert_columns() method is used with the table name as first argument and 
the columns as the other arguments.

Let's insert 7 columns in the Artist table.

```python 
db.insert_columns("Artist", "id", "name", "city", "state", "address", "phone", "genres") 
```

Note that all tables should always have and start with an id column.

This inserts the columns: id, name, city, state, address, phone and genres in the Artist table with initial null values.

For the other tables

```python 
db.insert_columns("Venue", "id", "name", "city", "state", "address", "phone", "genres")
db.insert_columns("Show", "id", "artist_id", "venue_id", "date")
```

### Insert values to the columns
The insert_values() method is used to insert values to the columns. The first argument of the function should be the table name, and the other arguments which are key-values pairs are the column and values respectively. 

The id column should not be passed in because it is automatically passed in and auto increments as new values are inserted.

Let's insert values into our tables

```python
db.insert_values("Venue", name="Music Parlor", city= "Ibadan", state= "Oyo", address="Ife Road", phone=909383844, genres=["pop", "jazz", "classical", "folk"])

db.insert_values("Artist", name="Emma", city="Ibadan", state="Oyo", address="2 old Ife Road", phone=8098184548, genres=["jazz", "pop"])

db.insert_values("Artist", name="Ameh", city="Nsukka", state="Enugu", address="1 Ake street", phone=7113557878, genres=["classical", "pop"])

db.insert_values("Show", artist_id=1, venue_id=1, date=str(date.today()))

db.insert_values("Venue", name="Blud Haven", city= "Ikeja", state= "Lagos", address="Ikeja", phone=717263844, genres=["christian", "jazz", "folk"])

db.insert_values("Artist", name="Danny", city="Ikeja", state="Lagos", address="Ikeja street", phone=947483902, genres=["christian", "folk"])

db.insert_values("Artist", name="Aminah", city="Lafia", state="Nassarawa", address="Gwa road", phone=46737338, genres=["jam"])

db.insert_values("Show", artist_id=2, venue_id=2, date=str(date.today()))

db.insert_values("Venue", name="Home of Music", city= "Ibadan", state= "Oyo", address="3, oritameta", phone=922332104, genres=["apala", "folk", "Raggae"])

db.insert_values("Artist", name="Romoke", city="Ijesha", state="Ogun", address="Ilesha", phone=8098184548, genres=["Rap", "pop", "Hip hop"])

db.insert_values("Artist", name="Kaleh", city="Kano", state="Kano", address="Goshin", phone=366785478, genres=["Afro", "Highlife"])`

db.insert_values("Show", artist_id=3, venue_id=3, date=str(date.today()))

db.insert_values("Show", artist_id=1, venue_id=2, date=str(date.today()))

db.insert_values("Show", artist_id=2, venue_id=1, date=str(date.today()))
```

## Read

### Get the whole data in the database 
To do this, the get_all() method is used
```python
db.get_all()
```

This returns the whole data as a dictionary object.

### Retrieve the database tables
To retrieve the database tables, the get_tables() is used
```python
db.get_tables()
```

This returns a list of all tables in the database

### Retrieve table data
To get the data of a particular table, we use the get_table_data() method with the table name as argument
```python
db.get_table_data("Venue")
db.get_table_data("Artist")
db.get_table_data("Show")
```

A list of dictionary objects is returned for each table

### Get data by filter
To retrieve a table data by a particular column value, the filter() method is used while the arguments will be the table name, and the key value pair of the column-value to filter with.

For example, to get the Venue data where id is 1 and name is Blud Haven,
```python
db.filter("Venue", id=2, name="Blud Haven")
```
This will return a list of dictionary object of the data that has an id of 1 and name Blud Haven. If there is no match, it returns None or null value.

To get the Artist data where state is Oyo
```python
db.filter("Artist", state="Oyo")
```

```python
db.filter("Show", artist_id=2 )
```
Returns list of show data where artist_id is 2