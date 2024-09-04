## Test Project with Python, Selenium, and Pytest

This repository includes the files and scripts necessary to conduct automated testing of the [Demo Online Store](http://selenium1py.pythonanywhere.com/) website. The project uses the Page Object pattern, the pytest framework, and the Selenium WebDriver.

### How to run the tests
1. Install the required libraries:
```
pip install -r requirements.txt
```
2. Run the tests:
```
pytest -v --tb=line --language=en test_main_page.py
```
3. Generate allure report and open the report in web browser:
```
pytest --alluredir=allure-results
allure serve allure-results
```
