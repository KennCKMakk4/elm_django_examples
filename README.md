# elm_django_examples
This Repo contains basic examples of using Elm generated Client Code with Django Server 

* Setting up a Virtual Environment
This creates a virtual environment located at your
*HOME* (you only need to do this once and you can put the venv wherever you want)
- Create a venv at home with `python3 -m venv ~/django_env`
- Activate the environment with `source ~/django_env/bin/activate`
- Install *django* and *corsheaders* with 
  ~~~~
  pip install Django
  pip install django-cors-headers
  ~~~~

* Running Django Server
- Make sure the virtual environment is activited
- Run the server with (at port 8000)
  ~~~~
  cd elm_django_examples/django_project
  python manage.py runserver localhost:8000
  ~~~~
- When you're finished, deactivate the virtual environment with the command `deactivate`
