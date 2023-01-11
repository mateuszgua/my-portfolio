# Portfolio 
> The application for show user portfolio.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)


## General Information
- This project was created because I wanted implement backend Flask with frontend like JavaScript. 
- I wanted also create own portfolio page.

## Technologies Used
- Python - version 3.10.6
- Flask - version 2.2.2


## Features
List the ready features here:
- backend in Flask,
- load data from Json,
- implement javascript in frontend,
- implementation in docker


## Setup
For start application with docker you need [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).


## Usage
The application can be build from sources or can be run in docker.


##### Build from sources
```bash
$ # Move to directory
$ cd folder/to/clone-into/
$
$ # Clone the sources
$ git clone XXX
$
$ # Move into folder
$ cd XXX
$
$ # Create virtual environment
$ python3 -m venv my_env
$
$ # Activate the virtual environment
$ source my_env/bin/activate
$
$ # Start app backend
$ flask --app run.py run
$ # ...
$ # * Running on http://127.0.0.1:5000  
```

##### Start the app in Docker
```bash
$ # Move to directory
$ cd folder/to/clone-into/
$
$ # Clone the sources
$ git clone XXX
$
$ # Move into folder
$ cd XXX
$
$ # Start app
$ docker-compose up --build
$ # ...
$ # backend_1  |  * Running on http://127.0.0.1:5000
```


## Project Status
Project is: _in progress_ 


## Room for Improvement

Room for improvement:
- Improve the view of pages

To do:
- Create dark/light mode