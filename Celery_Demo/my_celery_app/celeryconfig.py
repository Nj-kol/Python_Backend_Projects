
CELERY_IMPORTS = ('tasks') # Import the name of the module containing celery task definitions
CELERY_IGNORE_RESULT = False
BROKER_URL = 'redis://10.159.21.107:30379/0'