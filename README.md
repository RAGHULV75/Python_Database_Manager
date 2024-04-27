# Python_Database_Manager
using Python and Sqlite3

I'd be glad to create a GitHub README for the provided SQLite customer management code:

**Customer Management System**

This Python script implements a simple customer management system using a SQLite database. It allows users to create a customer table (if it doesn't exist), add customer data, sort customers by ID, search for customers by city or name, remove customers, and list all customers.

**Features:**

* **SQLite Database Integration:** Leverages SQLite for data persistence.
* **User Input and Interaction:** Provides a menu-driven interface for user interaction.
* **CRUD Operations:** Supports Create, Read, Update (indirectly through deletion and re-addition), and Delete functionalities.
* **Data Sorting and Searching:** Enables sorting customers by ID (descending) and searching by city or name.

**Getting Started**

1. **Install Dependencies:** You'll need the `sqlite3` module installed in your Python environment. Use `pip install sqlite3` if it's not already available.
2. **Run the Script:** Save the code as a Python file (e.g., `customer_manager.py`) and execute it from the command line using `python customer_manager.py`.

**Usage**

The script presents a menu with the following options:

1. **Create Customer Table (if it doesn't exist):** Creates the `shop` table with columns for `customer_id` (integer, primary key), `customer_name` (text, not null), `city` (text, not null), and `phone_number` (integer, unique).
2. **Add Customers:** Prompts the user to enter multiple customer records in the format `(id, name, city, phone_number)`. These are then inserted into the database.
3. **List Customers by ID (highest first):** Retrieves and displays all customers sorted by their ID in descending order (highest ID first).
4. **Find Customers by City:** Asks for a city name and displays customer names residing in that city.
5. **Find Customer Information:** Requests a customer name and shows the information for that specific customer.
6. **Remove Customer:** Prompts for a customer name and deletes the corresponding customer record from the database.
7. **List All Customers:** Retrieves and displays all customer data from the database.
8. **Exit:** Closes the connection to the database and terminates the program.

**Example Usage:**

```
Customer Management System

1. Create Customer Table (if it doesn't exist)
2. Add Customers
3. List Customers by ID (highest first)
4. Find Customers by City
5. Find Customer Information
6. Remove Customer
7. List All Customers
8. Exit

Enter your choice: 1
Customer table created successfully (if it didn't already exist).

... (continue using the menu options) ...

Bye have a Good Day
```

**Improvements**

* **Error Handling:** Consider adding error handling for invalid user input, database connection errors, etc.
* **Data Validation:** Implement data validation to ensure correct data formats (e.g., integer IDs, unique phone numbers).
* **Modularization:** Refactor the code into well-defined functions for better organization and reusability.
* **Database Schema Enhancements:** Explore additional columns (e.g., email address) or data types (e.g., date for registration) based on specific needs.
* **Security:** For production use, consider security measures to protect sensitive customer data.

**License**

This code is provided under the MIT license. Feel free to use, modify, and distribute it as needed, with attribution to the original author.
