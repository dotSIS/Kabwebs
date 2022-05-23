# uBLOG
uBLOG is a university blog web app for students and staffs. Hear from us.

## Installation
- `git clone https://github.com/dotSIS/uBLOG.git`
- `cd uBLOG`
- `pip install -r requirements.txt`
- `cd backend/uBLOG`
- `python manage.py runserver`

## Status
- Temporary Django as Frontend
- Django REST Framework API complete
- Proper Front-end not present

## Temoporary Front-end
- `localhost:8000`
- NOTE: Update and delete not present.
- NOTE: Temporary Front-end is not connected to the api and have a database on its own.

## DJango REST Framework endpoints
- `localhost:8000/api/`
- `localhost:8000/api/users/`
- `localhost:8000/api/users/<int:pk>/`
- `localhost:8000/api/blogs/`
- `localhost:8000/api/blogs/<int:pk>`
- `localhost:8000/api/comments/`
- `localhost:8000/api/comments/<int:pk>`
