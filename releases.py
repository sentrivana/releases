from datetime import date
from importlib import metadata
from time import sleep

import requests
from ciso8601 import parse_datetime
from tabulate import tabulate


PYPI_URL = "https://pypi.python.org/pypi/{project}/{version}/json"

projects = []

for package in metadata.distributions():
    project = package.metadata["Name"]
    version = package.metadata["Version"]
    url = PYPI_URL.format(project=project, version=version)

    pypi_data = requests.get(url)
    if pypi_data.status_code != 200:
        # XXX
        continue

    release_date = parse_datetime(pypi_data.json()["urls"][0]["upload_time_iso_8601"])

    projects.append((project, version, release_date))

    sleep(0.5)


projects.sort(key=lambda p: p[2], reverse=True)
projects = [(p[0], p[1], p[2].strftime("%d %b %Y")) for p in projects]

print(tabulate(projects, headers=["Package", "Version", "Release"]))
