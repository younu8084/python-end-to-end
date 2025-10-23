FROM python:3.8
EXPOSE 30002
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "./src/main.py"]