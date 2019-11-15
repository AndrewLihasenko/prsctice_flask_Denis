import os

PG_USER = os.environ.get('PG_USER', 'practice')
PG_PASSWORD = os.environ.get('PG_PASSWORD', '123')
PG_HOST = os.environ.get('PG_HOST', 'localhost')
PG_PORT = os.environ.get('PG_PORT', 5432)
DB_NAME = os.environ.get('DB_NAME', 'practice')