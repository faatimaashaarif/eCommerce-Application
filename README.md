# eCommerce-Application
A fully operational eCommerce Selling store with HTML. CSS, Python and Flask to offer implemented features.

Project Overview

This is a full-stack web application for managing an online store.
Users can browse products, view details, add items to a shopping cart, and simulate a checkout.
Admins can manage the product catalog, track inventory, and export product data for reporting.

The system is lightweight, using Flask for the backend and SQLite for storage, making it easy to deploy for small-scale projects or as a learning tool.

Features

Product Catalog: Display products with name, description, price, and stock.
Shopping Cart: Users can add products to the cart and see total prices.
Admin Panel: Add, edit, or delete products, and view the product list.
JSON Export: Export the full product catalog for reporting or integration.
SQLite Backend: No external database setup required.
Frontend: Simple HTML/CSS templates with clear product display.
Dependencies

Python 3.x
Flask
Install Flask using pip:

pip install flask

To run:

python app.py

http://127.0.0.1:5000/ -> Product catalog http://127.0.0.1:5000/admin -> Admin panel http://127.0.0.1:5000/cart -> Shopping cart
