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
3. `docker exec -it <mongo_container_id> mongosh`
4. `use admin`
5. `db.auth("ejek", "ejek")`
6. `use ez_flask_app_db`
7. `db.animals.find()`
8. ```
    db.animals.insertMany([
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
9. `db.animals.find()`
10. DATABASE IS SET UP !!!

Now you can run your app (on the host)
```
python app.py
```

