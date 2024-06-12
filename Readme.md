# README.md

## Online Store Inventory and Supplier Management API
### Overview
This API is developed to manage the inventory and suppliers for an online store. The API provides functionalities to add, view, update, and delete items and suppliers, and to establish relationships between them.

### Features
- Inventory Management: Add, view, update, and delete inventory items.
- Supplier Management: Add, view, update, and delete suppliers.
- Inventory-Supplier Relationship: Link items to suppliers and vice versa.

### Technologies Used
- Django: Web framework used to build the API.
- Django REST Framework: For building the RESTful API.
- PostgreSQL: Database to store inventory and supplier information.
- Docker: Containerization of the application.
- Gunicorn: WSGI HTTP Server for running the application in production.



## How to Run the Project

1. Clone the repository.
2. Navigate to the project directory.

### Setup
Setting up the project is as simple as following these steps:

3. Create a `.env` file, using `.env.sample` as a guide.

4. Install Precommit with this command:

   ```bash
    pre-commit install
   ```

#### To run the project locally without docker

5. Create a virtual environment the Run the following command:

   ```bash
   just install
   python manage.py runserver
   ```
#### To run the project locally with docker

6. 
    ### Run
    ```bash
    just start_local
    ```
    ### Clean up
    ```bash
    just down_local
    ```

### Test
To run tests without Docker, run:

    python manage.py tests

While tests will run on docker builds, you can also run tests using these commands:

    docker-compose run --rm tests

### Pre-commit
It is recommended to run your code against the pipeline of linting tolls and formatters before committing your code. This can be done by running the following command:

```bash
just pre_commit
```

### API DOCS
The API Documentation is automatically built with Swagger and is located at:
- /api/docs/
- /api/docs/redoc/

### Contributing

Use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) to ensure that your commit messages are readable and easy to follow. Also use [commitlint](https://commitlint.js.org/#/) to enforce this convention. To ensure that your commit messages are valid, just make sure you run the previous **pre_commit** command before committing your code.



### Debugging Docker
5. To access the bash, Run `docker exec -it store_app bash`
6. To view the logs, Run `docker logs -f store_app`

### Production
5. To access the bash, Run `docker exec -t store_app bash`
6. To view the logs, Run `docker logs -f store_app`
