# Measure Converter - Unit Tests, Integration Tests, and End-to-End Tests

## Purpose
Sample application to demonstrate basic concepts of object-oriented programming, unit testing, integration testing, and end-to-end testing.

It allows conversions between the following measure systems:
- Length: between metric and imperial
- Temperature: between Celsius, Fahrenheit, and Kelvin
- Currency: between all currencies at https://currencyapi.com/
- Academic grades: between the Danish and American systems


## Installation

1. A file `.env` must be created in the root directory with the following content:

```python
ENVIRONMENT='Development'
FLASK_HOST=<your_mysql_server_by_default_localhost>
FLASK_USER=<your_mysql_user_by_default_root>
FLASK_PASSWORD=<your_mysql_password_by_default_empty_string>
FLASK_DATABASE='converter'
```

2. The script `db/converter.sql` for the MariaDB/MySQL database `converter` must be installed.

3. The API must be run. In Windows:
```
> python -m venv venv
> .\venv\Scripts\activate
> pip install -r requirements.txt
> python -m flask --app api run --port 8000 --debug
```

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
Programming: Flask / Python / JavaScript / CSS3 / HTML5
Testing: Pytest / GitHub Actions / Cypress

## Author
Arturo Mora-Rioja