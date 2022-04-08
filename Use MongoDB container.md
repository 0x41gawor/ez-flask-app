# Use MongoDB container
Now lets forget about Docker Image we just created for our app and lets think about adding some database to our app.

First just pull the `mongo:latest` docker image.
We want to run it with some configuration. In order to do that we created mongo-compose.yml file.
Run it with `docker-compose -f .\mongo-compose.yml up` and you database server is ready.
If you go to http://localhost:27017 it listens.
Now
do the following staff:
1. Open Windows Terminal
2. `docker ps`
3. `docker exec -it <mongo_container_id> sh`
4. In container terminal run: `mongosh`
5. `use admin`
6. `db.auth("ejek", "ejek")`
7. `db.ez_flask_app_db.find()`
8. ```
    db.ez_flask_app_db.insertMany([
    {
        "id": 1,
        "name": "Lion",
        "type": "wild"
    },
    {
        "id": 2,
        "name": "Cow",
        "type": "domestic"
    },
    {
        "id": 3,
        "name": "Tiger",
        "type": "wild"
    },
    ]);
    ```
9. `db.ez_flask_app_db.find()`
10. DATABASE IS SET UP !!!

Now you can run your app (on the host)
```
python app.py
```
When it will work, you can try to deploy two containers talking to each other with `docker-compose.yml`
Later you can add some volumes.

