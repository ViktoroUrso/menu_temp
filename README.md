# menu_temp
Django template tag apps which draws a tree-like menu in your page

## How to use
* install requirements from 'menu_temp/'
```commandline
pip install -r requirements.txt
```
* create superuser
```commandline
postgres -c psql postgres
psql-# ALTER USER admin WITH PASSWORD 'password';
```
* create db
```commandline
psql-# CREATE DATABASE db_menu WITH OWNER admin;
```
* create migrations from 'menu_temp/'
```commandline
python manage.py makemigrations
python manage.py migrate
```
* load templatetags in your page template
```commandline
{% load make_menu %}
```
* go to admin of Django site (in menu "Tag menus") and add menus and menu's items
```commandline
http://localhost:8000/admin
```

* insert your menu by its name ("menu_name") in your page template
```commandline
<div class="some-class">
    {% make_menu 'menu_name' %}
</div>
```
You can use not-root 'name' then all menu will be drawn and node with 'name' will be **selected**
* run your project
```commandline
python manage.py runserver
```