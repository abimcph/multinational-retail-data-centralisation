# EXAMPLE markdown tab 

write stuff here 

## title 2 

- hello
- -
-- hello
    - hello 
    -

-hello
- hello
    - hello

>This is a highlighted one

**This is bold**

*this is in italics*

'hello'

hi

 class DataCleaning:
#     @staticmethod
#     def clean_user_data(data_frame):
#         """
#         Clean user data by handling NULL values, date errors, incorrect types, etc.

#         Parameters:
#         - data_frame (pd.DataFrame): The DataFrame containing user data.

#         Returns:
#         - pd.DataFrame: The cleaned DataFrame.
#         """
#         # Clean the user data
#         # Placeholder: Add your cleaning logic here
#         cleaned_df = data_frame.dropna()  # Example: Remove rows with NULL values
#         return cleaned_df

#     @staticmethod
#     def clean_card_data(data_frame):
#         """
#         Clean card data by removing erroneous values, NULL values, and formatting errors.

#         Parameters:
#         - data_frame (pd.DataFrame): The DataFrame containing card details.

#         Returns:
#         - pd.DataFrame: The cleaned DataFrame.
#         """
#         # Clean the card data
#         # Placeholder: Add your cleaning logic here
#         cleaned_df = data_frame.dropna()  # Example: Remove rows with NULL values
#         return cleaned_df

#     @staticmethod
#     def clean_store_data(data_frame):
#         """
#         Clean store data retrieved from the API.

#         Parameters:
#         - data_frame (pd.DataFrame): The DataFrame containing store details.

#         Returns:
#         - pd.DataFrame: The cleaned DataFrame.
#         """
#         # Clean the store data
#         # Placeholder: Add your cleaning logic here
#         cleaned_df = data_frame.dropna()  # Example: Remove rows with NULL values
#         return cleaned_df

# import pandas as pd

# class DataCleaning:

#     """
#     This class contains methods to clean data from various sources.
#     """
#     @staticmethod
#     def clean_user_data(user_data):
#         """
#         Clean the user data by handling NULL values, correcting date errors,
#         fixing incorrectly typed values.

#         Parameters:
#         - user_data (pd.DataFrame): The input DataFrame containing user data.

#         Returns:
#         - pd.DataFrame: Cleaned user data.
#         """
#         df = DataExtractor().read_rds_table('legacy_users')#extract the legacy users table from data extractor class
#         df['date_of_birth'] = pd.to_datetime(df['date_of_birth'],  infer_datetime_format=True, errors='coerce')#inferes date time as many different forms
#         df['join_date'] = pd.to_datetime(df['join_date'], infer_datetime_format=True, errors='coerce')#inferes date time as many different forms
#         df.dropna(subset=['date_of_birth','join_date'], inplace=True)#removes rows that contain null values spcifically looking in columns date_of_birth and join_date
        
#         return df #cleaned data frame

#         # The line below has been removed, so no filtering based on a condition
#         # cleaned_data = cleaned_data[~(cleaned_data['condition_column'] == 'condition_value')]


        # # Method to clean the user data
        # cleaned_df = DataExtractor().read_rds_table('legacy_users')
        # cleaned_data = legacy_users.copy()

        # # Handling NULL values
        # cleaned_data = cleaned_data.dropna()

        # # Correcting date errors (assuming 'date_column' is the date column in the DataFrame)
        # cleaned_data['date_of_birth'] = pd.to_datetime(cleaned_data['date_of_birth'], errors='coerce')

        # # Fixing incorrectly typed values
        # # (assuming 'numeric_column' is a numeric column in the DataFrame)
        # # cleaned_data['numeric_column'] = pd.to_numeric(cleaned_data['numeric_column'], errors='coerce')

        # return cleaned_data
    
#     def __init__(self):
#         self.db_connector = DatabaseConnector()

#     # T3S6: Create a method called clean_user_data which will perform the cleaning of the user data
#     def clean_user_data(self, df):
#         print(f"Type of df: {type(df)}")
#         # Remove rows with NULL values
#         cleaned_df = df.dropna()

#         # Handle date errors 
#         try:
#             df['opening_date'] = pd.to_datetime(df['opening_date'], format='%Y-%m-%d')
#         except ValueError as e:
#             print(f"Error converting dates: {e}")
            
