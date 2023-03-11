#!/usr/bin/env python3
# Serve primes from a web page.

import primes
import primesql
import sqlalchemy
from sqlalchemy import orm

from flask import Flask, render_template, stream_with_context

app = Flask(__name__)


@app.route("/primes")
def route_primes():

    def stream_template(template_name, **context):

        app.update_template_context(context)

        template = app.jinja_env.get_template(template_name)
        result = template.stream(context)
        result.enable_buffering(1000)
        return result

    def generate_primes():

        engine = sqlalchemy.create_engine(
            primesql.PrimeNumber.get_database_uri())

        with orm.Session(engine) as session:

            for prime_number in session.query(
                    primesql.PrimeNumber):
                yield prime_number.value

    # Keep request context, it's apparently needed to build static URLs.
    return app.response_class(stream_with_context(stream_template(
        'primes.html', primes=generate_primes())))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
