import pytest
from flask import Flask

from flask_variable_manager.extension.variable_manager import VariableManagerExtension


def test_variable_manager_extension_initialization():
    app = Flask(__name__)
    vm = VariableManagerExtension(app)
    assert vm is not None


def test_variable_manager_extension_without_app_initialization():
    vm = VariableManagerExtension()
    assert vm is not None


def test_variable_manager_extension_init_app():
    app = Flask(__name__)
    vm = VariableManagerExtension()
    vm.init_app(app)
    assert vm is not None


def test_variable_manager_extension_key_error():
    app = Flask(__name__)
    vm = VariableManagerExtension(app)
    with pytest.raises(KeyError):
        _ = vm._local['non_existent_key']
