# cars-API
## API for get info about cars ordering
### installation
1) update system, pip and install virtualenv
```
$ sudo apt update
$ sudo -H pip3 install --upgrade pip
$ sudo -H pip3 install virtualenv
```

2) create enviroment and activate
```
$ virtualenv env
$ source env/bin/activate
```

3) upload project and install requirements
```
(env) $ git clone https://github.com/andrews-lerk/cars-API.git
(env) $ cd cars-api & pip install requirements.txt
```

4) in settings.py specify your database settings or use default django sqlite for testing

5) make migrate and runserver
```
(env) $ python manage.py migrate
(env) $ python manage.py runserver
```
### usage

#### api documentation you can see in 

http://localhost:8000/swagger/
