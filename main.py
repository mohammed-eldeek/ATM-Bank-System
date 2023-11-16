from getpass import getpass
from  os import  system
import mysql.connector
from cardHolder import CardHolder
def load_DB():
    condb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="moonknight",
    )
    condb.cursor().execute("CREATE DATABASE IF NOT EXISTS ATM_SYSTEM")
    condb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="moonknight",
        database="ATM_SYSTEM"
    )

    try:
        mycursor = condb.cursor()
        mycursor.execute("select *from cardholders;")
        if (mycursor.arraysize):
            print("")
    except:
        print("Adding Database To Your System.\nPlease wait...")
        with open('database/db/data.sql', 'r') as file:
            queries = file.read()

        cursor = condb.cursor()
        cursor.execute(queries)
def create_connection():
    """Create a database connection."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="moonknight",
        database="ATM_SYSTEM",
        sql_mode="TRADITIONAL",
        allow_local_infile=True,
        autocommit=True,

    )
    if connection.is_connected():
        print(f"Welcome, To Egyptian Bank..")
    return connection




def fetch_cardholders(connection):
    cardholders = []
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cardholders")
    rows = cursor.fetchall()
    for row in rows:
        cardholder = CardHolder(str(row[1]).strip(), row[2], row[3], row[4], row[5])
        cardholders.append(cardholder)
    return cardholders

def print_menu():
    # Options
    print("Please choose an option: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Profile")
    print("5. Exit")

def deposit(cardHolder, connection,max=20000):
    print(f"Your Current Balance is $ { cardHolder.get_balance():,.2f}")

    try:
        deposit_amount = float(input("How much $ do you want to deposit? "))
        current_balance = cardHolder.get_balance()
        if deposit_amount >= max :
            print("Sorry, You cannot deposit more than $ 20000 per day.")
            print(f"current balance: {current_balance:,.2f}")
        else:
            new_balance = float(current_balance) + deposit_amount
            cardHolder.set_balance(new_balance)
            print(f"Successfully Deposit,Your Current Balance Is $: {new_balance:,.2f}")

            # Commit the changes to the database
            update_balance_query = "UPDATE cardholders SET balance = %s WHERE card_num = %s"
            cursor = connection.cursor()
            cursor.execute(update_balance_query, (new_balance, cardHolder.get_card_num()))
            connection.commit()
            cursor.close()
    except ValueError:
        print("Invalid input")

def withdraw(cardHolder, connection):
    print(f"Your Current Balance is $ { cardHolder.get_balance():,.2f}")
    try:
        withdraw = float(input("How much $ do you want to withdraw? "))
        if withdraw > cardHolder.get_balance():
            print("Insufficient Balance..")
        else:
            current_balance = cardHolder.get_balance()
            new_balance = float(current_balance) - withdraw
            cardHolder.set_balance(new_balance)
            print("Current balance is $", f"{new_balance:,.2f}")
            print("Successfully Withdraw","Thank you :)")
            # Commit the changes to the database
            update_balance_query = "UPDATE cardholders SET balance = %s WHERE card_num = %s"
            cursor = connection.cursor()
            cursor.execute(update_balance_query, (new_balance, cardHolder.get_card_num()))
            connection.commit()
            cursor.close()
    except ValueError:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your Current Balance is",f"${cardHolder.get_balance():,.2f} ")
def show_profile(cardHolder,connection):
    cardHolder.print_output()
    edit_profile(current_user,connection)

def edit_profile(cardHolder,connection):

    # Options
    while True:
        print("\n1. Change PIN")
        print("2. Back")
        option = int(input())
        if option == 2 :
            break
        elif option == 1:
            confirm_PIN = int(getpass("Enter your Current PIN: "))
            current_PIN = cardHolder.get_pin()
            if confirm_PIN == current_PIN:
                new_pin = int(getpass("Enter your new PIN: "))
                cardHolder.set_pin(new_pin)
                update_pin = cardHolder.get_pin()
                # Commit the changes to the database
                update_pin_query = "UPDATE cardholders SET pin = %s WHERE card_num = %s"
                cursor = connection.cursor()
                cursor.execute(update_pin_query, (update_pin, cardHolder.get_card_num()))
                connection.commit()
                print("New PIN Has Been Updated Successfully!")
                cursor.close()
            else:
                print("Invalid input")
        else:
            print("Invalid input")
if __name__ == "__main__":
    load_DB()
    connection = create_connection()

    if connection:
        # play sound
        file = "assets/audio/air.mp3"
        system("mpg123 " + file + " > /dev/null 2>&1")
        # Fetch cardholders from the database
        list_of_card = fetch_cardholders(connection)

    debit_card_number = ""
    while True:
        try:
            debit_card_number = input("Please enter your debit card: ").strip()
            debit_match = [holder for holder in list_of_card if str(holder.get_card_num()) == debit_card_number]
            if len(debit_match) > 0:
                current_user = debit_match[0]
                break
            else:
                print("Card number not recognized. Try again.")
        except ValueError:
            print("Card number not recognized. Try again.")

    # PIN
    tries = 4
    while tries > 0:
        try:
            user_pin = int(getpass("Please enter your PIN number: ").strip())
            if current_user.get_pin() == user_pin:
                break
            else:
                print("Invalid PIN, Try again.")
                tries -=1
                print( "Last Chance" if tries == 1 else f"Available Tries: {tries}")

        except ValueError:
            print("Invalid PIN, Try again.")
            tries -=1
            print(f"Available Tries: {tries}")

    if current_user.get_pin() == user_pin:
        # Print Options
        print("Welcome ", current_user.get_fname(), ":)")
        option = 0
        while True:
            print_menu()
            try:
                option = int(input())
            except ValueError:
                print("Invalid input! ")

            if option == 1:
                deposit(current_user,connection)
            elif option == 2:
                withdraw(current_user,connection)
            elif option == 3:
                check_balance(current_user)
            elif option == 4 :
                show_profile(current_user,connection)
            elif option == 5:
                break
            else:
                option = 0

        connection.close()
        print("\nThank You For Using Our System!\n")
        print("Made With ❤️ By Mohammed Osama.")
        print("-"*30)
        print("Project : 🏧 Dr.Gamal M.Behery.")
        print("-"*30)
        # play sound
        file = "assets/audio/air.mp3"
        system("mpg123 " + file + " > /dev/null 2>&1")