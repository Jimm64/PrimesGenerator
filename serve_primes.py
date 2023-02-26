#!/usr/bin/env python3
# Serve primes from a web page.

import primes
import primesql
import sqlalchemy
from sqlalchemy import orm

from flask import Flask, render_template

app = Flask(__name__)


def get_style():
    return '''
    body {
        font-family: monospace;
    }

    '''


@app.route("/primes")
def route_primes():

    def generate_row():
        yield (
            '<html><head><style>' + get_style() +
            '</style></head><body><ol>')

        engine = sqlalchemy.create_engine(
            primesql.PrimeNumber.get_database_uri())

        with orm.Session(engine) as session:

            for prime in session.query(primesql.PrimeNumber):
                yield '<li>{}</li>'.format(prime.value)

        yield '</ol></body></html>'

    return app.response_class(generate_row())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
