import pytest
from pymongo import MongoClient
from src.Part_1 import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

@pytest.fixture(scope='module')
def connection():
    conn = MongoClient(MONGO_URI)
    yield conn
    conn.close()

@pytest.fixture
def database_conn(connection):
    database = connection[f"{DATABASE_NAME}"]
    yield database

@pytest.fixture
def collection(database_conn):
    collection = database_conn[f"{COLLECTION_NAME}"]
    yield collection
