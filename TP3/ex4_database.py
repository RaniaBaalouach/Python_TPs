import mysql.connector

def create_database():
    conn = mysql.connector.connect(host="localhost", user="root", password="")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS universite")
    conn.close()


def create_table():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="universite")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS etudiants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(50),
            age INT,
            moyenne FLOAT
        )
    """)
    conn.close()

def insert_data():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="universite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO etudiants (nom, age, moyenne) VALUES ('Ali', 20, 14.5)")
    conn.commit()
    conn.close()

def fetch_students(min_moyenne):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="universite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM etudiants WHERE moyenne > %s", (min_moyenne,))
    for row in cursor.fetchall():
        print(row)
    conn.close()
