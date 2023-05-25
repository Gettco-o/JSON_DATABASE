from json_db import JsonDb

from datetime import date

db = JsonDb("Music")
print(db.getSession())


# C FOR CREATE

db.create_tables("Venue", "Artist", "Show")

a = db.get_table_id("Venue"); print(f"Venue table id is {a}")
b = db.get_table_id("Artist"); print(f"Artist table id is {b}")
c = db.get_table_id("Show"); print(f"Show table id is {c}")

db.insert_columns("Venue", "id", "name", "city", "state", "address", "phone", "genres")
db.insert_columns("Artist", "id", "name", "city", "state", "address", "phone", "genres")
db.insert_columns("Show", "id", "artist_id", "venue_id", "date")

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
db.insert_values("Artist", name="Kaleh", city="Kano", state="Kano", address="Goshin", phone=366785478, genres=["Afro", "Highlife"])
db.insert_values("Show", artist_id=3, venue_id=3, date=str(date.today()))

db.insert_values("Show", artist_id=1, venue_id=2, date=str(date.today()))

db.insert_values("Show", artist_id=2, venue_id=1, date=str(date.today()))

# R FOR READ

a = db.get_all()
print("\n ", a)

tables = db.get_tables()
print("\n", tables)

table = db.get_table_data("Venue")


print("\n")
print(table)

print("\n")

y = db.filter("Venue", id=2, name="Blud Haven")
print(y); print()
#print(json.dumps(y))  #json format

print()

z = db.filter("Venue", name="Music Parlor")
print(z)


b = db.filter("Artist", state="Oyo")
print("\n ", b)

a = db.filter("Show", artist_id=2 )
print("\n ", a)


# U FOR UPDATE

db.update_table("Venue", "Venues")
db.update_table("Artist", "Artists")
db.update_table("Show", "Shows")

db.add_columns("Artists", "facebook", "website")

db.update_values("Venues", "id", 1, name="Grand Music Parlor")
db.update_values("Artists", "name", "Emma", facebook="emma.facebook.com", website="emma.space.me")
db.update_values("Artists", "name", "Ameh", facebook="ameh.facebook.com", website="ameh.space.me")
db.update_values("Artists", "id", 3, facebook="danny.facebook.com", website="danny.space.me")
db.update_values("Artists", "name", "Aminah", facebook="aminah.facebook.com", website="aminah.space.me")
db.update_values("Artists", "id", 5, facebook="romoke.facebook.com", website="romoke.space.me")
db.update_values("Artists", "city", "Kano", facebook="kaleh.facebook.com", website="kaleh.space.me")
db.update_values("Venues", "id", 1, address="Old Ife Road")


# D FOR DELETE

#db.drop_table("Shows")

#db.drop_column("Shows", "start_time")
