FROM python:latest
WORKDIR /say_hi
ADD src /say_hi
RUN pip install -r requirements.txt
CMD ["python","app.py"]







