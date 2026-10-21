# Learning Python Flask, Networking & SQLite 🐍

## 📌 Overview

This project documents my early progress in learning **Python backend development using Flask**, alongside fundamental networking concepts and database management with SQLite.

My goal is to understand how web servers handle HTTP requests, how routes map requests to Python functions, and how databases store and retrieve data for web applications.

## 🛠️ Technologies Used

* **Python** — Backend programming.
* **Flask** — Lightweight Python web framework for building web applications and REST APIs.
* **Flask-SQLAlchemy** — ORM integration for interacting with databases using Python classes and objects.
* **SQLite** — Lightweight, file-based relational database.
* **PowerShell** — Running commands and managing my Python development environment.

## 📚 What I've Learned

### 1. Flask and Routing

* Creating a Flask application using `Flask(__name__)`.
* Defining URL routes with `@app.route()`.
* Handling HTTP requests with Python functions.
* Returning Python dictionaries as JSON responses.
* Creating dynamic routes using URL parameters, such as `/users/<int:user_id>`.

### 2. Basic Networking Concepts

* Understanding URLs, IP addresses, ports, and network protocols.
* Understanding `127.0.0.1` as the localhost loopback address.
* Exploring how clients communicate with servers through IP addresses and ports.
* Understanding the roles of HTTP, HTTPS, TCP, and DNS.
* Running a local Flask development server on port `5000`.

### 3. SQLite and Database Integration

* Configuring an SQLite database using Flask-SQLAlchemy.
* Defining database models and columns using Python classes.
* Understanding primary keys, data types, and nullable fields.
* Creating database tables with `db.create_all()`.
* Inserting records and retrieving them using SQLAlchemy queries.
* Converting database records into JSON responses.
* Learning why changes to existing database models may require schema migrations.

## 🚀 Current Implementation

The application currently includes:

* A `/colors` endpoint that retrieves color records from SQLite.
* A `/food` endpoint that returns sample food data.
* A dynamic `/users/<int:user_id>` endpoint that accepts a user ID.

The `/colors` endpoint demonstrates the connection between a Flask route, a SQLAlchemy model, an SQLite database, and a JSON response.

## ▶️ Running the Project

**1. Install the dependencies:**

```bash
pip install flask flask-sqlalchemy
```

**2. Start the Flask development server:**

```bash
flask --app app run
```

**3. Open the endpoints in your browser:**

* Colors: `http://127.0.0.1:5000/colors`
* Food: `http://127.0.0.1:5000/food`
* Example user: `http://127.0.0.1:5000/users/1`

## 🎯 Next Steps

* Learn HTTP methods: GET, POST, PUT, PATCH, and DELETE.
* Implement CRUD operations with SQLite and SQLAlchemy.
* Understand request bodies, query parameters, and HTTP status codes.
* Learn database migrations and proper error handling.
* Build more complete REST APIs and connect them to frontend applications.

## 📈 Learning in Progress

This is a hands-on learning project focused on understanding backend development fundamentals, networking, and database integration one concept at a time.

**The goal is not just to make the code work, but to understand what happens behind the scenes.**
