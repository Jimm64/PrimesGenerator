# Prime number functions

import bisect


def generate_primes(max_value=None):
    '''
        Generate primes in increasing order, up to the given max value, or
        indefinitely.
    '''

    if max_value and 2 > max_value:
        return
    yield 2

    # Use the Eratosthenes sieve, but continually increase the limit of the
    # search. Measurements showed this method to be several times faster than
    # trial division methods.

    # Keep multiples of the known primes.  Each element starts with a known
    # prime, and at each step it is multiplied until it is greater than the
    # current possible prime.
    prime_multiples = [2]

    # For each prime multiple, remember what its corresponding original prime
    # was.
    known_primes = [2]

    # 2 is known, so start with the next number (yes, I know, 3 is also a
    # prime).
    possible_prime = 3

    while not max_value or possible_prime <= max_value:

        # For each of the current prime multiples, multiply them until they are
        # all greater than the current possible prime.  The multiples list is
        # sorted, so we just have to keep checking the front.
        while prime_multiples[0] < possible_prime:

            # Take the lowest multiple.
            lowest_multiple = prime_multiples.pop(0)
            lowest_multiple_prime = known_primes.pop(0)

            # Multiply it until it is greater than our possible prime.
            while lowest_multiple < possible_prime:
                lowest_multiple += lowest_multiple_prime

            # Put the new multiple back in the list.
            index = bisect.bisect(prime_multiples, lowest_multiple)
            prime_multiples.insert(index, lowest_multiple)
            known_primes.insert(index, lowest_multiple_prime)

        # Now, any values from our current possible prime up until the next
        # multiple is a confirmed prime number.
        while possible_prime < prime_multiples[0]:
            yield possible_prime
            index = bisect.bisect(prime_multiples, possible_prime)
            prime_multiples.insert(index, possible_prime)
            known_primes.insert(index, possible_prime)

            # Skip even numbers (they are all multiples of 2)
            # (though profiling indicates that this doesn't really make any
            # difference)
            possible_prime += 2

        possible_prime = prime_multiples[0] + 1
