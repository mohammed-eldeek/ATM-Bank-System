# ATM-Bank System
Python ATM Bank System With MySQL - mariaDB.

## Database Setup

### Prerequisites

- Ensure you have MySQL installed on your system.

### Setting up the Database


1. Clone this repository to your local machine:
   ```bash
	git clone https://github.com/mohammed-eldeek/ATM-Bank-System.git
	```

2. Open a terminal and navigate to the project directory.
### Establishing Database Connection
3. Open the main.py file in your preferred code editor.

4. Locate the create_connection function within the code.
	-  Update the database connection parameters:
  ```python
def create_connection():
      connection = mysql.connector.connect(
          host="localhost", 
          user="your_username", ## root
          password="your_password", ## your MySQL Password
          database="ATM_SYSTEM", 
  ```
5. Replace your_username, your_password, and other parameters accordingly.

## Usage

- To run the main script that interacts with the database, follow these steps:
	1. Ensure you've set up the database as mentioned in the **Database Setup** section.
	2. Open a terminal and navigate to the project directory.
	3. Run the script using the following command:
   ```bash
   source venv/bin/activate
   python main.py
   ```
## Contributions

Contributions to this project are welcome! If you'd like to contribute, follow these steps:

1. Fork this repository to your GitHub account.
2. Clone the forked repository to your local machine.
   ```bash
   git clone https://github.com/mohammed-eldeek/ATM-Bank-System.git
	```

## License

This project is licensed under the [MIT] License - see the [MIT](LICENSE) file for details.
