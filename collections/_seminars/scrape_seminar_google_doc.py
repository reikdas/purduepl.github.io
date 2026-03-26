#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "gspread",
#     "python-dateutil",
# ]
# ///
import argparse
import json
import os

import gspread
from dateutil.parser import parse

print(
    "Warning, don't run a script from the internet that you haven't read before... certainly don't give it write permissions - Patrick, August 22, 2023"
)

parser = argparse.ArgumentParser(description="Scrape seminar data from a Google Sheet")
parser.add_argument("url", help="URL of the Google Sheet")
args = parser.parse_args()

gc = gspread.service_account()
sh = gc.open_by_url(args.url)
print(sh.title)
print(sh.sheet1)

records = sh.sheet1.get_all_records()

print("Asserting some kind of format")
for record in records:
    assert "Date" in record.keys()
    assert "Presenter" in record.keys()
    assert "Title" in record.keys()
    assert "Location" in record.keys()


def date_filter(x):
    try:
        parse(x["Date"])
        return True
    except ValueError:
        print("Date filtered out:\n", json.dumps(x, indent=2))
        return False


def presenter_filter(x):
    result = x["Presenter"] != "" and x["Presenter"] != "N/A"
    if not result:
        print("Presenter filtered out:\n", json.dumps(x, indent=2))
    return result


def spring_break_filter(x):
    result = x["Location"] != "Bahamas" and x["Title"] != "Spring Break"
    if not result:
        print("Spring break filtered out:\n", json.dumps(x, indent=2))
    return result


print("The unfiltered list of records")
print(json.dumps(records, indent=2))

records = filter(date_filter, records)
records = filter(presenter_filter, records)
records = filter(spring_break_filter, records)

for record in list(records):
    date = parse(record["Date"])
    presenter = record["Presenter"].strip()
    title = record["Title"].strip()
    location = record["Location"].strip()

    year_dir = str(date.year)
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)

    file_name = f"{year_dir}/{date.year}-{date.month}-{date.day}-seminar.md"
    file_contents = f"""---
layout: post
speaker: "{presenter}"
title: "{title}"
time: 12p EST
location: "{location}"
category: seminar
invited: false
link_abstract: true
bio: "TBA"
---
TBA
"""
    print(file_name)
    print(file_contents)
    if not os.path.exists(file_name):
        with open(file_name, mode="w") as f:
            f.write(file_contents)
