import os
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')

    django.setup()
    from django.core import management
    from address.management.commands import deadlinecrossed

    management.call_command('deadlinecrossed', verbosity=0, interactive=False)
