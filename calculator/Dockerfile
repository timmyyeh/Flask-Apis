FROM python:3.7.2
RUN pip install pipenv
COPY Pipfile* /app/
WORKDIR /app
RUN pipenv install --system

COPY . /app

CMD [ "python", "app.py" ]