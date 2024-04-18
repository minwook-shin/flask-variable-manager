# Changelog

## [Unreleased]

## 0.4.1 - 2024-04-18

### Added

- add documentation for the all methods in the API

## 0.4.0 - 2024-04-17

### Added

- third-party python packages installation and uninstallation
  - added `py/packages` GET Method to check the list of python packages
  - added `py/install`, `py/uninstall` POST Method to install and uninstall a python package

## 0.3.1 - 2024-04-12

### Fixed

- Fixed referencing flask versions as outdated.
    - Updated the `flask` version to `3.0.3`.

## 0.3.0 - 2024-04-10
### Added
- Added `py/runner` POST Method to run a Python script
  - access the variable manager to get and set variables
  - return and save variables value

```python
# import packages
import platform
from flask import g
# used to get the value of a user-defined variable and built-in package
data = additionalProp + "-" + platform.platform()
# save the value of the user-defined variable or return variable
g.local['saved_user_variable'] = data
return data
```

## 0.2.0 - 2024-04-03
### Added
- Added `vm/vars` DELETE Method to clear all user-defined variables
- Added `vm/var` DELETE Method to clear a single user-defined variable

## 0.1.0 - 2024-04-02
### Added
- Added `vm/vars` POST Method to set all user-defined variables

## 0.0.1 - 2024-04-02
### Added
- Initial release
    -