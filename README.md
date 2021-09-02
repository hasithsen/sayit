# Say it

### Service to publish a webpage to display what you want to say 😜 

![Message view screenshot](images/message-view.png?raw=true "Message view screenshot")

[Have your say!](https://sayit.hsen.tech "Webpage")

### Setup
  - Clone repository
  - Create ```.env``` file inside ```sayit/settings/``` with following variables
    ```
    SECRET_KEY='<random-django-secret-key>'
    ALLOWED_HOSTS=<allowed-hosts-seperated-by-spaces>

    HASHIDS_SALT='<random-characters-as-salt>'
    ```

#### Credits
 - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website
 - https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

#### License
  MIT
