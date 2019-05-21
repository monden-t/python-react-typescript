FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/share/nginx/html/public
ADD requirements.txt /usr/share/nginx/html/public
RUN pip install -r requirements.txt

CMD ["gunicorn", "index:app", "-b", "0.0.0.0:5000"]