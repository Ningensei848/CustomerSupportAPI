# cf. https://fastapi.tiangolo.com/tutorial/bigger-applications/

"""
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── routers
│       ├── __init__.py
│       ├── items.py
│       └── users.py

The app directory contains everything.
This app directory has an empty file app/__init__.py.
So, the app directory is a "Python package" (a collection of "Python modules").
The app directory also has a app/main.py file.
As it is inside a Python package directory (because there's a file __init__.py), it is a "module" of that package: app.main.
There's a subdirectory app/routers/.
The subdirectory app/routers also has an empty file __init__.py.
So, it is a "Python subpackage".
The file app/routers/items.py is beside the app/routers/__init__.py.
So, it's a submodule: app.routers.items.
The file app/routers/users.py is beside the app/routers/__init__.py.
So, it's a submodule: app.routers.users.
"""
