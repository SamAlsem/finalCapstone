from tabulate import tabulate


# Create a shoe class with country, code, product, cost and quantity objects
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # get_cost returns the cost of the shoe
    def get_cost(self):
        return self.cost

     # get_quantity returns the quantity of the shoe
    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country} {self.code} {self.product} {self.cost} {self.quantity}"

    # Further methods added for below functions
     # get_product returns the product name of the shoe
    def get_product(self):
        return self.product

     # get_code returns the product code of the shoe
    def get_code(self):
        return self.code


# =============Shoe list===========
shoe_list = []
# ==========Functions outside the class==============


def read_shoes_data():

    # Using try and except for error handling, open the inventory.txt file, skipping the first item
    # Loop through the data, removing spacing and commas
    # create a Shoe object
    # Append this object to the empty shoe_list
    try:
        file = open("inventory.txt", "r").readlines()[1:]
        for line in file:
            data = line.strip().split(",")
            shoe_create = Shoe(data[0], data[1], data[2], data[3], data[4])
            shoe_list.append(shoe_create)

    except FileNotFoundError:
        print("File not found: inventory.txt")


view_data = read_shoes_data()


def data_shoes():
    view_data
    for shoe in shoe_list:
        return shoe


def capture_shoes():

    # Provide inputs to get the relevant country, code, product, code and quantity data
    country = input("Country of origin: ")
    code = input("Product code: ")
    product = input("Product name: ")
    cost = int(input("Product cost: "))
    quantity = int(input("Number of pairs of shoes: "))

    # Use this data to create a new shoe object and append to the shoe_list
    shoe_create = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_create)
    print(f"{shoe_create} added to shoe_list")


def view_all():

    # User given the option to view the data from the shoe_list object or to view in a tabulated format
    choice = input(
        "View data from object to tab, by selecting 'object' or 'tab'")
    # If the object is chosen, the read_shoes_data() function is called and the shoe_list is looped over and printed
    if choice == "object":
        data_shoes()
        # read_shoes_data()
        print("Country, Code, Product, Cost, Quantity: \n")
        for shoe in shoe_list:
            print(shoe)

    # Is the tab option is chosen instead, the file is opened, and the data is appended to a list within a list and printed accordingly
    elif choice == 'tab':
        # In order to tabulate the data, open the file
        shoe_data = []
        file = open("inventory.txt", "r").readlines()[1:]
        for line in file:
            data = line.strip().split(",")
            shoe_data.append(data)

        header = ["Country", "Code", "Product", "Cost", "Quantity"]
        print(tabulate(shoe_data, header))

    else:
        print("Incorrect input")
        Main()


def re_stock():

    # Clear the current inventory
    inventory_clear = open("inventory.txt", "w")
    inventory_clear.close()

    # find the minimum quantity within the shoe_list and set to a variable
    lowest = min(shoe_list, key=lambda shoe: int(shoe.quantity))
    print(f"The following range is low in stock: {lowest}")

    # find the index of where the low quantity item is stored within the shoe_list so that it can be re-added once updated
    lowest_index = shoe_list.index(lowest)

    # Ask user if they want to order more stock, if yes, request the number of additional pairs to order. If not, return them to the main menu.
    choice = input("Would you like to order more of these? (y/n) ")
    if choice == 'y':
        shoe_quant = int(input(
            "How many pairs would you like to order? : "))

        # Update the quantity by adding the existing number of pairs to additionally ordered pairs
        lowest.quantity = int(lowest.quantity) + shoe_quant
        print(
            f"You have ordered {shoe_quant} more pairs, updated to {lowest}")

        # Return this updated data within its index in the shoe_list
        shoe_list[lowest_index] = lowest
        # Write this updated data to the inventory.txt file
        try:
            with open("inventory.txt", 'w') as update_file:
                update_file.write("Country,Code,Product,Cost,Quantity")
                for shoe in shoe_list:
                    update_file.writelines(
                        f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
        except FileNotFoundError:
            print("File not found, unable to write this information to file")
    # User is returned to the main menu if they select n or any other key that 'y'
    else:
        Main()


def search_shoe(code_input):

    # Call the read_shoes_data function to access the shoe_list
    # Call the search_code function with parameter, code-input which is supplied as the code_input variable
    # loop through the shoe_list, if the code in the list matches the code_input, return the item or else nothing is returned
    # If the item exists, print it out, or else print that the code was not found

    for shoe in shoe_list:
        if shoe.code == code_input:
            return shoe

    return None


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Call the read_shoes_data function to access the inventory
    # loop through the list
    # call the product, code, cost and quantity methods from the shoe class and store in a variable
    # Calculate the value of the shoes by multiplying the cost and quantity
    # Print out the result

    for shoe in shoe_list:
        product_name = shoe.get_product()
        product_code = shoe.get_code()
        shoe_cost = int(shoe.get_cost())
        shoe_quantity = int(shoe.get_quantity())
        value = float(shoe_cost * shoe_quantity)
        print()
        print(f"Product: {product_name} Code: {product_code} Value: R{value}")


def highest_qty():

    # Call the read_shoes_data function to access the inventory
    # loop through the list
    # Find the number of shoes using the get_quantity method and convert to an integer and save it to a variable qty
    # if there are more than 40 pairs available, stringify and print these out

    for shoe in shoe_list:
        qty = int(shoe.get_quantity())
        if qty >= 40:
            shoe_highest = str(shoe)
            print()
            print(shoe_highest)


# ==========Main Menu=============

def Main():

    user_input = ""
    while user_input != 'quit':
        user_input = input('''Select action:
        * view = view all shoes
        * add = add a new shoe range to the database
        * low = view low stock items and order more
        * search = search for a particular shoe range by code
        * value = provides total value for each range of shoes
        * quantity = shows high quantity shoe ranges to put on sale
        * quit = exit
        ''')
        if user_input == 'view':
            view_all()

        elif user_input == 'add':
            capture_shoes()

        elif user_input == "low":
            data_shoes()
            # read_shoes_data()
            re_stock()

        elif user_input == "search":
            data_shoes()
            # read_shoes_data()
            code_input = input(
                "Enter the code of the shoes you are searching for: ")
            shoe = search_shoe(code_input)
            if shoe:
                print()
                print("Item found: ")
                print(shoe)
            else:
                print("Code not found")

        elif user_input == "value":
            print("The value of each shoe range is as follows: ")
            data_shoes()
            # read_shoes_data()
            value_per_item()

        elif user_input == "quantity":
            print("The following shoes should be put on sale: ")
            data_shoes()
            # read_shoes_data()
            highest_qty()

        elif user_input == "quit":
            print("Goodbye")

        else:
            print("Incorrect input, please try again")


Main()
