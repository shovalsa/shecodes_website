# she codes; website

A Django based website for the she codes; organization

### Install instructions
Create virtual environment:
```ruby
$> python -m venv myvenv
```

To run virtual environment use:

```ruby
$> myvenv\Scripts\activate
```

Install these dependencies:

```ruby
$> pip install django~=1.10.0
$> pip install django-bootstrap3
$> pip install pillow
$> pip install pytz
```
This is best done (and more up-to-date) via requirements.txt
```ruby
$> pip install -r requirements.txt
```
Unzip static.zip inside sc_project>scsite>static. Note that a file sensitive.py is missing. In need, ask me for the file.

Finally run the server to view and work on the website:
```ruby
$> python manage.py runserver
```
