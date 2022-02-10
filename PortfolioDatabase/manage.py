#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PortfolioDatabase.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# Create a Django Project With an App Called PortfolioDatabase
    # Minimum Requirements
        # Views
            # Minimum of 4 views (Home, Hobbies, Portfolio, Contact)
            # Home - Have a welcome message, general summary about yourself
            # Hobbies - Display your hobbies names and descriptions from the database
            # Portfolio - Display your portfolio names and descriptions from the database (portfolio is a group of projects you have done)
            # Contact - Display student email
            # Attach Views to URLs
        # Database
            # Minimum of 2 models (hobby, portfolio)
                # The database needs to store names and descriptions of your hobbies and portfolio items
                # Minimum of 5 portfolio items (name & description)
                # Minimum of 3 hobbies (name & description)