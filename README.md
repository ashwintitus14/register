# register
An open source student record management system built using Django.

## Installation
* Install virtualenv, django.
* Install mysqlclient. (https://pypi.org/project/mysqlclient/)
* Change db backend to MySQL. (https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database)
* Create superuser.

## Files changed
* settings.py
* new.html
* base_generic.html
* index.html
* models.py

## TODO

* [x] Create and register the studreg application.
* [x] Change time zone.
* [x] Add paths to urls.py.
* [x] Change backend to MySQL from SQLite.
* [x] Create data models for student details.
* [x] Register models to admin page.
* [x] Create an index/home page.
* [ ] Modify admin page.
* [x] Create ModelForm.
* [ ] Change dateinput to DateInput widget.
* [x] Create form to add admission number.
* [ ] Copy address if same.
* [ ] Add validation functions to form.
* [ ] Setup backups for MySQL database.
* [ ] Change bootstrap source from CDN to local.
* [ ] Deploy

## Changing form style
* https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html

## Deployment notes
(https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04)
* ssh into machine.
* sudo apt-get update
* sudo apt-get upgrade
* hostnamectl set-hostname django-server //Setting the hostname
* nano /etc/hosts
  * Add IP address of machine after localhost
  * IP_ADDRESS django-server
* adduser dj
* adduser dj sudo
* login as dj
* -----------------
* sudo apt-get install ufw (uncomplicated firewall)
* sudo ufw default allow outgoing
* sudo ufw default deny incoming
* sudo ufw allow 8000 (django development server)
* sudo ufw enable
* sudo ufw status
* -----------------
* Deployment of django app
  * pip freeze > requirements.txt (done already)
  * clone django app to server
  * sudo apt-get install python3-pip
  * sudo apt-get install python3-venv
  * python3 -m venve django-project/venv
  * source venv/bin/activate
  * pip install -r requirements.txt
  * Change settings.py
    ALLOWED_HOSTS = ['IP_ADDRESS']
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  * python manage.py collectstatic
  * python manage.py runserver 0.0.0.0:8000
  * cd
  * sudo apt-get install apache2
  * sudo apt-get install libapache2-mod-wsgi-py3
  * cd /etc/apache2/sites-available
  * sudo cp 00-default.conf django_project.conf
  * sudo nano django_project.conf (https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/snippets/django_project.conf)
    * Before </VirtualHost>
      * ```
      Alias /static /home/user/django_project/static
      <Directory /home/user/django_project/static>
            Require all granted
      </Directory>
      Alias /media /home/user/django_project/media
      <Directory /home/user/django_project/media>
            Require all granted
      </Directory>
      <Directory /home/user/django_project/django_project>
        <Files wsgi.py>
            Require all granted
        </Files>
      </Directory>
      
      WSGIScriptAlias / /home/user/django_project/django_project/wsgi.py
      WSGIDaemonProcess django_app python-path=/home/user/django_project...
      WSGI...
      ```
   * sudo a2ensite django_project
   * sudo a2dissite 000-default.conf
   * sudo chown :www-data django_project/db
   * sudo chown :www-data django_project/
      
      
      
      
      
      
      
      
      
