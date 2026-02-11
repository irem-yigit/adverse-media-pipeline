import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="adverse_media",
        user="postgres",
        password="password"
    )
