# import part
from django.apps import AppConfig
# ______________________________________________________________________________

class BlogConfig(AppConfig):
    """
    this is a class to make config settings
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
