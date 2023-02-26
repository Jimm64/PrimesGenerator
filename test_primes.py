#!/usr/bin/env python3
# Test primes module.

import unittest
from primes import generate_primes


class PrimesTest(unittest.TestCase):

    def test_first_primes_are_correct(self):

        prime_generator = generate_primes(max_value=17)
        self.assertEqual(list(prime_generator), [2, 3, 5, 7, 11, 13, 17])

    def test_max_value_of_2_yields_only_2(self):

        prime_generator = generate_primes(max_value=2)
        self.assertEqual(list(prime_generator), [2])

    def test_max_value_of_1_yields_empty_list(self):

        prime_generator = generate_primes(max_value=1)
        self.assertEqual(list(prime_generator), [])


if __name__ == "__main__":
    unittest.main()
