""" Archivo que maneja la conexion con la base de datos """

import os
import logging
from typing import Generator, List, TypedDict, Union

from contextlib import contextmanager

from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import LoggingConnection


class DBInitData(TypedDict):
    """
    `DBInitData` is a dictionary with keys `user`, `password`, `host`, `port`, and `database`, and
    values that are all strings except for `port`, which can be either a string or an integer
    """
    user: str
    password: str
    host: str
    port: Union[str, int]
    database: str


def get_db_info():
    """
    It takes a list of environment variables, splits them by semicolon, and returns a list of
    dictionaries with the values from the environment variables
    :return: A list of dictionaries.
    """
    users = [x.strip() for x in os.getenv("DB_USER", "").split(";")]
    passwords = [x.strip() for x in os.getenv("DB_PASSWORD", "").split(";")]
    hosts = [x.strip() for x in os.getenv("DB_HOST", "").split(";")]
    ports = [x.strip() for x in os.getenv("DB_PORT", "").split(";")]
    databases = [x.strip() for x in os.getenv("DB_DBNAME", "").split(";")]

    lenadbs = max(len(users), len(passwords), len(hosts), len(ports), len(databases))

    def safe_list_get(lst, idx, default = None):
        try:
            return lst[idx]
        except IndexError:
            return default

    available_dbs: List[DBInitData] = []
    for index in range(lenadbs):
        temp_dict = {
            "user": safe_list_get(users, index, ""),
            "password": safe_list_get(passwords, index, ""),
            "host": safe_list_get(hosts, index, ""),
            "port": safe_list_get(ports, index, ""),
            "database": safe_list_get(databases, index, ""),
        }
        available_dbs.append(temp_dict)

    return available_dbs

class Connection:
    """ It's a class that represents a connection to a database """
    def __init__(self) -> None:
        self.__available_dbs = get_db_info()

    def _connect(self, _db: int = 0) -> connection:
        try:
            _connection = connect(**self.__available_dbs[_db], connection_factory=LoggingConnection)
            _connection.initialize(logging.getLogger("db_logger"))
            return _connection
        except Exception as ext:
            raise Exception(
                f"No fue posible realizar una conexion (psycopg2 error): {ext}"
            ) from ext

    @contextmanager
    def _open_connection(self, _db: int = 0) -> Generator[connection, None, None]:
        try:
            _connection = connect(**self.__available_dbs[_db], connection_factory=LoggingConnection)
            _connection.initialize(logging.getLogger("db_logger"))
        except Exception as ext:
            raise Exception(
                f"No fue posible realizar una conexion (psycopg2 error): {ext}"
            ) from ext
        else:
            try:
                with _connection as conn:
                    yield conn
            finally:
                _connection.close()

    def _close_connection(self, _connection: connection):
        _connection.close()
