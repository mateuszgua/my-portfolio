FROM python:3.10-alpine3.16

WORKDIR /app

RUN pip install --upgrade pip

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN apk add --no-cache gcc musl-dev linux-headers

COPY ./requirements.txt /app/requirements.txt

COPY . /app

ENV VIRTUAL_ENV=/home/mateusz/Learn/my-portfolio/my_env
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PIP_ROOT_USER_ACTION=ignore
RUN export FLASK_APP=app.py
RUN pip install -r requirements.txt

EXPOSE 5001
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]
