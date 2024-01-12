import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.db_file = db_file
        self.conn = None

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_file)
            return self.conn
        except Error as e:
            print(e)

    def create_table(self):
        """Create the table for storing scrape jobs and results."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS scrape_jobs (
                    id INTEGER PRIMARY KEY,
                    url TEXT NOT NULL,
                    status TEXT NOT NULL,
                    result TEXT
                )
            """)
            self.conn.commit()
        except Error as e:
            print(e)

    def add_scrape_job(self, url):
        """Add a new scrape job to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO scrape_jobs (url, status) VALUES (?, 'pending')", (url,))
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(e)

    def update_scrape_job(self, job_id, status, result=None):
        """Update the status and result of a scrape job."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE scrape_jobs SET status = ?, result = ? WHERE id = ?", (status, result, job_id))
            self.conn.commit()
        except Error as e:
            print(e)

    def get_scrape_job(self, job_id):
        """Retrieve a scrape job by its ID."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM scrape_jobs WHERE id = ?", (job_id,))
            return cursor.fetchone()
        except Error as e:
            print(e)

    def get_all_scrape_jobs(self):
        """Retrieve all scrape jobs."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM scrape_jobs")
            return cursor.fetchall()
        except Error as e:
            print(e)

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

# Example usage:
# db = Database('scrape_jobs.db')
# db.create_connection()
# db.create_table()
# job_id = db.add_scrape_job('http://example.com')
# db.update_scrape_job(job_id, 'completed', 'Result data here')
# job = db.get_scrape_job(job_id)
# print(job)
# db.close_connection()