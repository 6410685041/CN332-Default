import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carDetection.settings")
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from django.core.management import call_command
from django.contrib.auth.models import User
import subprocess
import argparse
from django.core.exceptions import ObjectDoesNotExist
from key import github_cid, github_csecrets, google_cid, google_csecrets

def run_migrations():
    print("Running migrations...")
    call_command("makemigrations")
    call_command("migrate")
    print("Migrations complete.")

def create_initial_data():
    print("Creating initial data...")
    # Create some initial data
    try:
        site = Site.objects.get(id=1)
        # If site with ID 1 exists, update its attributes
        site.name = '127.0.0.1'
        site.domain = '127.0.0.1'
        site.save()
    except ObjectDoesNotExist:
        # If site with ID 1 doesn't exist, create a new one
        site = Site.objects.create(id=1, name='127.0.0.1', domain='127.0.0.1')
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

def create_superuser():    
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin1234'
    call_command('createsuperuser', username=username, email=email, interactive=False)
    # Set the password for the created superuser
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print("Create super user complete.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Decrypt file using OpenSSL')
    parser.add_argument('-i', default="key.enc", help='Input encrypted file path')
    parser.add_argument('-o', default="key.py", help='Output decrypted file path')
    parser.add_argument('-r', action='store_true', help='Reset Database')
    parser.add_argument('-e', action='store_true', help='install requirements to environment')
    args = parser.parse_args()
    if args.e:
        subprocess.run(["pip", "install", "-r", "requirements.txt"])
    if args.r:
        subprocess.run(["rm", "-rf", "db.sqlite3"])
        subprocess.run(["rm", "-rf", "**/migrations"])
    run_migrations()
    create_initial_data()
    create_superuser()
