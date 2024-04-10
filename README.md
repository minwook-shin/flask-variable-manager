# Flask Variable Manager

The Flask Variable Manager is a Flask extension that allows you to manage variables within your Flask application. 

It provides an interface to set and get variables, and even render them in Jinja2 templates. 

This can be useful when you need to share data across different parts of your application.

## Installation

To install the Flask Variable Manager, you can use pip:

```bash
pip install flask-variable-manager
```

## Usage

First, import the `VariableManagerExtension` from the `flask_variable_manager` package:

Then, create an instance of the `VariableManagerExtension` and initialize it with your Flask application:

```python
from flask import Flask
from flask_variable_manager import VariableManagerExtension

vm = VariableManagerExtension()
app = Flask(__name__)
vm.init_app(app)
```

Now, you can use the `VariableManagerExtension` to set and get variables in your Flask routes. 

```python
vm._local['my_var'] = 'Hello, World!'
```

```python
vm._local['my_var']
```

## Routes

### Render a string as a Jinja2 template

This route allows you to render a string as a Jinja2 template. 

It accepts a POST request at the `/vm/render` endpoint. 

### Set a user-defined variable

This route allows you to set a user-defined variable. 

It accepts a POST request at the `/vm/var` endpoint. 

### Get all user-defined variables

This route allows you to get all user-defined variables. 

It accepts a GET request at the `/vm/var` endpoint. 

(or `vm/vars` for the multiple count of the variable)

### Remove a user-defined variable

This route allows you to remove a user-defined variable.

It accepts a DELETE request at the `/vm/var` endpoint.

(or `vm/vars` for the multiple count of the variable)

### Run a Python script and return the result

This route allows you to run a Python script and return the result.

It accepts a POST request at the `/py/runner` endpoint.

```python
import platform
from flask import g
data = additionalProp + "-" + platform.platform()
g.local['saved_user_variable'] = data
return data
```

## License

This project is licensed under the terms of the MIT license.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.