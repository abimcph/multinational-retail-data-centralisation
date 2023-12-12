import yaml
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.reflection import Inspector
class DatabaseConnector:
    """Handles database connections and interactions."""

    def read_db_creds(self):
        """
        Reads database credentials from a YAML file.

        Returns:
        dict: Database credentials.
        """
        with open('db_creds.yaml', 'r') as file:
            return yaml.safe_load(file)

    def init_db_engine(self):
        """
        Initializes a SQLAlchemy database engine.

        Returns:
        sqlalchemy.Engine: A database engine.
        """
        creds = self.read_db_creds()
        return sqlalchemy.create_engine(
            f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        )

    def list_db_tables(self):
        """
        Lists all tables in the database.

        Returns:
        list: A list of table names.
        """
        engine = self.init_db_engine()
        inspector = Inspector.from_engine(engine)
        return inspector.get_table_names()

    def upload_to_db(self, df, table_name):
        """
        Uploads a DataFrame to a specified table in the database.

        Args:
        df (pandas.DataFrame): The DataFrame to upload.
        table_name (str): The name of the target table.
        """
        engine = self.init_db_engine()
        df.to_sql(table_name, engine, if_exists='replace', index=False)

