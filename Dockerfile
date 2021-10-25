FROM python:3.8
COPY Flask ./Flask
WORKDIR Flask
RUN pip install -r requirements.txt
CMD ["python","app.py"]