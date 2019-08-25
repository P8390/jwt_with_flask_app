<!-----
Author: Pankaj Kumar
Updated at: 12:20 AM, 25 August, 2019
----->

# Jwt with Flask APP - Setup Manual

This project has implementation of JWT with Flask App using Mysql, Sqlalchemy, Flask and 12 Factor APP

### 1. Virtual Environment

First of all, you need to create virtual environment for your project. For this you need tool <code>virtualenv</code>. If you do not have this, it can be installed by running the following command


```
pip install virtualenv
```

Now that you have the required tool, we can create isolated environment for our development by executing following commands

```
python3 -m venv env
source env/bin/activate
```

### 2. Package Installation

Having done with setting with virtual environment, we are ready to install all dependencies.

```
pip install -r requirements.txt
```

### 3. Running Flask APP
./run_wit_env.sh env_var.env python run_app.py

* Serving Flask app "Flask Jwt" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on https://127.0.0.1:5000/ (Press CTRL+C to quit)


### 4. paste below url in postman for testing
http://127.0.0.1:5000/api/v1

### 5. Check url_list.py for different endpoint execution
http://127.0.0.1:5000/api/v1/login