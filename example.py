from flasgger import Swagger
from flask import Flask

from flask_variable_manager import VariableManagerExtension

vm = VariableManagerExtension()

app = Flask(__name__)
vm.init_app(app)

Swagger(app)

if __name__ == '__main__':
    app.run(debug=True, port=8888)
