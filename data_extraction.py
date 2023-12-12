import pandas as pd
from database_utils import DatabaseConnector
import tabula
import requests
import boto3
import io
class DataExtractor:
    """Extracts data from various sources."""

    def read_rds_table(self, db_connector, table_name):
        """
        Reads a table from an RDS database into a pandas DataFrame.

        Args:
        db_connector (DatabaseConnector): Database connector instance.
        table_name (str): Name of the table to read.

        Returns:
        pandas.DataFrame: The extracted table data.
        """
        engine = db_connector.init_db_engine()
        return pd.read_sql_table(table_name, engine)

    def retrieve_pdf_data(self, pdf_url):
        """
        Extracts data from a PDF document and returns it as a pandas DataFrame.

        Args:
        pdf_url (str): URL or path to the PDF document.

        Returns:
        pandas.DataFrame: Data extracted from the PDF.
        """
        return tabula.read_pdf(pdf_url, pages='all', multiple_tables=True)
    
    def list_number_of_stores(self, endpoint, headers):
        """
        Retrieves the number of stores from the API.

        Args:
        endpoint (str): API endpoint to get the number of stores.
        headers (dict): Headers to include in the API request.

        Returns:
        int: Number of stores.
        """
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()['number_of_stores']
        else:
            raise Exception(f"API request failed with status code {response.status_code}")

    def retrieve_stores_data(self, endpoint, headers, num_stores):
        """
        Retrieves data for all stores from the API.

        Args:
        endpoint (str): API endpoint to retrieve store details.
        headers (dict): Headers to include in the API request.
        num_stores (int): Number of stores to retrieve.

        Returns:
        pandas.DataFrame: DataFrame containing details of all stores.
        """
        all_stores = []
        for store_number in range(1, num_stores + 1):
            store_endpoint = endpoint.format(store_number=store_number)
            response = requests.get(store_endpoint, headers=headers)
            if response.status_code == 200:
                all_stores.append(response.json())
            else:
                print(f"Failed to retrieve data for store number {store_number}")
        return pd.DataFrame(all_stores)

    def extract_from_s3(self, s3_url):
        """
        Extracts data from an S3 bucket and returns it as a pandas DataFrame.

        Args:
        s3_url (str): S3 URL of the file (e.g., 's3://bucket-name/file.csv').

        Returns:
        pandas.DataFrame: Data extracted from the S3 file.
        """
        # Parse bucket name and file path from s3_url
        bucket_name = s3_url.split('/')[2]
        file_path = '/'.join(s3_url.split('/')[3:])

        # Initialize S3 client
        s3_client = boto3.client('s3')

        # Get object from S3
        obj = s3_client.get_object(Bucket=bucket_name, Key=file_path)
        
        # Read data into DataFrame
        return pd.read_csv(io.BytesIO(obj['Body'].read()))
    
    def extract_json_from_s3(self, s3_url):
        bucket_name = s3_url.split('/')[2]
        file_path = '/'.join(s3_url.split('/')[3:])
        s3_client = boto3.client('s3')
        obj = s3_client.get_object(Bucket=bucket_name, Key=file_path)
        data = json.load(io.BytesIO(obj['Body'].read()))
        return pd.DataFrame(data)
# import pandas as pd
# from sqlalchemy import inspect
# import tabula
# import requests
# import yaml
# import boto3
# import time
# from io import BytesIO
# from database_utils import DatabaseConnector


# class DataExtractor:
#     def __init__(self):
#         self.db_connector = DatabaseConnector()
#         self.credentials = self.db_connector.read_source_db_creds()
#         self.source_engine = self.db_connector.init_source_db_engine(self.credentials)

#     def read_rds_table(db_connector, table_name):
#         """
#         Extract the database table to a pandas DataFrame.

#         Parameters:
#         - connector_instance: An instance of DatabaseConnector.
#         - table_name (str): The name of the table to extract.

#         Returns:
#         - pd.DataFrame: Extracted data.
#         """
#         try:
#             engine = db_connector.init_db_engine()
#             return pd.read_sql(f"SELECT * FROM {table_name}", engine)
#         except Exception as e:
#             print(f"Error reading table {table_name}: {e}")
#             return None

#     def extract_from_s3(self, s3_url):
#         bucket_name = "data-handling-public"
#         file_name = "products.csv"
#         s3 = boto3.client('s3')

#         # Download the CSV file from S3
#         s3.download_file(bucket_name, file_name, '/tmp/products.csv')
        
#         # Load the CSV file into a DataFrame and return
#         return pd.read_csv('/tmp/products.csv')
    
#     def retrieve_pdf_data(self, pdf_url):
#         response = requests.get(pdf_url)
#         if response.status_code == 200:
#             with open("temp.pdf", "wb") as f:
#                 f.write(response.content)
#             dfs = tabula.read_pdf("temp.pdf", pages="all", multiple_tables=True)
#             return pd.concat(dfs, ignore_index=True)
#         else:
#             print("Failed to download PDF")
#             return None
        
#     def retrieve_stores_data(self):
#         num_stores = []
#         try:
#             store_number = self.list_number_of_stores()
#         except Exception as e:
#             print(f"Error getting store number: {e}")
#             return None

#         for i in range(1, store_number + 1):
#             api_url_base = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{i}'
#             response = requests.get(api_url_base, headers=self.header)
            
#             if response.status_code != 200:
#                 print(f"Failed to get data for store {i}")
#                 continue
            
#             num_stores.append(pd.json_normalize(response.json()))
            
#         return pd.concat(num_stores)
