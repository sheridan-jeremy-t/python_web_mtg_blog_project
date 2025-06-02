This is the start of the main project for Python Web Development created by Ontario Learn and  presented by Sheridan College.

This document will be updated with the outline for the current assignment that is being worked on.

*** ASSIGNMENT 1 ***

Assignment - Create & deploy a Django project

In this course, you will create a fully-functional blog which using Python and the Django framework. Each assignment will add new features to this project to ultimately produce a fully-featured web app. This assignment lays the foundation for the entire course and all subsequent assignments.

Use the mysite project built in this module as reference.
Requirements

Pick a topic for a blog. It could be a personal blog, or related to a special topic or interest.

    Set up your GitHub account if you have not already

    Create a new Django project - different than the one used in the course modules. In your ~/PycharmProjects folder, run:

    $ django-admin startproject <project-name> .

    Use snake_case naming for the Django project.

    Use the standard, out-of-box, sqlite3 database (db.sqlite3) to store data.

    Create an index view (at /) with an accompanying test to demonstrate a 200 HTTP response status code.

    Your app will be run locally on your (and the instructor's) machine. The website must run using python manage.py runserver
    Share github repo (public) for this assignment with the instructor

Evaluation

This assignment is graded using the following criteria, each is worth 3 points.
Points 	Criteria
/ 3 	The project contains a .gitignore file suitable for Python projects
/ 3 	Repository contains a functional Django project with a README file containing a short description of the project
/ 3 	The Django project has an index route at the root path: /
/ 3 	The project has a configured test suite and a test for the index view at the root path: /
/ 3 	The app is configured to connect to the local sqlite3 database in the settings.py file
/ 3 	The project has a valid requirements.txt file containing the libraries used in this project
/ 3 	The Django admin is functional and can be accessed by the instructor

Total: / 21
Grade ( / 3 ) 	Explanation of the Criteria
3 	Criteria is met and all functionality is present
2 	Criteria is mostly met with some gaps in functionality
1 	Criteria is mostly unsatisfied or not functional, though some elements are present
0 	Criteria is not met. No visible attempt to satisfy it exists
Code style

1% will be deducted from the final grade for every code style violation in the project on the last commit.

Code style is verified using pylint. To run pylint locally, install:

$ pip install pylint pylint-django

You should already have Pylint enabled in your code editor, but it can also be run from the command line. Run this command from the root of your project from bash:

$ find . -name '*.py' | xargs pylint

Submission

Submit in the assignment dropbox the full URLs to the GitHub repository link
Running the code

The instructor will run your code using these steps. Make sure your project is compatible.

    Checkout your code from the provided public Github repository.
    Install any new pip modules by running: pip install -r requirements.txt
    Apply any migrations to the local database: python manage.py migrate
    Create a superuser for Django Admin: python manage.py createsuperuser
    Start the website: python manage.py runserver
    Test your website by navigating to: http://127.0.0.1:8000/
    Execute your unit test(s): pytest

requirements.txt

In order to run your code for marking, the instructor's computer must have the required packages to run your code. The packages below will be included as a part of the course standard. Any additional packages you import must also be added to requirements.txt.

# requirements.txt - save this in your project's root folder

Django
gunicorn
psycopg2
whitenoise
freezegun
model_bakery
pytest
pytest-django
pylint
pylint-django
Pillow
boto3
django-ckeditor
django-storages
djangorestframework