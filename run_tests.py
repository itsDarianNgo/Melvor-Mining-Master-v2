# run_tests.py

import unittest

def main():
    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests")

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    main()
