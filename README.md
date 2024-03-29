# Say it

### Service to publish a webpage to display what you want to say 😜 

![Message view screenshot](images/message-view.png?raw=true "Message view screenshot")

### Local setup
  - Clone repository
  - Create ```.env``` file inside ```sayit/settings/``` with following variables
    ```
    SECRET_KEY='<random-django-secret-key>'
    ALLOWED_HOSTS=<allowed-hosts-seperated-by-spaces>

    HASHIDS_SALT='<random-characters-as-salt>'
    ```
  - Start development server as follows, site will be accessible at http://localhost:8000/
    ```
    python3 manage.py runserver --settings="sayit.settings.dev"
    ``` 

#### Credits
 - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website
 - https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

#### License
  MIT
