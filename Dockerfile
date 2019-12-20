FROM python:3.6-alpine

WORKDIR /surfops
COPY . /surfops

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip --version
RUN pipenv --version
RUN pipenv install --skip-lock --system --deploy


