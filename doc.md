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
- you are ready to use the database

## Import requirements
import the database module with the following command

` from json_db import JsonDb `

## Initialize the database
Create an instance of the database

` db = JsonDb("Music") `

This command creates a json file Music.json. This is similar to creating a database in sql databases.
Put the database name as the argument of the class. In this case, the database name is Music.

## Create
The database implements basic CRUD operations.

### To create tables in the database
use the create_tables() function with the table names to be created passed in as arguments

` db.create_tables("Artist", "Venue", "Show") `

This command creates three tables: Artist, Venue, Show. More can be created based on the number of arguments passed in.

When tables are created, an id is stored for each table of the database, it can be retrieved by using the get_table_id() method with the table name as an argument

` db.get_table_id("Venue") `

The command return the id for Venue table (2) which is the second table in the database

`output: 2 `