# Database-related prime number info.

import sqlalchemy
from sqlalchemy import orm

Base = orm.declarative_base()


class PrimeNumber(Base):

    __tablename__ = "prime_numbers"

    @classmethod
    def get_database_uri(cls):
        ''' Get typical database name for saving/querying. '''
        return 'sqlite:///primes.sqlite3'

    # ID
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    # Prime number value
    value = sqlalchemy.Column(sqlalchemy.Integer)
