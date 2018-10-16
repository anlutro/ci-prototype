FROM python:3.7-slim-stretch AS build
RUN python3 -m venv /venv && /venv/bin/pip install -U pip setuptools
RUN mkdir -p /app
ADD requirements.txt /app
RUN /venv/bin/pip install -r /app/requirements.txt
ADD . /app
WORKDIR /app
RUN /venv/bin/pip install /app

FROM build AS dev
ADD requirements-dev.txt ./
RUN /venv/bin/pip install -r /app/requirements-dev.txt

FROM build AS prod
COPY --from=build /venv /venv
EXPOSE 5000
CMD /venv/bin/python -m myapp
