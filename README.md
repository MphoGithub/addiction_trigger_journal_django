# Addiction Trigger Journal

Triggers is a web app for recording addiction triggers and coping strategies. Each user has their own journal which they can use to track what happened, how they felt and what helped.

## Live Demo
https://addiction-trigger-journal.onrender.com

*Note: hosted on Render's free tier — the app spins down after periods of inactivity, so the first load may take 30-50 seconds.*

## Features

+ **User accounts** — Register, log in, and log out. Trigger entries are private to each user.
+ **Trigger logging** — Record a name, description, category, and optional coping strategy for each entry.
+ **Journal view** — Browse all of your triggers in a table, sorted by most recent first.
+ **Edit and delete** — Update entries as you learn more, or remove ones you no longer need.
+ **Categories** — Categorise triggers as Emotional, Environmental, Physical, Psychological, or Other.
+ **Home page** — Introductory guidance and a random motivational quote on each visit.

## Tech Stack

+ Django 5.2
+ PostgreSQL
+ Bootstrap 5
+ python-dotenv

## Setup

1. Clone the repo and create a virtual environment
2. `pip install -r requirements.txt`
3. Install PostgreSQL if you don't have it, and create a database + user:
4. Copy `.env.example` to `.env` and fill in your credentials
5. Generate a secret key with python -c "from django.core.management.utils import get_random_secret_key;
   print(get_random_secret_key())" and add it to your .env
6. `python manage.py collectstatic`
7. `python manage.py migrate`
8. `python manage.py makemigrations` 
9. `python manage.py runserver`

## Future Improvements
- Improve UI

## Disclaimer

This app is a personal journaling tool. It is not medical advice and is not a substitute for professional support. If you or someone you know is struggling with addiction, please reach out to a qualified healthcare provider or local support service.
