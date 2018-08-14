import csv
import os
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://rzeznik:Chujek123@localhost/csv_test")
db = scoped_session(sessionmaker(bind=engine))

def main():
    test = db.execute("SELECT title FROM test2 WHERE id=1")
    for i in test:
        print(i)
    books = open("books.csv")
    reader = csv.reader(books)
    for isbn, author, title, year in reader:

        #print(isbn)
        #print(author)
        #print(title)
        #print(year)

        db.execute("INSERT INTO test2 (isbn, title, author, year) VALUES (:isbn, :title , :author, :year)",
        {"isbn": isbn, "title": title, "author": author, "year": year})
        #print(f"added the correct data {isbn}, {author}, {title}, {year}.")
    db.commit()

if __name__ == "__main__":
    main()
