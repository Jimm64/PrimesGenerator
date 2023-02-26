#!/usr/bin/env python3
# Save primes to a database.

import primes
import primesql
import time
import sqlalchemy
from sqlalchemy import orm


if __name__ == "__main__":

    # Create and open a database.
    engine = sqlalchemy.create_engine(
        primesql.PrimeNumber.get_database_uri())
    primesql.PrimeNumber.metadata.create_all(engine)

    with orm.Session(engine) as session:

        tick_time = time.time()

        # Find and save primes.
        for prime in primes.generate_primes():

            session.add(primesql.PrimeNumber(value=prime))

            # Commit once every second.
            if time.time() > tick_time + 1:
                session.commit()
                tick_time += 1
