# Indicators

This is a project to have a dashbord that display indicators used on a humanitarian situation 

## Features


- Django 2.0+
- Uses Pipenv - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with django-configurations.
- Get value insight and debug information while on Development with django-debug-toolbar.
- Collection of custom extensions with django-extensions.
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
PostgreSQL database support with psycopg2.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required modules.

```bash
git clone https://github.com/unicefburundi/Indicators.git
cd Indicators/
pip install -r requirements.txt
python manage.py runserver
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
