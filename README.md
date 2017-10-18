# handkeinzungen-app
An app to publish &amp; analyze the data in the project Handke: in Zungen

## install

1. Download or Clone this repo
2. Adapt the information in `webpage/metadata.py` according to your needs.
3. Create an virtual environment and run `pip install -r requirements.txt`

### first steps

This projects uses modularized settings (to keep sensitive information out of version control or being able to use the same code for development and production). Therefore you'll have to append all `manage.py` commands with a `--settings` parameter pointing to the settings file you'd like to run the code with. For development just append `--settings={nameOfYouProject}.settings.dev` to the following commands, e.g. `python manage.py makemigrations --settings=hiz.settings.dev`

4. Run `makemigrations`, `migrate`, and `runserver` and check [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Tests

To get needed software you can run

    pip install -r requirements_test.txt

To run the tests execute

    python manage.py test --settings=hiz.settings.test
