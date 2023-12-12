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

    # Assuming we know the table name containing user data
    user_table_name = 'legacy_users'  # Replace with actual table name

    # Check if the user table is in the list of tables
    if user_table_name in tables:
        # Extract data from the user table
        user_data = data_extractor.read_rds_table(db_connector, user_table_name)

        # Initialize the data cleaner
        data_cleaner = DataCleaning()

        # Clean the extracted user data
        cleaned_user_data = data_cleaner.clean_user_data(user_data)

        # Perform in-memory operations on cleaned_user_data here
        # For example, analysis, visualization, exporting to a file, etc.
        print("Cleaned user data is ready for in-memory operations.")
        # Example: cleaned_user_data.to_csv('cleaned_user_data.csv', index=False)
    else:
        print(f"Table '{user_table_name}' not found in the database.")

    # Initialize data extractor and data cleaner
    data_extractor = DataExtractor()
    data_cleaner = DataCleaning()

    # Path or URL to the PDF document
    pdf_path = '/Users/abimcph/Downloads/card_details.pdf'  # Update this path as needed

    # Extract data from PDF
    pdf_data = data_extractor.retrieve_pdf_data(pdf_path)

    # Assuming pdf_data is a list of DataFrames, one for each page or table
    for df in pdf_data:
        # Clean the extracted data
        cleaned_data = data_cleaner.clean_card_data(df)

        # Handle the cleaned data (e.g., analysis, visualization, saving to file)
        print("Cleaned card data is ready for in-memory operations.")
        # Example: cleaned_data.to_csv('cleaned_card_data.csv', index=False)

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

