from urllib.parse import urlparse
import os

from flask import Flask
import psycopg2
import redis


app = Flask(__name__)


def test_postgres():
    p = urlparse(os.environ["DB_URL"])
    kwargs = dict(
        database=p.path.lstrip("/"),
        host=p.hostname,
        password=p.password,
        user=p.username,
    )
    if p.port:
        kwargs["port"] = p.port
    with psycopg2.connect(**kwargs) as conn:
        with conn.cursor() as cur:
            cur.execute("select 1")


def test_redis():
    p = urlparse(os.environ["REDIS_URL"])
    kwargs = dict(host=p.hostname, db=p.path[1:])
    if p.port:
        kwargs["port"] = p.port
    conn = redis.Redis(**kwargs)
    conn.ping()


def hello_world():
    return "Hello World!"


@app.route("/")
def hello():
    test_postgres()
    test_redis()
    return hello_world()


if __name__ == "__main__":
    app.run("0.0.0.0")
