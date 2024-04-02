.. flask-variable-manager documentation master file, created by
   sphinx-quickstart on Tue Apr  2 11:53:25 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to flask-variable-manager's documentation!
==================================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:


Contents
--------

.. toctree::

   flask_variable_manager
   generated/flask_variable_manager.VariableManagerExtension


Flask Variable Manager
======================

The Flask Variable Manager is a Flask extension that allows you to manage variables within your Flask application.

It provides an interface to set and get variables, and even render them in Jinja2 templates.

This can be useful when you need to share data across different parts of your application.

Installation
------------

To install the Flask Variable Manager, you can use pip:

```bash
pip install flask-variable-manager
```

Usage
-----

First, import the `VariableManagerExtension` from the `flask_variable_manager` package:

Then, create an instance of the `VariableManagerExtension` and initialize it with your Flask application:

Now, you can use the `VariableManagerExtension` to set and get variables in your Flask routes.

Render a string as a Jinja2 template
------------------------------------

- [POST] `/vm/render`

This route allows you to render a string as a Jinja2 template.

It accepts a POST request at the `/vm/render` endpoint.

Set a user-defined variable
---------------------------

- [POST] `/vm/var`

This route allows you to set a user-defined variable.

It accepts a POST request at the `/vm/var` endpoint.

Get all user-defined variables
------------------------------

- [GET] `/vm/var`

This route allows you to get all user-defined variables.

It accepts a GET request at the `/vm/var` endpoint.

License
-------

This project is licensed under the terms of the MIT license.
