import html
import os
import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path
from django.utils.crypto import get_random_string

settings.configure(
    DEBUG=(os.environ.get("DEBUG", "") == "1"),
    ALLOWED_HOSTS=["*"],  # Disable host header validation
    ROOT_URLCONF=__name__,  # Make this module the urlconf
    SECRET_KEY=get_random_string(50),
)


def index(request):
    name = request.GET.get("name", "World")
    response = HttpResponse(f"""
        <html>
          <head>
            <link rel="stylesheet" type="text/css" href="/styles.css">
          </head>
          <body>
            <h1>Hello, {html.escape(name)}!</h1>
          </body>
        </html>
    """)
    response["Link"] = "</styles.css>; as=style; rel=preload"
    return response


def styles(request):
    return HttpResponse(
        """
        body {
            background-color: salmon;
            font-family: sans-serif;
        }
        """,
        content_type="text/css",
    )


urlpatterns = [
    path("", index),
    path("styles.css", styles),
]

app = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
