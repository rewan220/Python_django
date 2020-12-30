Running the Project:

1-download the zip file

2-Go to the project folder in your cmd:
	#cd myproject

3-Create virtual environment with a directory i.e. venv:
	# virtualenv venv
4-Now activate the virtual environment:
    # .../Scripts/activate

5-Check/Show python version:
	# python --version

6-Install all required packages:
      # pip install -r requirements.txt

7-Initialization form the DB migration:
	#python manage.py makemigrations

8-Excute the DB migration:
	#python manage.py migrate

9-Create admin user:
	#python manage.py createsuperuser

10-Run server in a specific port:
	#python manage.py runserver 

by clicking on the url you will be able to access the home page

to access the admin page go to localserver/admin

