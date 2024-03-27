# Python API Automation Framework


### Integration TestCases for the Restfull Booker
url - https://restful-booker.herokuapp.com/apidoc/index.html

1.GET, POST, PATCH, PUT, DELETE
2.Response Body, Headers, Status_code
3.Authentication- Basic Auth, Cookie Based Auth
4.JSON schema validation

##Tech Stack(Package used)
1.Request Module 
2.Pytest , PyTest-html
3.Allure Report
4.Faker, CSV, Json, YAML
5.Run via Command line - Jenkins

p.s --> DB connection(in future)

## Install pip packages
  -     pip install requests pytest pytest-html faker allure-pytest jsonschema
  -     pip install requirements.txt

### How to run locally and see the report? 
-     pytest -s -v --alluredir=./reports --html=report.html

### How to run via Jenkins?
1.#   P y A P I A u t o m a t i o n F r a m e w o r k 
 
 