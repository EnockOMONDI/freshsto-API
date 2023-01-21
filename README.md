
# Technical documentation Fresh sto web app 
#### This is an onlineshop application that allows different users to view items on sale and make an order online. Admins are able to view orders made and process orders



# SET UP 
(Ubuntu Development Only) 
### Relational database dependencies (PostgreSQL):
#### Install components for Ubuntu:
```commandline
 sudo apt-get update
```
```commandline
 sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib
```

##### Switch to postgres (PostgreSQL administrative user):
```commandline
 sudo su postgres
```
##### Log into a Postgres session:

```commandline
 psql
```

##### Create database with name ecommerce:
```commandline
 CREATE DATABASE ecommerce;
```
##### Create a database user which we will use to connect to the database:
```commandline
 CREATE USER ecommerce_user WITH PASSWORD 'ecommerce_pass';
```
##### Modify a few of the connection parameters for the user we just created:
```commandline
 ALTER ROLE ecommerce_user SET client_encoding TO 'utf8';
```
```commandline
 ALTER ROLE ecommerce_user SET default_transaction_isolation TO 'read committed';
```
```commandline
 ALTER ROLE ecommerce_user SET timezone TO 'UTC';
```


##### Give our database user access rights to the database we created:
```commandline
GRANT ALL PRIVILEGES ON DATABASE ecommerce TO ecommerce_user; 
```
##### Exit the SQL prompt and the postgres user's shell session:
```commandline
 \q then exit
```
## Quickstart

If you want to have a quick look or just run the project locally for development purposes, you can get started by either forking this repository
or just cloning it directly:

```commandline
git clone 
```

Ideally, create a [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) and install the projects dependencies:

 Activate the virtual environment:
 
```commandline
source ~/.virtualenvs/ecommerce/bin/activate
```

```commandline
pip install -r requirements.txt
```

Create a local database:


```commandline
python manage.py makemigrations
```

```commandline
python manage.py migrate
```

Start development server:

```commandline
python manage.py runserver
```

Open your browser and access the setup page to create an admin account:
site - link [here](http://localhost:8000/admin/)







## How to use as a user
* Open the site - link [here](http://localhost:8000/)
* Create an account if you are new or login to application
* Search for different items 
* Click on desired Item to view
* add to cart and submit to make an order

## How to use as admin
* Open the site - link [here](http://localhost:8000/admin/)
* login to application
* Search for different orders made
* Click on desired Item order to process
 


## Technologies used
* Django - The web framework used
* Python - Language
* html/css/bootstrap4- Used for-frontend
* Postgresql-Database


###### Deployment
* HEROKU


### KNOWN BUGS
- no known bugs


<br>
Github - [Enock OMONDI](https://github.com/EnockOMONDI)

### License
This is an opensource software therefore the license is [MIT](https://choosealicense.com/licenses/mit/)
<br>
Copyright (c) 2018 
