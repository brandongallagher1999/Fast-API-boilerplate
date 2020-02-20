FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . .

RUN pip install -r requirements.txt

#This line runs the GUNICORN server on Heroku when the Container starts.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]