#         return df
    
#         self.db_connector.upload_to_db(cleaned_df, 'your_table_name')

# data_cleaner = DataCleaning()
# cleaned_df = data_cleaner.clean_user_data(df)


# import pandas as pd
# import requests
# import boto3
# import io
# from database_utils import DatabaseConnector

# # This calss will work as a utility class, in it will be methods that help extract data from different data sources. The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and an S3 bucket. 
# class DataExtractor:
#     @staticmethod
#     def extract_rds_data(table_name):
#         # Method to extract data from an AWS RDS database
#         engine = DatabaseConnector.init_db_engine()

#         # Use pandas to read data from the specified table
#         with engine.connect() as connection:
#             query = f"SELECT * FROM {table_name};"
#             data = pd.read_sql(query, connection)

#         return data

#     @staticmethod
#     def list_db_tables():
#         # Method to list all tables in the database
#         engine = DatabaseConnector.init_db_engine()

#         with engine.connect() as connection:
#             metadata = MetaData()
#             metadata.reflect(bind=connection)
#             table_names = metadata.tables.keys()

#         return table_names

#     @staticmethod
#     def read_rds_table(connector_instance, table_name):
#         # Method to extract the database table to a pandas DataFrame
#         tables = DataExtractor.list_db_tables()

#         if table_name not in tables:
#             raise ValueError(f"Table '{table_name}' not found in the database.")

#         data = connector_instance.extract_rds_data(table_name)
#         return data
#     def __init__(self):
#         pass

#     # T3S5: Create a method 'read_rds_table' which will extract the database table to a pandas DataFrame
#     def read_rds_table(self, db_connector, legacy_users):
#         engine = db_connector.init_db_engine()
#         query = f"SELECT * FROM {legacy_users}"
#         df = pd.read_sql(query, engine)
#         return df
        
    # def extract_from_csv(self, file_path):
    #     """
    #     Method to extract data from a CSV file.

    #     Args:
    #         file_path (str): Path to the CSV file.

    #     Returns:
    #         pd.DataFrame: Extracted data as a Pandas DataFrame.
    #     """
    #     try:
    #         df = pd.read_csv(file_path)
    #         return df
    #     except Exception as e:
    #         print(f"Error extracting data from CSV: {e}")
    #         return None
    
    # def extract_from_api(self, api_url):
    #     """
    #     Method to extract data from an API.

    #     Args:
    #         api_url (str): URL of the API.

    #     Returns:
    #         pd.DataFrame: Extracted data as a Pandas DataFrame.
    #     """
    #     try:
    #         response = requests.get(api_url)
    #         response.raise_for_status()  # Raise an error if the request was unsuccessful

    #         data = response.json()
    #         df = pd.DataFrame(data)
    #         return df
    #     except Exception as e:
    #         print(f"Error extracting data from API: {e}")
    #         return None
    
    # def extract_from_s3(self, bucket_name, file_key):
    #     """
    #     Method to extract data from an S3 bucket.

    #     Args:
    #         bucket_name (str): Name of the S3 bucket.
    #         file_key (str): Key (path) of the file within the bucket.

    #     Returns:
    #         pd.DataFrame: Extracted data as a Pandas DataFrame.
    #     """
    #     try:
    #         s3 = boto3.client('s3')
    #         response = s3.get_object(Bucket=bucket_name, Key=file_key)
    #         data = response['Body'].read().decode('utf-8')
    #         df = pd.read_csv(io.StringIO(data))
    #         return df
    #     except Exception as e:
    #         print(f"Error extracting data from S3: {e}")
    #         return None


# import pandas as pd
# from sqlalchemy import create_engine, inspect
# import yaml

# class DatabaseConnector:
#     def __init__(self):
#         pass

#     @staticmethod
#     def read_db_creds():
#         """
#         Read the credentials from the YAML file.

#         Returns:
#         - dict: Database credentials.
#         """
#         with open("db_creds.yaml", "r") as yaml_file:
#             creds = yaml.safe_load(yaml_file)
#         return creds

#     @staticmethod
#     def init_db_engine():
#         """
#         Initialize and return an SQLAlchemy database engine.

#         Returns:
#         - sqlalchemy.engine.base.Engine: Database engine.
#         """
#         creds = DatabaseConnector.read_db_creds()

