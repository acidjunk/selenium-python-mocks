# selenium-python-mocks

A small test with some mocks for a selenium webdriver in pytest. This repo also contains some "best-practices" regarding
py.test tests and uses pre-commit hooks to run black and isort: whcih should be easily incoporated in LeadExpress's github
repo's.

## Quickstart

create an virtual env and:

```shell
pip install -r requirements/all.txt
python3 src/main.py
```

## Setting up pre-commit hooks

If you want you can install the pre-commit hooks to ease the development process.

```shell
pre-commit install
```

### PyCharm/IntelliJ IDEA

1. Open External tools in PyCharm/IntelliJ IDEA

   On macOS:

   `PyCharm -> Preferences -> Tools -> External Tools`

   On Windows / Linux / BSD:

   `File -> Settings -> Tools -> External Tools`

   On Windows / Linux / BSD:

   `File -> Settings -> Tools -> External Tools`

2. Run _Black_ on every file save

   1. Make sure you have the [File Watcher](https://plugins.jetbrains.com/plugin/7177-file-watchers) plugin installed.
   2. Go to `Preferences or Settings -> Tools -> File Watchers` and click `+` to add a new watcher:
      - Name: Black
      - File type: Python
      - Scope: Project Files
      - Program: `$ProjectFileDir$/fmt_code.sh`
      - Arguments: `$JDKPath$ $FilePath$`
      - Output paths to refresh: `$FilePath$`
      - Working directory: `$ProjectFileDir$`
   3. Uncheck "Auto-save edited files to trigger the watcher"
