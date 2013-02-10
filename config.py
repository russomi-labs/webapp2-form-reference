from google.appengine.api import app_identity
import logging
import os

app_name = "REPLACE"
app_id = app_identity.get_application_id()
isLocal = os.environ['SERVER_SOFTWARE'].startswith('Dev')

webapp2_config = {}
webapp2_config['webapp2_extras.sessions'] = {
    'secret_key': '1AE9F84E-D822-411C-8586-ABEE310CDE90',
}

webapp2_config['webapp2_extras.auth'] = {
    'user_model': 'models.models.User',
    'cookie_name': 'session_name'
}

webapp2_config['webapp2_extras.jinja2'] = {
    'template_path': 'templates'
}

error_templates = {
    403: 'errors/default_error.html',
    404: 'errors/default_error.html',
    500: 'errors/default_error.html',
}

#: LOCAL ENVIRONMENT overrides all
if (isLocal):
    # define environment specific configuration
    localhost = True
    logging.info('Using localhost configuration in config.py.')

else:

    if (app_id == 'application_id'):
        #: PROD ENVIRONMENT
        localhost = False

    if (app_id == 'application_id_dev'):
        #: DEV ENVIRONMENT
        localhost = False

    if (app_id == 'application_id_qa'):
        #: QA ENVIRONMENT
        localhost = False
