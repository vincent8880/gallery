# [Gallery]https://vincollage.herokuapp.com/
### Simple photo gallery web application to showcase beautiful pictures and designs 
### June 8th, 2018
#### By **Vincent Ododo**

## Description
[Gallery]https://vincollage.herokuapp.com/ is a simple photo gallery web application to showcase beautiful pictures and designs. Users get to view photos updated by the site admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. The search functionality will search photos based on the categories. 

## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/vincent8880/Zoom.git && cd Zoom`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE zoom;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'zoom'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations album
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
Copy functionality does not work

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on ododovincent54@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Vincent Ododo**
