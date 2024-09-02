# Measure Converter - Unit Tests, Integration Tests, and End-to-End Tests

## Purpose
Sample application to demonstrate basic concepts of object-oriented programming, unit testing, integration testing, and end-to-end testing.

It allows conversions between the following measure systems:
- Length: between metric and imperial
- Temperature: between Celsius, Fahrenheit, and Kelvin
- Currency: between all currencies at https://currencyapi.com/
- Academic grades: between the Danish and American systems


## Installation

1. A file `info/info.php` must be created with the following content:

```php
<?php

class apiKey {
    public const CURRENCY_API_KEY = '<API key provided by https://currencyapi.com/>';
}
```

2. The script `db/converter.sql` for the MariaDB/MySQL database `converter` must be installed.

## Unit tests

The unit tests for the PHP code are managed by PHPUnit. They lie under `tests\unitTests` and can be run with the command `composer test`:
- LengthTest and TemperatureTest test the classes Length and Temperature
- CurrencyTest and GradeTest mock the classes Currency and Grade, as they connect to volatile dependencies (an external API and a database, respectively). These tests bear no value. They are simple examples of creating a stub in PHPUnit 

## Integration tests

There are two types of integration tests:
1. Integration tests in code, managed by PHPUnit. They are under `tests\integrationTests`:
- CurrencyTest tests the integration with the currency API. As most of the data returned by said API is non-deterministic (currency exchange changes daily), the tests only check data formalities
- GradeTest tests the integration with the grading table in the database
2. Continuous integration job in GitHub Actions that runs the unit tests. Its script is at `.github/workflows/php.yml`

## End-to-End tests

The end-to-end tests are managed by Cypress. They are in `cypress\e2e\tests.cy.js` and can be run with the command `npm run test`.

## Tools
Database: MariaDB
Programming: Node.js / JavaScript / CSS3 / HTML5
Testing: Jest / GitHub Actions / Cypress

## Author
Arturo Mora-Rioja (amri@kea.dk)