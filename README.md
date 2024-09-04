## Test Project with Python, Selenium, and Pytest

This repository contains the scripts and files necessary for automated testing of the [Demo Online Store](http://selenium1py.pythonanywhere.com/) website. The project follows the Page Object Model pattern and utilizes the Pytest framework along with Selenium WebDriver.

### How to Run the Tests

#### 1. Prepare the Environment

Ensure Python 3 is installed on your machine:
```bash
python3 -V
```
Install pip, if it's not already installed:
```
python3 -m pip install pip
```
(Optional, recommended) Create and activate a virtual environment:
```
pip install -r requirements.txt
```
Install the required libraries:
```
pip install -r requirements.txt
```
#### 2. Run the tests
To run all tests in the directory:
```
pytest -v --tb=line
```
To run tests in a specific file:
```
pytest -v --tb=line test_main_page.py
```
To run tests with a specific mark (e.g., basket):
```
pytest -v --tb=line -m basket
```

The `--tb=line` option shortens the traceback output, making the logs more concise.
The `--reruns N` option can be used to automatically rerun failed tests, where N is the number of retries.

#### 3. Generate allure report and open the report in web browser
If you want to generate a detailed test report in HTML format, which can also be integrated into CI/CD pipelines for reporting purposes, follow these steps:
Generate the report:
```
pytest --alluredir=allure-results
```
Serve and view the report in a web browser:
```
allure serve allure-results
```
