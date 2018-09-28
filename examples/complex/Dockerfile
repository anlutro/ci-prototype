FROM python:3.7-slim-stretch AS build
RUN python3 -m venv /venv
RUN /venv/bin/pip install -e . -r requirements.txt

FROM build AS dev
RUN /venv/bin/pip install -r requirements-dev.txt

FROM build AS prod
CMD /venv/bin/python -m myapp
