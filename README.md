# releases

Fetch the release dates of currently installed package and display them as a table, sorted by newest release first.

Useful for determining which of your direct or indirect dependencies might have broken your tests.

The script takes a bit of time since it fetches data from PYPI and does so in a deliberately serial manner.

## Usage

```
$ python3 -m venv releases.env
$ . releases.env/bin/activate
$ pip install -r requirements.txt
$ python releases.py
Package             Version    Release
------------------  ---------  -----------
requests            2.31.0     22 May 2023
platformdirs        3.5.1      11 May 2023
certifi             2023.5.7   07 May 2023
urllib3             2.0.2      03 May 2023
packaging           23.1       12 Apr 2023
black               23.3.0     29 Mar 2023
pathspec            0.11.1     15 Mar 2023
charset-normalizer  3.1.0      06 Mar 2023
mypy-extensions     1.0.0      04 Feb 2023
ciso8601            2.3.0      21 Dec 2022
pip                 22.3.1     05 Nov 2022
setuptools          65.5.0     14 Oct 2022
tabulate            0.9.0      06 Oct 2022
idna                3.4        14 Sep 2022
click               8.1.3      28 Apr 2022
``` 
