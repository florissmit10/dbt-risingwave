from dataclasses import dataclass
import dbt.exceptions  # noqa
from dbt.adapters.postgres import PostgresCredentials, PostgresConnectionManager

from dbt.logger import GLOBAL_LOGGER as logger


@dataclass
class RisingWaveCredentials(PostgresCredentials):
    """
    Defines database specific credentials that get added to
    profiles.yml to connect to new adapter
    """

    @property
    def type(self):
        """Return name of adapter."""
        return "risingwave"

    def _connection_keys(self):
        """
        List of keys to display in the `dbt debug` output.
        """
        return ("host", "port", "username", "user", "database")


class RisingWaveConnectionManager(PostgresConnectionManager):
    TYPE = "risingwave"


    @classmethod
    def open(cls, connection):
        """
        Receives a connection object and a Credentials object
        and moves it to the "open" state.
        """

        connection = super().open(connection)
        return connection


    # disable transactional logic
    def add_begin_query(self, *args, **kwargs):
        pass

    def add_commit_query(self, *args, **kwargs):
        pass

    def begin(self):
        pass

    def commit(self):
        pass

    def clear_transaction(self):
        pass