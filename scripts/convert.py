import sqlite3
import csv


def create_database():
    conn = sqlite3.connect("irregular_verbs.db")
    c = conn.cursor()
    c.execute(
        """CREATE VIRTUAL TABLE verbs USING fts5(present, past_simple, past_participle)"""
    )
    conn.commit()
    conn.close()


def populate_database(csv_file):
    conn = sqlite3.connect("irregular_verbs.db")
    c = conn.cursor()
    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            present, past_simple, past_participle = row
            c.execute(
                "INSERT INTO verbs (present, past_simple, past_participle) VALUES (?, ?, ?)",
                (present, past_simple, past_participle),
            )
    conn.commit()
    conn.close()


def main():
    create_database()
    populate_database("irregular_verbs.csv")


if __name__ == "__main__":
    main()
