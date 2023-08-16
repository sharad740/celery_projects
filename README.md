# Installation

Setup Redis server in your system or in docker container

Setup Saperate virtual env

```
pip install -r requirements.txt
```

Setup your Email Account in projects settings.py
```
EMAIL_HOST = "mail.mydomain.com"
EMAIL_HOST_USER = "smtp@webmaster.com"
EMAIL_HOST_PASSWORD = "smtpuserpass"
```

Open terminal and start Broker

```
python -m celery -A project worker --pool=solo -l info
```
Start python server

```
python manage.py runserver
```