#         # Modify the URL for PostgreSQL
#         db_url = f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
#         engine = create_engine(db_url)

#         return engine

#     def list_db_tables(self):
#         """
#         List all tables in the database.

#         Returns:
#         - list: List of table names.
#         """
#         engine = self.init_db_engine()

#         with engine.connect() as connection:
#             table_names = connection.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'").fetchall()

#         return [table[0] for table in table_names]

#     def upload_to_db(self, clean_dataframe, table_name):
#         """
#         Upload data to the specified table in the database.

#         Parameters:
#         - table_name (str): The name of the target table.
#         - data (pd.DataFrame): Data to be uploaded.
#         """
#         db_to_sql = clean_dataframe.to_sql(table_name, self.engine, if_exists='replace', index=False)
#         return db_to_sql
        
        # engine = self.init_db_engine()

        # with engine.connect() as connection:
        #     # Ensure 'if_exists' is set to 'append' to add data to an existing table
        #     data.to_sql(table_name, connection, index=False, if_exists='replace', index=False)



# # import psycopg2
# # from sqlalchemy import create_engine, MetaData
# # import yaml

# # class DatabaseConnector:
# #     def __init__(self):
# #         pass

# #     @staticmethod
# #     def read_db_creds():
# #         """
# #         Read the credentials from the YAML file.

# #         Returns:
# #         - dict: Database credentials.
# #         """
# #         with open("db_creds.yaml", "r") as yaml_file:
# #             creds = yaml.safe_load(yaml_file)
# #         return creds

# #     @staticmethod
# #     def init_db_engine():
# #         """
# #         Initialize and return an SQLAlchemy database engine.

# #         Returns:
# #         - sqlalchemy.engine.base.Engine: Database engine.
# #         """
# #         creds = DatabaseConnector.read_db_creds()

# #         db_url = f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
# #         engine = create_engine(db_url)

# #         return engine

# #     def list_db_tables(self):
# #         """
# #         List all tables in the database.

# #         Returns:
# #         - list: List of table names.
# #         """
# #         engine = self.init_db_engine()

# #         with engine.connect() as connection:
# #             metadata = MetaData()
# #             metadata.reflect(bind=connection)
# #             table_names = metadata.tables.keys()

# #         return list(table_names)

# #     def upload_to_db(self, table_name, data):
# #         """
# #         Upload data to the specified table in the database.

# #         Parameters:
# #         - table_name (str): The name of the target table.
# #         - data (pd.DataFrame): Data to be uploaded.
# #         """
# #         engine = self.init_db_engine()

# #         with engine.connect() as connection:
# #             data.to_sql(table_name, connection, index=False, if_exists='replace')
            
# # import yaml
# # from sqlalchemy import create_engine, MetaData
# # import pandas as pd
# # import psycopg2
# # import yaml

# # class DatabaseConnector:

# #     def __init__(self, creds_file_path='db_creds.yaml'):
# #         self.credentials = self.read_db_creds(creds_file_path)
# #         self.connection = None
# #         self.cursor = None

# #     def read_db_creds(self, creds_file_path):
# #         # Method to read database credentials from a YAML file and return a dictionary
# #         try:
# #             with open(creds_file_path, 'r') as file:
# #                 creds = yaml.safe_load(file)
# #             return creds
# #         except Exception as e:
# #             print(f"Error: Unable to read database credentials.\n{str(e)}")
# #             return {}

# #     def connect(self):
# #         # Method to establish a connection to the RDS database
# #         try:
# #             self.connection = psycopg2.connect(**self.credentials)
# #             self.cursor = self.connection.cursor()
# #             print("Connected to the RDS database.")
# #         except Exception as e:
# #             print(f"Error: Unable to connect to the RDS database.\n{str(e)}")

# #     def close_connection(self):
# #         # Method to close the RDS database connection
# #         if self.connection:
# #             self.connection.close()
# #             print("Connection to the RDS database closed.")


# #     def init_db_engine(self):
# #         # Method to initialize and return an SQLAlchemy database engine
# #         try:
# #             engine = create_engine(
# #                 f"postgresql+psycopg2://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['host']}:{self.credentials['port']}/{self.credentials['dbname']}",
# #                  echo=True  # Set to False for production
# #             )
# #             print("Database engine initialized.")
# #             return engine
# #         except Exception as e:
# #             print(f"Error: Unable to initialize the database engine.\n{str(e)}")
# #             return None
    
