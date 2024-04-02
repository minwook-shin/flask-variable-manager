import importlib

from flask import g, jsonify, request, render_template_string


def define_routes(app):
    @app.route('/vm/render', methods=['POST'])
    def render_template():
        """
        ---
        tags:
          - Rendering
        summary: Render a string as a Jinja2 template
        description: This endpoint allows you to render a string as a Jinja2 template.
        parameters:
          - in: formData
            name: template_string
            type: string
            required: true
            description: The string to render as a Jinja2 template.
        responses:
          200:
            description: The rendered template
            schema:
              type: string
        """
        template_string = request.form.get('template_string', '')
        rendered_template = render_template_string(template_string, _local=g.local, system=g.system)

        return rendered_template

    @app.route('/vm/var', methods=['POST'])
    def set_variable():
        """
        ---
        tags:
          - Variables
        summary: Set a user-defined variable
        description: This endpoint allows you to set a user-defined variable.
        parameters:
          - in: formData
            name: key
            type: string
            required: true
            description: The key of the variable.
          - in: formData
            name: value
            type: string
            required: true
            description: The value of the variable.
        responses:
          200:
            description: The variable has been set successfully.
        """
        key = request.form.get('key')
        value = request.form.get('value')

        g.local[key] = value
        return jsonify({'message': 'The variable has been set successfully.'})

    @app.route('/vm/vars', methods=['POST'])
    def set_variables():
        """
        ---
        tags:
          - Variables
        summary: Set multiple user-defined variables
        description: This endpoint allows you to set multiple user-defined variables.
        parameters:
          - in: body
            name: variables
            description: The variables to set.
            schema:
              type: object
              additionalProperties:
                type: string
        responses:
          200:
            description: The variables have been set successfully.
        """
        variables = request.get_json()

        for key, value in variables.items():
            g.local[key] = value

        return jsonify({'message': 'The variables have been set successfully.'})

    @app.route('/vm/var', methods=['GET'])
    def get_variables():
        """
        ---
        tags:
          - Variables
        summary: Get all user-defined variables
        description: This endpoint allows you to get all user-defined variables.
        responses:
          200:
            description: The variables have been retrieved successfully.
            schema:
              type: object
              properties:
                variables:
                  type: object
                  description: The user-defined variables.
        """
        return jsonify(g.local.to_dict())


class VariableManagerExtension:
    def __init__(self, app=None):
        self._local = Local()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.before_request(self.before_request)
        define_routes(app)

    def before_request(self):
        g.system = System()
        g.local = self._local


class System:
    def __init__(self):
        self._modules = {}

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __getitem__(self, name):
        if not isinstance(name, str):
            raise TypeError("Module name must be a string")

        if name in self._modules:
            return self._modules[name]

        try:
            module = importlib.import_module(name)
            self._modules[name] = module
            return module
        except ImportError:
            raise ImportError(f"Module '{name}' not found")


class Local:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found")
        return self._data[key]

    def to_dict(self):
        return self._data
