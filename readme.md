# Dinero app


## Setup dev environment

```bash
pip install -r requirements.txt
```

To create the database,

In the main directory run
```bash
./initdb.sh
```

---




A bit of restructuring has been done, and it might be confusing to look at.
I'll do my best to walk you though.

Check requirements.txt

/*
 * Launching (flask) virtual environment
 */
:dinero: `/flask` - virtual flask environment. To run::
:dir:`dinero`
$ source flask/bin/activate

you should see:
(flask) [some/path]:
in your command line.

"""
should this fail, remove /dinero/flask
then while running python3.5
pip install flask
pyvenv flask
source flask/bin/activate
"""
Note: to deactivate, in the window running the venv, command:
deactivate

/*
 * Run App
 */
(flask) [some/path]: python run.py

Note: if this does not work,
(flask) [some/path]: pip install flask
then run

Note, make sure you have the ::req::``/Flask-SQLAlchemy==2.1`` installed

/*
 * Structure
 */

 /dinero
    /app
       /root
          /__init__.py
          /dinero.py
       /templates
          /index.html
       /__init__.py
    /models
        /Bill.py
        /Customer.py
        /Item.py
        /Resturant.py
    /config.py
    /run.py

/*
 * Base Directory
 */
/dinero = repository
/app = control app directory
/models = models directory
/config.py = environment configuration
/run.py = server launch

/*
 * dinero/app
 */
  /root = root of app
     /__init__.py = creates root of the app as a Blueprint. Good for scaling.
     /dinero.py = ultimately, the controller. right now it has a `model` feel
  /templates = .html files go here. render_template('somefile.html') looks in
               :dir:`templates` for somefile.html.
  /__init__.py = holds class create_app()


/*
 * dinero/models
 */
  /Bill.py = Bill model
  /Customer.py = Customer model
  /Item.py = Menu item model
  /Resturant.py = Resturant model

---
