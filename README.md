# Flask CRUD Application

This is a simple python CRUD (Create, Read, Update, Delete) application built with Flask and SQLite. It allows users to manage and add data of product details.

## Features

- Create a new item
- Read (view) items
- Update existing items
- Delete items
- Uses SQLite for data storage

## Output

- name:[Textbox]
- price:[Textbox]
-    [add button]

Table of database:
| Name     | Price     | Actions |
| ---      | ---       | --      |
| Tshirts  | 600       | [Tshirts][600][update_button][delete_button]
| Jeans    | 1000      | [Jeans][600][update_button][delete_button]

## Dependencies

This project requires the following Python packages:
- **Flask**:This is python framework for used to build the web application.
- **SQLite**: A tool for handling SQLite database migrations for Flask applications.
- **Flask-RESTful**: An extension for Flask that adds support for quickly building REST APIs.
