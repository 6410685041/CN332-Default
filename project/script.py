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
import subprocess
import argparse

def decrypt_file(input_file, output_file, password):
    # Construct the OpenSSL command
    openssl_command = [
        'openssl',
        'enc',
        '-d',
        '-aes-256-cbc',
        '-in',
        input_file,
        '-out',
        output_file,
        '-k',
        password
    ]

    # Run the OpenSSL command
    subprocess.run(openssl_command)

def run_migrations():
    print("Running migrations...")
    call_command("makemigrations")
    call_command("migrate")
    print("Migrations complete.")

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
    parser.add_argument('-i', "--input", default="key.enc", help='Input encrypted file path')
    parser.add_argument('-o', "--output", default="key.py", help='Output decrypted file path')
    parser.add_argument('-r', '--reset', action='store_true', help='Reset Database')
    parser.add_argument('-p', '--password', required=True, help='Password for decryption')
    args = parser.parse_args()
    
    if args.r:
        subprocess.run("rm -rf db.sqlite3")

    decrypt_file(args.input_file, args.output_file, args.password)
    run_migrations()
    create_initial_data()
    create_superuser()
