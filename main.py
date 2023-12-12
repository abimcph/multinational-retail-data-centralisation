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
    user_table_name = 'legacy_users'

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
        cleaned_user_data.to_csv('cleaned_user_data.csv', index=False)
        
    else:
        print(f"Table '{user_table_name}' not found in the database.")

    # Initialize data extractor and data cleaner
    data_extractor = DataExtractor()
    data_cleaner = DataCleaning()

    # Path or URL to the PDF document
    pdf_path = 'card_details.pdf'  # Update this path as needed

    # Extract data from PDF
    pdf_data = data_extractor.retrieve_pdf_data(pdf_path)

    # Assuming pdf_data is a list of DataFrames, one for each page or table
    for df in pdf_data:
        # Clean the extracted data
        cleaned_data = data_cleaner.clean_card_data(df)

        # Handle the cleaned data (e.g., analysis, visualization, saving to file)
        print("Cleaned card data is ready for in-memory operations.")
        # Example: cleaned_data.to_csv('cleaned_card_data.csv', index=False)
    # Initialize data extractor and data cleaner

    data_extractor = DataExtractor()
    data_cleaner = DataCleaning()

    # API details
    api_key = "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"
    headers = {"x-api-key": api_key}
    number_stores_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
    store_details_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"

    # Retrieve the number of stores
    num_stores = data_extractor.list_number_of_stores(number_stores_endpoint, headers)

    # Retrieve store data
    store_data = data_extractor.retrieve_stores_data(store_details_endpoint, headers, num_stores)

    # Clean the store data
    cleaned_store_data = data_cleaner.clean_store_data(store_data)

    # Handle the cleaned data (e.g., analysis, visualization, saving to file)
    print("Cleaned store data is ready for in-memory operations.")
    # Example: cleaned_store_data.to_csv('cleaned_store_data.csv', index=False)

    # Initialize data extractor and data cleaner
    data_extractor = DataExtractor()
    data_cleaner = DataCleaning()

    # S3 URL for the products data
    s3_url = 's3://data-handling-public/products.csv'

    # Extract product data from S3
    product_data = data_extractor.extract_from_s3(s3_url)

    # Convert product weights
    product_data = data_cleaner.convert_product_weights(product_data)

    # Clean the product data
    cleaned_product_data = data_cleaner.clean_products_data(product_data)

    # Handle the cleaned data (e.g., analysis, visualization, saving to file)
    print("Cleaned product data is ready for in-memory operations.")
    # Example: cleaned_product_data.to_csv('cleaned_product_data.csv', index=False)
    
    # Initialize data extractor, data cleaner, and database connector
    data_extractor = DataExtractor()
    data_cleaner = DataCleaning()
    db_connector = DatabaseConnector()

    # List all tables in the database
    tables = db_connector.list_db_tables()
    print("Tables in the database:", tables)

    # Identify the table containing order information
    # Replace 'orders_table_name' with the actual name of the orders table
    orders_table_name = 'orders_table_name'  # Adjust this based on actual table name

    if orders_table_name in tables:
        # Extract orders data
        orders_data = data_extractor.read_rds_table(db_connector, orders_table_name)
        print("Extracted Orders Data:")
        print(orders_data.head())  # Print first few rows of the orders data

        # Clean the orders data
        cleaned_orders_data = data_cleaner.clean_orders_data(orders_data)
        print("Cleaned Orders Data:")
        print(cleaned_orders_data.head())  # Print first few rows of the cleaned data
    else:
        print(f"Table '{orders_table_name}' not found in the database.")

    # S3 URL for the date events data
    s3_url_date_events = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'

    # Extract date events data from S3
    date_events_data = data_extractor.extract_json_from_s3(s3_url_date_events)

    # Clean the date events data
    cleaned_date_events_data = data_cleaner.clean_date_events_data(date_events_data)

    # Handle the cleaned data (e.g., analysis, visualization, saving to file)
    print("Cleaned date events data is ready for in-memory operations.")
    # Example: cleaned_date_events_data.to_csv('cleaned_date_events_data.csv', index=False)

if __name__ == "__main__":
    main()