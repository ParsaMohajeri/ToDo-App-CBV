# import part
from django.apps import AppConfig

# _____________________________________________________________________________

class AccountsConfig(AppConfig):
    """
    this is a class to make config settings
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
