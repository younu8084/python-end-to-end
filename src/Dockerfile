FROM python:3.8
EXPOSE 30002
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py . 
CMD ["python", "./main.py"]