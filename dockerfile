FROM python:3

WORKDIR /fast_api_tut
COPY . .

RUN pip install fastapi 
RUN pip install uvicorn
RUN pip install psycopg2
EXPOSE 8000

# CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
