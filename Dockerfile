FROM python:alpine 

RUN pip install nltk

WORKDIR /app 

COPY counter.py /app/

COPY cleaned_text.txt /app

CMD python counter.py


