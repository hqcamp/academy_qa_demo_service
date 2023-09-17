FROM python:3.11.5-bullseye as base

ENV PKGS_DIR=/install \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

FROM base as builder
RUN apt update
RUN pip install --upgrade pip

RUN mkdir $PKGS_DIR
RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt ./requirements.txt

# Install dependencies to local folder
RUN pip install --target=$PKGS_DIR -r ./requirements.txt
RUN pip install --target=$PKGS_DIR gunicorn

# Main image with service
FROM base

ENV PYTHONPATH=/usr/local
COPY --from=builder /install /usr/local

RUN mkdir -p /app
COPY demo_service /app

WORKDIR /app

ENV SERVICE_HOST="0.0.0.0"
ENV SERVICE_PORT=8080

# Run service
CMD python manage.py migrate && gunicorn --workers=1 --bind $SERVICE_HOST:$SERVICE_PORT demo_service.wsgi
