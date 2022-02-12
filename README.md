# form project

form to sign up and login with phone number

## before run
download & install node.js

change .env-sample to .env and set your sms api-key

# run frontend

```
cd form-project/frontend
npm i
npm start
```

# run backend

```
$ pip install virtualenv
$ cd backend
$ virtualenv env (create env just once)
$ env/scripts/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

## api documentions

127.0.0.1:8000/swagger

## api url

127.0.0.1:8000/otp/request/ <br />
127.0.0.1:8000/otp/verify/
