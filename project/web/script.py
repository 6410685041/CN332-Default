import os
import django
import subprocess

try:
    # Set up Django environment
    from key import (
        github_cid,
        github_csecrets,
        google_cid,
        google_csecrets,
        facebook_cid,
        facebook_csecrets,
        ms_cid,
        ms_csecrets,
    )

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carDetection.settings")
    django.setup()
except Exception as e:
    # Handle the exception (e.g., log it)
    print(f"An error occurred: {e}")
    print("Enter the password: ", end="")
    subprocess.run(
        [
            "openssl",
            "enc",
            "-d",
            "-aes-256-cbc",
            "-in",
            "key.enc",
            "-out",
            "key.py",
            "-k",
            input(),
        ]
    )
    print("decryption DONE!")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carDetection.settings")
    django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from django.core.management import call_command
from user.models import Profile
from process.models import Intersection, Task, Result
from datetime import datetime
import pytz
import argparse
from django.core.exceptions import ObjectDoesNotExist
import json


def run_migrations():
    print("Running migrations...")
    subprocess.run(["python", "manage.py", "makemigrations", "user"])
    subprocess.run(["python", "manage.py", "makemigrations", "process"])
    call_command("makemigrations")
    call_command("migrate")
    print("Migrations complete.")


def create_initial_data(
    github_cid,
    github_csecrets,
    google_cid,
    google_csecrets,
    facebook_cid,
    facebook_csecrets,
):
    print("Creating initial data...")
    # Create some initial data
    try:
        site = Site.objects.get(id=1)
        # If site with ID 1 exists, update its attributes
        site.name = "127.0.0.1"
        site.domain = "127.0.0.1"
        site.save()
    except ObjectDoesNotExist:
        # If site with ID 1 doesn't exist, create a new one
        site = Site.objects.create(id=1, name="127.0.0.1", domain="127.0.0.1")
    github = SocialApp.objects.create(
        provider="github",
        name="Github",
        client_id=github_cid,
        secret=github_csecrets
    )
    google = SocialApp.objects.create(
        provider="google",
        name="Google",
        client_id=google_cid,
        secret=google_csecrets
    )
    facebook = SocialApp.objects.create(
        provider="facebook",
        name="Facebook",
        client_id=facebook_cid,
        secret=facebook_csecrets,
    )
    github.sites.set([site])
    google.sites.set([site])
    facebook.sites.set([site])

    # create profile
    username = "default"
    email = "default@example.com"
    password = "default1234"
    default_user = Profile.objects.create(
        username=username,
        email=email,
    )
    default_user.set_password(password)
    default_user.save()
    # create intersection
    intersection = Intersection.objects.create(
        intersection_name="Default Intersection",
        location="13.755871860300672, 100.52335739135744",
    )
    print("Default intersection Created")
    # create task
    Task.objects.create(
        status="Created",
        video="static/video/test1.MP4",
        intersection=intersection,
        owner=default_user,
        created_at=datetime.now(pytz.timezone("Asia/Bangkok")),
    )
    print("Default task Created")
    # create result
    loop_open = open('static/json/example_loop.json')
    loop = json.load(loop_open)
    result_open = open('static/json/example_result.json')
    result = json.load(result_open)
    Result.objects.create(
        result_name="Default result",
        video="static/video/test1.MP4",
        owner=default_user.username,
        intersection=intersection,
        created_at=datetime.now(pytz.timezone("Asia/Bangkok")),
        loop_json=loop,
        result_json=result,
    )
    print("Default result Created")
    print("Initial data created.")


def create_superuser():
    username = "admin"
    email = "admin@example.com"
    password = "admin1234"
    call_command("createsuperuser", username=username, email=email, interactive=False)
    # Set the password for the created superuser
    user = Profile.objects.get(username=username)
    user.set_password(password)
    user.save()
    print("Create super user complete.")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Script to help doing the things")
    parser.add_argument("-r", action="store_true", help="Reset")
    parser.add_argument("-s", action="store_true", help="Setting")
    parser.add_argument("-a", action="store_true", help="Activate docker")
    args = parser.parse_args()
    if args.r:
        with open("reset_list.txt", "r") as file:
            for to_clear in file.read().split("\n"):
                subprocess.run(["rm", "-rf", to_clear])
        print("clear file in reset_list DONE!")
    if args.s:
        run_migrations()
        create_initial_data(
            github_cid,
            github_csecrets,
            google_cid,
            google_csecrets,
            facebook_cid,
            facebook_csecrets,
        )
        create_superuser()
    if args.a:
        subprocess.run(["docker", "compose", "down"])
        subprocess.run(["docker", "compose", "up", "-d"])
