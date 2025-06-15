# Bank Management System

A simple console-based Bank Management System implemented in Python using SQLite database.

## Features

- Create new bank accounts
- Deposit money
- Withdraw money
- Check account balance
- View customer details
- Delete accounts
- View all accounts
- Admin login system

## Requirements

- Python 3.x
- SQLite3

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/bank-management-system.git
```

2. Navigate to the project directory
```bash
cd bank-management-system
```

3. Run the main program
```bash
python main.py
```

## Usage

1. When you run the program, you'll be presented with a login screen
2. Default admin credentials:
   - Username: admin
   - Password: admin123

3. After logging in, you can:
   - Create new accounts
   - Perform transactions
   - View account details
   - Delete accounts
   - View all customer records

## Database Structure

The program uses SQLite database with two tables:
- `admin_table`: Stores admin login credentials
- `bank_table`: Stores customer account information

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License