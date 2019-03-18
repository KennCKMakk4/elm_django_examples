# elm_django_examples
contains basic examples of using elm with django server

Run django_project inside a virtual environment (follow these instructions to create a run a venv from your home)

- Create a venv at home with `python3 -m venv ~/django_env`
- Activate the environment with `source ~/django_env/bin/activate`
- Install *django* and *corsheaders* with 
  ~~~~
  pip install Django
  pip install django-cors-headers
  ~~~~
- Run the server with (at port 8000)
  ~~~~
  cd elm_django_examples/django_project
  python manage.py runserver localhost:8000
  ~~~~
- When your finished, deactivate the virtual environment with the command `deactivate`
