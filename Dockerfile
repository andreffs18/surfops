FROM python:3.6-alpine

# To install dependencies without virtual environment
# Source: https://pipenv-fork.readthedocs.io/en/latest/install.html#virtualenv-mapping-caveat
ENV PIPENV_VENV_IN_PROJECT=1

WORKDIR /surfops
COPY . /surfops

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip --version
RUN pipenv --version
RUN pipenv install --skip-lock --system --deploy