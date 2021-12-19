# Pinterest Back-End
A back-end clone for the Pinterest website made with Django Rest Framework. 
  - The front-end project can be found [here](https://github.com/mamume/pinterest-front/). 
  - The Deployment of the project can be found [here](http://3.132.156.164/)

## Overview
This project is a back-end clone for the Pinterest website made with Django Rest Framework. The project contains four apps:
  - **account**: for user account models, follow relations, authentications, and models serializers.
  - **board**: for the board, notes, and section models, their relations with pins and account models and models serializers.
  - **pin**: for pins, notes, comments models, their relations with account models and models serializers.
  - **user_profile**: for customizing returned data from other apps models.
  
## Installation
- Clone Project
  - `git clone https://github.com/mamume/pinterest-back.git`
- Enter project folder
  - `cd pinterest-back`
- Install `venv`
  - `pip install venv`
- Create a virtual environment
  - `python -m venv <venv_name>`
- Enter virtual environment
  - `source <venv_name>/bin/activate`
- Install requires libraries
  - `pip install -r requirements.txt`
- Add a secret key to `.env` file
  
## Database Processing
  - Download & install PostgreSQL: 
    - [Download Link](https://www.postgresql.org/download/)
  - Create database and set its configurations in `.env` file
  - Create project migrations
    - `python manage.py makemigrations`
  - Apply database migrations
    - `python manage.py migrate`
    
## Start Project
  - To start the project run:
    - `python manage.py runserver`

## Team Members
  - [Ahmed Saied](https://github.com/AhmedSaied94)
  - [Amr Magdy](https://github.com/Amr-Magdy95)
  - [Andrew Roshdy](https://github.com/andrew-roshdy13)
  - [Mahmoud Metwally](https://github.com/mamume)
  - [Momen Awad](https://github.com/momen-awad)
