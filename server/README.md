Late Show API

A Flask REST API for managing episodes, guests, appearances, and users for a late night TV show. Built with PostgreSQL, Flask-JWT-Extended for authentication, and follows MVC architecture.
Features

    User Registration & Login (JWT Auth)
    Episode Management: List, retrieve, and delete episodes (with cascade delete for appearances)
    Guest Management: List all guests
    Appearance Management: List and create appearances (protected)
    User Management*: List all users
    Validation*: Data integrity for ratings and foreign keys

Technologies Used

    Flask
    Flask-SQLAlchemy
    Flask-Migrate
    Flask-JWT-Extended
    PostgreSQL

Folder Structure

server/
  app.py
  config.py
  seed.py
  models/
    __init__.py
    user.py
    guest.py
    episode.py
    appearance.py
  controllers/
    __init__.py
    user_controller.py
    guest_controller.py
    episode_controller.py
    appearance_controller.py
    auth_controller.py
migrations/
README.md

Setup Instructions
Clone the repository
https://github.com/Bree-M/late-show-api-challenge.git
git clone <> cd lateshow

2. **Install dependencies**
   ```bash
pipenv install --dev
pipenv shell

Configure PostgreSQL

    Create a PostgreSQL user and database:

    CREATE USER brenda WITH PASSWORD 'brenda1234';
    ALTER USER brenda CREATEDB;
    CREATE DATABASE late_show_db OWNER brenda;

    The default config uses: postgresql://brenda:brenda1234@localhost:5432/late_show_db
    To change, edit server/config.py or set the DATABASE_URI environment variable.

Run migrations and seed the database

export FLASK_APP=server/app.py flask db migrate -m "initial migration" flask db upgrade python server/seed.py

5. **Run the server**
   ```bash
flask run --port=5002

The API will be available at http://127.0.0.1:5002
Notes

    All passwords are hashed.
    All data validations and foreign key constraints are enforced.
    Use the /users endpoint to verify seeded users: carren caro, ann anne, beth, brenda.

License
MIT