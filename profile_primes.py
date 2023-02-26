#!/usr/bin/env python3
# Measure time needed to save some number of primes.

import timeit

time_to_run = timeit.timeit(
    stmt='list(prime_generator)',
    setup='import primes;'
          ' prime_generator = primes.generate_primes(max_value=100000)')

print('Run time:', time_to_run)
