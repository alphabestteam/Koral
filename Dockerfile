FROM python

RUN pip install flask

COPY ./app1.py /app/app.py

EXPOSE 5000

WORKDIR /app

CMD python app.py