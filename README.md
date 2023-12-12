# Multinational Retail Data Centralisation

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

This project focuses on extracting, cleaning, and analyzing data from various sources including AWS RDS databases, PDF documents, S3 buckets, and JSON files. The primary aim is to demonstrate the capability to handle diverse data sources, perform necessary data transformations, and prepare the data for analytical purposes. Key learnings from this project include data extraction techniques using Python, data cleaning and preprocessing, working with different data formats, and understanding the basics of data warehousing concepts. The project simulates a real-world scenario where data from various sources is aggregated and processed for business intelligence purposes.

## Installation

To install the necessary dependencies for this project, run the following commands:

```bash
pip install pandas
pip install sqlalchemy
pip install boto3
pip install tabula-py

## Usage

To use this project, follow these steps:

- Clone the repository to your local machine.
- Navigate to the project directory in your terminal or command prompt.
- Execute the main.py script: python main.py.

Make sure to update the database credentials and paths to S3 buckets or PDF files as per your setup.

## File Structure

data_extraction.py: Contains methods to extract data from RDS databases, PDF files, and S3 buckets.
data_cleaning.py: Defines methods for cleaning the extracted data, including handling missing values and standardizing formats.
database_utils.py: Manages database connections and interactions with AWS RDS.
main.py: Orchestrates the overall data extraction, cleaning, and analysis process.

