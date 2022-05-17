FROM python:3.7-slim
RUN python -m pip install --upgrade pip
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install psycopg2-binary
COPY aplication.py /aplication.py
CMD ["python","aplication.py"]
