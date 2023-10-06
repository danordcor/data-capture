# Do not import a library to solve it instantly

This solution provides two main classes: `DataCapture` and `Stats`, designed for capturing and analyzing numerical data, respectively. Assuming all values will be less than 1,000.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Exceptions](#exceptions)
- [Running Tests](#running-tests)

## Description

- **DataCapture**: 
  - This class allows for data input and subsequently builds a statistical object based on the captured data.
  
- **Stats**: 
  - Once data has been captured using `DataCapture`, you can construct a `Stats` object to carry out statistical analyses on the data.
  - The `Stats` object supports three primary types of queries: numbers less than a given value, numbers greater than a given value, and numbers between two values.

## Features

 - Do not import a library to solve it instantly
 - The methods add(), less(), greater(), and between() have constant time O(1)
 - The method build_stats() has a linear complexity O(n)


## Exceptions

The less(), greater(), and between() functions will throw a ValueError exception if you attempt to query a value that hasn't been previously added using the add function.

## Running Tests

To run the tests, make sure you have pytest installed:

```bash
pip install pytest
```

Then, navigate to the project directory and run:

```bash
pytest test.py
```

This will execute all the tests and provide an output showing which tests passed and which failed.