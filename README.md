# My Solution

This is my solution to the problem at hand. Here's a brief overview of what my solution does:

- It uses Python 3.10.3 and the Django web framework.
- It includes a database schema and data migrations to set up the database.
- It provides a REST API for get resources information.
- It includes unit tests for the API endpoints,database models and management commands.

## Installation

To install and run the solution, follow these steps:

1. Clone the repository to your local machine (git clone https://github.com/peredirtbike/immfly_technical_test.git).
2. Install the required dependencies using pip: `pip install -r requirements.txt`.
3. Run the Django development server: `python manage.py runserver`.
4. Use a web browser or API client to interact with the REST API.

If you want to run it through Docker:

1. Install Docker https://www.docker.com/get-started/
2. Run `docker build -t immfly_api . ` (this command will install all the dependencies on the requirements.txt file)
3. Run `docker compose up web ` to start the web server.
4. Run `docker compose up tests ` to start the tests server.
5. Run `docker compose up tests ` to start the ratings server.


