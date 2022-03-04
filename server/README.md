# Server

Backend server for mands app.

## Usage

Install
```sh
python3 -m venv env/
pip3 install --user -r requirements.txt
```

Test
```sh
bash scripts/test.sh
```

Run
```sh
bash scripts/run.sh
```

When running api docs are under
```sh
http://<HOST>:<PORT>/docs
```

## Tooling outside requirements.

- **dbdiagram.io** to develop the database schema.
- **Docker PostgreSQL image**
- **golang-migrate** for database migrations.
- **TablePlus** to interact with Postgres and develop queries.