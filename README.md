# Elm Django Examples
This Repo contains basic examples of using Elm generated Client Code with Django Server 

## Setting up a Virtual Environment

This creates a virtual environment located at your
*HOME* (you only need to do this once and you can put the venv wherever you want)
- Create a venv at home with `python3 -m venv ~/django_env`
- Activate the environment with `source ~/django_env/bin/activate`
- Install the required packages from requirements.txt with
  ~~~~
  pip install -r requirements.txt
  ~~~~
- When you're finished, deactivate the virtual environment with the command `deactivate`

## Running Django Server (On Local Machine)

- Make sure the virtual environment is activated
- Run the server with (at port 8000)
  ~~~~
  cd elm_django_examples/django_project
  python manage.py runserver localhost:8000
  ~~~~
- (Press Ctrl-c to quit django_server)

## Running Elm Reactor (On Local Machine)
- If you're running both Elm Reactor and Django on your local machine, make sure to run them on different ports
  ~~~~
  cd elm_django_examples/elm_examples
  elm reactor --port=8001
  ~~~~
- Go to localhost:8001 in your browser
- Select the elm file you want to run
- (Press Ctrl-c to quit elm reactor)
