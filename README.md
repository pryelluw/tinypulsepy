# tinypulsepy
Python client for tinypulse api


# dev setup

Client is Python 2 & 3 compatible

Create a new virtualenv `python3 -m venv .venv/`

Install the dependencies with `pip install -r requirements.txt`


# dev flow

Everything goes through the develop branch.

Master -> production.

Don't break backwards compatibility.



# Settings

reference: https://api-docs.tinypulse.com/doc/develop_get_auth_tokens

Source these from your administration dashboard.

`API_KEY = ''` **Required**

`ACCESS_TOKEN = ''` Optional