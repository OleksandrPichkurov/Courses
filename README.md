# Courses

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)


## General info
This is a training project.

1. Course creation, retrive, update, delete.
* api/courses/
* api/courses/(course id)/
2. Search for a course by name and filter by date.
* api/courses/?start_date=2021-04-01&end_date=2021-08-30

	
## Technologies
Project is created with:
* Django==3.0
* djangorestframework==3.12.2
	
## Setup
To run this project, clone it locally using:

```
$ git clone https://github.com/OleksandrPichkurov/Courses.git
$ pip3 install -r requirements.txt
```

Run migration
```
$ python3 manage.py migrate
```

Run test
```
$ python3 manage.py test
```