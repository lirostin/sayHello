import psycopg2
from urllib.parse import urlparse
import os

def parse_db_url(db_url: str):
    db_url_parsed = urlparse(db_url)
    database = db_url_parsed.path[1:]
    credentals, address = db_url_parsed.netloc.split("@")
    uname, passwd = credentals.split(":")
    host, port = address.split(":")
    return {"dbname": database, "user": uname, "password": passwd, "host": host, "port": port}

def get_counter():
        sql_command = """
SELECT current_date
        """
        with _conn.cursor() as cursor:
            cursor.execute(sql_command, ())
            return cursor.fetchone()

db_url = os.environ["DATABASE_URL"]

_conn = psycopg2.connect(**parse_db_url(db_url))

print(get_counter())
