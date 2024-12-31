from fastapi import FastAPI

app = FastAPI()

items = ['apple','orange', 'banana'] 

@app.get("/")
def root():
  return {"Hello": "World"}
  
@app.get("/items")
def get_items():
  return items