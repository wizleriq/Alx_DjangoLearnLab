from django.apps import AppConfig

# bookshelf/apps.py
# def ready(self):
#     import bookshelf.signals  # Ensure this is inside your AppConfig class

# class BookshelfConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'bookshelf'


from django.apps import AppConfig

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    # def ready(self):
    #     import bookshelf.signals  # This ensures your signals are connected