# #     @staticmethod
# #     def list_db_tables():
# #         # Method to list all tables in the database
# #         engine = DatabaseConnector.init_db_engine()

# #         with engine.connect() as connection:
# #             metadata = MetaData()
# #             metadata.reflect(bind=connection)
# #             table_names = metadata.tables.keys()

# #         return table_names

# #     @staticmethod
# #     def upload_to_db(table_name, data):
# #         # Method to upload a Pandas DataFrame to the specified table in the database
# #         engine = DatabaseConnector.init_db_engine()

# #         with engine.connect() as connection:
# #             data.to_sql(table_name, connection, index=False, if_exists='replace')
    
# # #     def __init__(self, creds_file_path='db_creds.yaml'):
# # #         self.credentials = self.read_db_creds(creds_file_path)
# # #         self.connection = None
# # #         self.cursor = None

# # #     def read_db_creds(self, creds_file_path):
# # #         # Method to read database credentials from a YAML file and return a dictionary
# # #         try:
# # #             with open(creds_file_path, 'r') as file:
# # #                 creds = yaml.safe_load(file)
# # #             return creds
# # #         except Exception as e:
# # #             print(f"Error: Unable to read database credentials.\n{str(e)}")
# # #             return {}

# # #     def connect(self):
# # #         # Method to establish a connection to the RDS database
# # #         try:
# # #             self.connection = psycopg2.connect(**self.credentials)
# # #             self.cursor = self.connection.cursor()
# # #             print("Connected to the RDS database.")
# # #         except Exception as e:
# # #             print(f"Error: Unable to connect to the RDS database.\n{str(e)}")

# # #     def close_connection(self):
# # #         # Method to close the RDS database connection
# # #         if self.connection:
# # #             self.connection.close()
# # #             print("Connection to the RDS database closed.")


# # #     def init_db_engine(self):
# # #         # Method to initialize and return an SQLAlchemy database engine
# # #         try:
# # #             engine = create_engine(
# # #                 f"postgresql+psycopg2://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['host']}:{self.credentials['port']}/{self.credentials['dbname']}",
# # #                  echo=True  # Set to False for production
# # #             )
# # #             print("Database engine initialized.")
# # #             return engine
# # #         except Exception as e:
# # #             print(f"Error: Unable to initialize the database engine.\n{str(e)}")
# # #             return None
        
# # #     def list_db_tables(self, engine):
# # #         # Method to list all tables in the database
# # #         try:
# # #             inspector = inspect(engine)
# # #             table_names = inspector.get_table_names()
# # #             print("Tables in the database:")
# # #             for table_name in table_names:
# # #                 print(table_name)
# # #             return table_names
# # #         except Exception as e:
# # # #             print(f"Error: Unable to list tables in the database.\n{str(e)}")
# # # #             return []

# # # class DatabaseConnector:

# # #     def __init__(self, creds_file_path='db_creds.yaml'):
# # #         self.credentials = self.read_db_creds(creds_file_path)
# # #         self.connection = None
# # #         self.cursor = None
# # #         self.engine = self.init_db_engine()
# # #         pass
    
# # #     # T3S2: Create a method 'read_db_creds'
# # #     def read_db_creds(self, creds_file_path):
# # #         try:
# # #             with open(creds_file_path, 'r') as file:
# # #                 creds = yaml.safe_load(file)
# # #                 return {
# # #                     'dbname': creds['RDS_DATABASE'],
# # #                     'user': creds['RDS_USER'],
# # #                     'password': creds['RDS_PASSWORD'],
# # #                     'host': creds['RDS_HOST'],
# # #                     'port': creds['RDS_PORT']
# # #                 }
# # #         except Exception as e:
# # #             print(f"Error: Unable to read database credentials.\n{str(e)}")
# # #             return {}

# # #     # T3S3: Create a method 'init_db_engine' that will read the credentials from the return of read_db_creds and initialise and return an sqlalchemy database engine.
# # #     def init_db_engine(self):
# # #         try:
# # #             engine = create_engine(
# # #                 f"postgresql+psycopg2://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['host']}:{self.credentials['port']}/{self.credentials['dbname']}",
# # #                 echo=True  # Set to False for production
# # #             )
# # #             print("Database engine initialized.")
# # #             return engine
# # #         except Exception as e:
# # #             print(f"Error: Unable to initialize the database engine.\n{str(e)}")
# # #             return None
    
