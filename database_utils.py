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


# import pandas as pd
# from sqlalchemy import create_engine, inspect
# import yaml

# class DatabaseConnector:
#     def __init__(self, db_config=None):
#         self.creds = self.read_db_creds()
#         self.db_config = db_config

#     @staticmethod
#     def read_db_creds():
#         """
#         Read the credentials from the YAML file.

#         Returns:
#         - dict: Database credentials.
#         """
#         with open("db_creds.yaml", "r") as yaml_file:
#             return yaml.safe_load(yaml_file)

#     def init_db_engine(self):
#         """
#         Initialize and return an SQLAlchemy database engine.

#         Returns:
#         - sqlalchemy.engine.base.Engine: Database engine.
#         """
#         try:
#             creds = self.read_db_creds()
#             engine_str = f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
#             engine = create_engine(engine_str)
#             return engine
#         except Exception as e:
#             print(f"Error initializing database engine: {e}")
#             return None
        
#     def upload_to_db(self, data_frame, table_name):
#         """
#         Upload data to the specified table in the database.

#         Parameters:
#         - table_name (str): The name of the target table.
#         - data (pd.DataFrame): Data to be uploaded.
#         """
#         try:
#             engine = self.init_db_engine()
#             data_frame.to_sql(table_name, engine, if_exists='replace')
#         except Exception as e:
#             print(f"Error uploading data to {table_name}: {e}")

#     def list_db_tables(self):
#         """
#         List all tables in the database.

#         Returns:
#         - list: List of table names.
#         """
#         try:
#             engine = self.init_db_engine()
#             inspector = inspect(engine)
#             return inspector.get_table_names()
#         except Exception as e:
#             print(f"Error listing tables: {e}")
#             return []
