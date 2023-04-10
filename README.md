# My Solution

This is my solution to the problem at hand. Here's a brief overview of what my solution does:

- It uses Python 3.10.3 and the Django web framework.
- It includes a database schema and data migrations to set up the database.
- It provides a REST API for get resources information.
- It includes unit tests for the API endpoints,database models and management commands.

## Installation

To install and run the solution, follow these steps:

1. Clone the repository to your local machine (git clone "url").
2. Install the required dependencies using pip: `pip install -r requirements.txt`.
3. Run the Django development server: `python manage.py runserver`.
    3.1 If you have installed Docker, you can build an image with: `docker build -t immfly_api .`
    3.2 Then `docker-compose up web` to create the web container, `docker-compose up tests` to create the unit tests container and `docker-compose up ratings ` to create the rating algorithm container.

4. Use a web browser or API client to interact with the REST API.


