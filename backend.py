from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel

app = FastAPI()

conn = psycopg2.connect(
    host="135.225.108.173",
    database="app_database",
    user="katypap",
    password="katypap",
    port="5432"
)
cursor = conn.cursor()

def select_from_table(table_name):
  cursor.execute("SELECT * FROM FRUITS")
  rows = cursor.fetchall()
  return rows

@app.get("/")
def root():
  return {"Hello": "World"}
  
@app.get("/fruits")
def get_fruits():
  fruits = select_from_table('FRUITS')
  return fruits