# # #     # T3S5: Create a method 'list_db_tables' to list all the tables in the database to know which tables to extract from. 
# # #     def list_db_tables(self):
# # #         try:
# # #             inspector = inspect(self.engine)
# # #             return inspector.get_table_names()
# # #         except Exception as e:
# # #             print(f"Error: Unable to list tables in the database.\n{str(e)}")
# # #             return []
    
# # #     # T3S7: Create a method to 'upload_to_db' This method will take in a Pandas DataFrame and table name to upload to as an argument
# # #     def upload_to_db(self, df, legacy_users):
# # #         try:
# # #             df.to_sql(table_name, self.engine, if_exists='replace', index=False)
# # #             print(f"Data uploaded to table '{table_name}'.")
# # #         except Exception as e:
# # #             print(f"Error: Unable to upload data to the database.\n{str(e)}")

        
# # #     # def connect(self):
# # #     #     try:
# # #     #         self.connection = psycopg2.connect(
# # #     #             database=self.database_name,
# # #     #             user=self.user,
# # #     #             password=self.password,
# # #     #             host=self.host,
# # #     #             port=self.port
# # #     #         )
# # #     #         print("Connected to database successfully")
# # #     #     except Exception as e:
# # #     #         print(f"Error connecting to database: {e}")
    
# # #     # def upload_data(self, data, table_name):
# # #     #     # Method to upload data to the database
# # #     #     pass
    
# # #     # def disconnect(self):
# # #     #     if self.connection:
# # #     #         self.connection.close()
# # #     #         print("Disconnected from database")
# # #     #     else:
# # #     #         print("No active database connection")

# # #         # def __init__(self):
# # #     #     pass


# from database_utils import DatabaseConnector
# from data_extraction import DataExtractor
# from data_cleaning import DataCleaning

# def main():
#     db_connector = DatabaseConnector()

#     # Extract User Data
#     user_data = DataExtractor.read_rds_table(db_connector, 'legacy_users')

#     # Clean User Data
#     cleaned_user_data = DataCleaning.clean_user_data(user_data)

#     # Upload Cleaned Data
#     db_connector.upload_to_db(cleaned_user_data, 'dim_users')

# if __name__ == "__main__":
#     main()


# # from data_extraction import DataExtractor
# # from data_cleaning import DataCleaning
# # from database_utils import DatabaseConnector

# # # Step 5: Read data from RDS database
# # db_connector = DatabaseConnector()
# # data_extractor = DataExtractor()
# # table_name = db_connector.list_db_tables()[0]  # Assuming the first table contains user data
# # user_data = data_extractor.read_rds_table(db_connector, table_name)
# # print(user_data)
# # print(user_data.columns)

# # # Step 6: Clean the user data
# # data_cleaner = DataCleaning()
# # cleaned_user_data = data_cleaner.clean_user_data(table_name)

# # # Step 8: Upload cleaned data to the database
# # table_to_upload = 'legacy_users'
# # db_connector.upload_to_db(cleaned_user_data, table_name)


#     # try:
#     #     table_names = db_connector.list_db_tables()
#     #     print("Tables in the database:")
#     #     for table in table_names:
#     #         print(f"- {table}")

#     #     # Prompt user to enter the correct user table name
#     #     user_table_name = input("\nEnter the name of the user table: ")

#     #     user_data = DataExtractor.read_rds_table(db_connector, user_table_name)

#     #     # Print columns of the user table
#     #     print(f"\nColumns of the {user_table_name} table:")
#     #     print(user_data.columns)

#     #     # Clean the user data
#     #     cleaned_user_data = DataCleaning.clean_user_data(user_data)

#     #     # Specify the target table name
#     #     target_table_name = 'dim_users'

#     #     # Upload the cleaned user data to the sales_data database in the dim_users table
#     #     db_connector.upload_to_db(target_table_name, cleaned_user_data)
        
#     #     print(f"\nData successfully uploaded to the {target_table_name} table.")
#     #         except Exception as e:
#     #          print(f"Error: {e}")