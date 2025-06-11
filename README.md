## Database (with sqlalchemy)

-   Install the two packges `pipenv install flask-sqlalchemy flask-migrate`
-   How to get the possible commands `flask db --help`
-   Init migrations with `flask db init` -- run only once
-   Create/autogenerate migration files with `flask db migrate -m ""`
-   Apply our migration with `flask db upgrade`
