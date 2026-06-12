# PropertyGuru Automation Framework

## Overview

PropertyGuru Automation Framework is a Python-based test automation solution designed to validate Property Search functionality through both UI and API layers.

The framework follows industry-standard automation design principles including:

* Page Object Model (POM)
* Data-Driven Testing
* Environment-Based Configuration
* Reusable Utility Components
* API + UI Validation
* Screenshot Capture on Failure
* Allure Reporting

The framework validates that search filters applied through the UI return matching data from the backend API.

---

# Technology Stack

| Tool               | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Programming Language      |
| Pytest             | Test Framework            |
| Selenium WebDriver | UI Automation             |
| Requests           | API Testing               |
| Allure             | Reporting                 |
| YAML               | Environment Configuration |
| JSON               | Test Data Management      |
| Docker             | Containerization          |
| Jenkins            | CI/CD                     |

---

# Framework Architecture

```text
property_guru_automation
│
├── api
│   └── property_search_api.py
│
├── config
│   ├── qa.yaml
│   ├── prod.yaml
│   └── config_manager.py
│
├── core
│   ├── driver_manager.py
│   ├── api_client.py
│   └── base_page.py
│
├── pages
│   └── sale_property_page
│
├── tests
│   ├── api_test
│   └── ui_test
│
├── validators
│   └── property_search_validator.py
│
├── utils
│   ├── logger.py
│   ├── json_reader.py
│   └── screenshot_utils.py
│
├── test_data
│   ├── api
│   └── ui
│
├── logs
├── screenshots
│
├── conftest.py
├── constants.py
├── requirements.txt
└── README.md
```

---

# Package Description

## api

Contains API-specific implementations.

### PropertySearchAPI

Responsible for:

* Building API requests
* Invoking property search APIs
* Returning parsed JSON responses

---

## config

Contains environment-specific configuration files.

### qa.yaml

QA environment configuration.

### prod.yaml

Production environment configuration.

### ConfigManager

Loads environment configuration dynamically based on the execution parameter.

Example:

```bash
pytest --env=qa
```

```bash
pytest --env=prod
```

---

## core

Contains framework core components.

### DriverManager

Responsible for:

* Browser initialization
* Browser configuration
* Headless execution support
* Browser cleanup

Supported Browsers:

* Chrome
* Firefox

### APIClient

Reusable HTTP client wrapper used by API classes.

### BasePage

Contains reusable Selenium operations used across page objects.

---

## pages

Contains Page Object Model implementations.

### SalePropertyPage

Responsible for:

* Property search
* Applying quick filters
* Applying advanced filters
* UI interactions

All page-specific locators and actions are maintained here.

---

## tests

Contains all automated test cases.

### ui_test

Contains UI automation scenarios.

### api_test

Contains API validation scenarios.

Tests are data-driven using JSON files.

---

## validators

Contains response validation logic.

### PropertySearchValidator

Validates API response data against applied filters.

Current validations:

* Location
* Property Type
* Bedrooms
* Bathrooms
* Price Range
* Verified Listings

---

## utils

Contains reusable utility classes.

### Logger

Framework-wide logging implementation.

Features:

* Timestamped logs
* Log levels
* File-based logging

### JSONReader

Reads and parses JSON test data.

### ScreenshotUtils

Captures screenshots automatically upon failure.

---

## test_data

Stores all test scenarios.

Benefits:

* Data-driven execution
* Easy maintenance
* Separation of test logic and test data

---

# Execution Flow

```text
Load Configuration
        ↓
Load Test Data
        ↓
Initialize Driver
        ↓
Open Property Search Page
        ↓
Apply UI Filters
        ↓
Execute API Request
        ↓
Validate API Response
        ↓
Generate Reports
```

---

# Configuration Management

Environment configuration is maintained in:

```text
config/
├── qa.yaml
└── prod.yaml
```

Example:

```yaml
base_url: https://www.propertyguru.com.sg
browser: chrome
headless: false
log_level: INFO
```

---

# Running Tests

## Create Virtual Environment

Windows

```bash
python -m venv test-env
```

Activate:

```bash
test-env\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execute Complete Test Suite

```bash
pytest -v
```

---

## Execute UI Tests

```bash
pytest -v tests/ui_test
```

---

## Execute API Tests

```bash
pytest -v tests/api_test
```

---

## Execute Specific Test

```bash
pytest -v tests/ui_test/test_sale_property/test_search_filter_property.py
```

---

## Execute Against QA Environment

```bash
pytest -v --env=qa
```

---

## Execute Against Production Environment

```bash
pytest -v --env=prod
```

---

# Allure Reporting

## Generate Allure Results

```bash
pytest -v --alluredir=allure-results
```

---

## Generate Allure Report

```bash
allure generate allure-results -o allure-report --clean
```

---

## Open Allure Report

```bash
allure open allure-report
```

---

# Screenshot Capture

Whenever a test fails:

1. Screenshot is captured automatically.
2. Screenshot is attached to Allure Report.
3. Screenshot is stored inside:

---

# Logging

Logs are automatically generated during execution.

Location:

```text
logs/
```

Log Information:

* Test execution
* Browser actions
* API requests
* API responses
* Validation failures

---

# Docker Execution

## Build Docker Image

```bash
docker build -t propertyguru-automation .
```

---

## Run Docker Container

```bash
docker run --rm \
-v $(pwd)/allure-results:/app/allure-results \
-v $(pwd)/reports:/app/reports \
propertyguru-automation
```

---

# Jenkins CI/CD 

## Sample Jenkins Pipeline Stages

1. Checkout Source Code
2. Build Docker Image
3. Execute Tests
4. Publish Allure Report
5. Archive Reports
6. Notify Results

---

# Framework Design Principles

The framework follows:

### Page Object Model (POM)

Separates UI actions from test logic.

### Data-Driven Testing

All test scenarios are maintained in JSON files.

### Reusability

Common functionality is centralized into utility and core components.

### Maintainability

Changes to locators or API implementations are isolated to specific layers.

### Scalability

New test cases, filters, APIs, and pages can be added with minimal impact.
