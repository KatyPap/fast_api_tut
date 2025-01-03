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

def insert_into_table_f(table_name, items):
    for item in items:
        cursor.execute(f"""
          INSERT INTO {table_name} VALUES ('{item}');
        """)
    conn.commit()

@app.get("/")
def root():
    return {"Hello": "World"}
  
@app.post("/select_from_table")
def select_from_table(data: dict):
    table_name = data['table_name']
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows

@app.post("/insert_into_table")
def insert_into_table(data: dict):
    table = data['table'] 
    items = data['items']
    insert_into_table_f(table, items)
    return f'inserted {items} into {table}'

# @app.post("/test_post")
# def insert_test(data: dict):
#     a = data['x']
#     b = data['y']
#     return [a,b]