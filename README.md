# Stock Analysis Project

This project analyzes stock data using the Simple Moving Average (SMA) crossover strategy to generate buy and sell signals. The project is built using Python, PostgreSQL, and Pandas.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup and Configuration](#setup-and-configuration)
- [Running the Project](#running-the-project)
- [Testing](#testing)

## Features

- Stores stock data in a PostgreSQL database.
- Analyzes stock data using the SMA crossover strategy.
- Generates buy and sell signals based on the analysis.
- Unit tests to validate data types and strategy logic.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [pip (Python package installer)](https://pip.pypa.io/en/stable/installation/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Shivansh-Ahirwal/stock_analysis_project.git
    cd stock_analysis_project
    ```

2. Install Python dependencies:

    ```bash
    pip install -r src/requirements.txt
    ```

## Setup and Configuration

### 1. **PostgreSQL Setup**

- **Install PostgreSQL**: If not already installed, download and install PostgreSQL from the [official website](https://www.postgresql.org/download/).
- **Create a New Database**: Use `pgAdmin` or the PostgreSQL command line tool to create a new database named `stock_db`.

### 2. **Configure Database Connection**

- In the `src` directory, Update the `db_config.py` file with the following content:

    ```plaintext
    DB_NAME=stock_db
    DB_USER=yourusername
    DB_PASSWORD=yourpassword
    DB_HOST=localhost
    DB_PORT=5432
    ```

- Replace `yourusername` and `yourpassword` with your PostgreSQL credentials.

## Running the Project

1. **Create Database Tables And Insert Stock Data**: 

   Run the `insert_data.py` script to insert stock data into the database:

    ```bash
    python insert_data.py
    ```

2. **Analyze Stock Data**: 

   Execute the `analyze_data.py` script to analyze the stock data using the SMA crossover strategy:

    ```bash
    python analyze_data.py
    ```

   The script will output buy and sell signals based on the analysis.
3. **Output**:

   ![image](https://github.com/user-attachments/assets/1babfe2d-fcd8-4e1d-9cc3-254d3cc3e79c)
## Testing

To run the unit tests for data validation and strategy logic, use the following command:

```bash
python -m unittest discover tests/
```
