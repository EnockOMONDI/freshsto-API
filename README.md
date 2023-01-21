![Landing page](1landing.png)
![shop](3landing.png)
![Make order](2landing.png)
![mobile view](mobileview.png)
# Technical documentation Fresh sto web app 
#### This is an onlineshop application that allows different users to view items on sale and make an order online. Admins are able to view orders made and process orders

#### By ****Enock OMONDI****

# SET UP Requirements
## Relational database dependencies (PostgreSQL):
#### Install components for Ubuntu:
sudo apt-get update
sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib

##### Switch to postgres (PostgreSQL administrative user):
sudo su postgres

##### Log into a Postgres session:
psql

##### Create database with name ecommerce:
CREATE DATABASE ecommerce;

##### Create a database user which we will use to connect to the database:
CREATE USER ecommerce_user WITH PASSWORD 'ecommerce_pass';

##### Modify a few of the connection parameters for the user we just created:
ALTER ROLE ecommerce_user SET client_encoding TO 'utf8';
ALTER ROLE ecommerce_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ecommerce_user SET timezone TO 'UTC';

##### Give our database user access rights to the database we created:
GRANT ALL PRIVILEGES ON DATABASE ecommerce TO ecommerce_user;

##### Exit the SQL prompt and the postgres user's shell session:
\q then exit

##### Activate the virtual environment:
source ~/.virtualenvs/ecommerce/bin/activate

##### Make Django database migrations: 
python manage.py makemigrations
python manage.py migrate

#### Use admin interface:
##### Create an admin user:
python manage.py dosuperuser
Run the project locally:
python manage.py runserver
Navigate to:
http://localhost:8000/admin/

## How to use as a user
* Open the site - link [here]()
* Create an account if you are new or login to application
* Search for different items 
* Click on desired Item to view
* add to cart and submit to make an order

## How to use as admin
* Open the site - link [here]()
* login to application
* Search for different orders made
* Click on desired Item order to process
* 


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
