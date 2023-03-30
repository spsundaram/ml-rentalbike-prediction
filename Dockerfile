FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5600
CMD python ./prediction.py
