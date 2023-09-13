# A simple CRUD APP

## Description

A mimimal CRUD App created with Flask and SQLite3 database. This App is capable of adding users to the database strictly by passing the name as JSON, retrieving users from the database by the user ID, update existing users by their ID, and deleting users by their ID.

## Setup and Installation

First, you may need to clone this repository to work with it

### Requirememts

- A virtual environment

You can install one for yourself (on a Linux machine) using the following command:
```
python3 -m venv venv
```
For windows, change `python3` to `python`. It should work.

- Flask

Flask can be installed using the following command

```
pip install flask
```
This will install the latest version of Flask on your machine.

- SQLite3

SQLite comes installed with Python. All you have to do is to import it.

## Usage

To use this API, you need to run the app first. You may use the following commands
```
export FLASK_APP = app.py
flask run
```
Or more conviniently:
```
python app.py
```

**All endpoints have been tested with curl and they worked. You can find all the commands I used with the responses returned by these emdpoints in [DOCUMENTATION.md](/DOCUMENTATION.md).**
