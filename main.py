from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

def main():
    # Initialize the database connector
    db_connector = DatabaseConnector()

    # Initialize the data extractor
    data_extractor = DataExtractor()

    # Extract the list of tables from the database
    tables = db_connector.list_db_tables()
    print("Tables in the database:", tables)

    user_table_name = 'legacy_users' 

    # Check if the user table is in the list of tables
    if user_table_name in tables:
        # Extract data from the user table
        user_data = data_extractor.read_rds_table(db_connector, user_table_name)

        # Initialize the data cleaner
        data_cleaner = DataCleaning()

        # Clean the extracted user data
        cleaned_user_data = data_cleaner.clean_user_data(user_data)

        # Upload the cleaned data to a new table in the database
        cleaned_table_name = 'dim_users'
        db_connector.upload_to_db(cleaned_user_data, cleaned_table_name)
        print(f"Cleaned data uploaded to table '{cleaned_table_name}' in the database.")
    else:
        print(f"Table '{user_table_name}' not found in the database.")

if __name__ == "__main__":
    main()


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

