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
BASE_API_URL='https://api.currencyapi.com/v3'
CURRENCY_API_KEY=<your_currency_api_key>
```

2. The script `db/converter.sql` for the MariaDB/MySQL database `converter` must be installed.

3. The private Python API must be run. In Windows:
```
> python -m venv venv
> .\venv\Scripts\activate
> pip install -r requirements.txt
> python -m flask --app api run --port 8000 --debug
```
If the API runs in a different port, make sure to update its base URL in `js\info.js`.

4. Cypress must be installed:
```
npm i
```

## Unit tests

The unit tests for the Python code are managed by Pytest. They lie under `test\unit_tests` and can be run with the command `pytest test\unit_tests`:
- TestLength and TestTemperature test the classes Length and Temperature
- TestCurrency and TestGrade mock the classes Currency and Grade, as they connect to volatile dependencies (an external API and a database, respectively). These tests bear no value. They are simple examples of mocking in Pytest

## Integration tests

There are two types of integration tests:
1. Integration tests in code, managed by Pytest. They are under `test\integration_tests`:
- TestCurrency tests the integration with the currency API. As most of the data returned by said API is non-deterministic (currency exchange changes daily), the tests only check data formalities
- TestGrade tests the integration with the grading table in the database
2. Continuous integration job in GitHub Actions that runs the unit tests. Its script is at `.github/workflows/measure-converter.yml`

## End-to-End tests

The end-to-end tests are managed by Cypress. They are in `cypress\e2e\tests.cy.js` and can be run with the command `npm run test`.

## Tools
Database: MariaDB
Programming: Flask / Python / JavaScript / CSS3 / HTML5
Testing: Pytest / GitHub Actions / Cypress

## Author
Arturo Mora-Rioja
