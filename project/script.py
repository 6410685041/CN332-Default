import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from key import github_cid, github_csecrets, google_cid, google_csecrets
from django.core.management import call_command
from django.contrib.auth.models import User

def run_migrations():
    print("Running migrations...")
    call_command("makemigrations")
    call_command("migrate")
    print("Migrations complete.")
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin1234'
    call_command('createsuperuser', username=username, email=email, interactive=False)
    # Set the password for the created superuser
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print("Create super user complete.")

def create_initial_data():
    print("Creating initial data...")
    # Create some initial data
    site = Site.objects.create(name='127.0.0.1', domain='127.0.0.1')
    github = SocialApp.objects.create(
        provider='github',
        name='Github',
        client_id=github_cid,
        secret=github_csecrets
    )
    google = SocialApp.objects.create(
        provider='google',
        name='Google',
        client_id=google_cid,
        secret=google_csecrets
    )
    github.sites.set([site])
    google.sites.set([site])
    print("Initial data created.")

if __name__ == "__main__":
    run_migrations()
    create_initial_data()