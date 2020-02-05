django-server-push-demo
=======================

A repository demonstrating how to use HTTP/2 server push with Django, using the
"Link" header and nginx.

Run:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py runserver
```

In another terminal, start nginx:

```
yes ok | openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
nginx -c $PWD/nginx.conf
```

Then visit https://localhost/ in local browser, ignoring the self-signed
certificate warning.
