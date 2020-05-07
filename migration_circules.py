"""Migrate data cicles from CSV file."""

# Python
import csv

# App
from cride.circles.models import Circle


def importCircles(file):
    """Import cicles data from App."""
    with open(file, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            circle = Circle(**row)
            circle.save()
