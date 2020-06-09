# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CWei,2020.06.04,Added variables
#     ,2020.06.05,Worked on FileProcessor & IO methods
#     ,2020.06.06, added Product class attributes
#     ,2020.06.07, debug Add to list
#     ,2020.06.08, " " " "
#     ,2020.06.08, " " " View list Table data
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []    # List of Products & Prices
lstOfNewProd = []           # List row of new Prod/Prices
objF = None                 # An object that represents a file
strChoice = ""              # Captures the user menu selection
objProd = ""                # object for 'Product' class


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CWei,06.06.2020,Modified code to complete assignment 8
        CWei,06.07.2020,Redo attributes
    """
    # Add Code to the Product class
    # -- Fields --
    # product_name = ""
    # product_price = 0.00

    # -- CONST --
    def __init__(self, pName:str, pPrice:float):
        """ create implicit fields for Product and price

        :param pName: (string)
        :param pPrice: (float) 
        """
        # -- ATTR --
        try:
            self.__prodName = str(pName)
            self.__prodPrice = float(pPrice)
        except Exception as e:
            raise Exception("\n" + str(e))
        
    # -- PROP --
    # Property getter/setter for Product Name
    @property
    def prodName(self):
        return str(self.__prodName).title()     # Title case

    @prodName.setter
    def prodName(self, pName):
        """ Ensure the Product Name is not a number

        :param pName: (string)
        :return:
        """
        if str(pName).isnumeric() == False:
            self.__prodName = pName
        else:
            raise Exception("Product Names cannot be numbers")

    # Propert getter/setter for Product Price
    @property
    def prodPrice(self):
        return str(self.__prodPrice)

    @prodPrice.setter
    def prodPrice(self, pPrice):
        if str(pPrice).isnumeric == True:
            self.__prodPrice = pPrice
        else:
            raise Exception("Product Price must be a number.")

    # -- METH --
    def __str__(self):
        return self.prodName + "," + self.prodPrice

# End of Product class ---------------------------------------------------- #
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CWei,06.06.2020,Modified code to complete assignment 8
        CWei,06.06.2020,add try/except
    """
    #  overwrite data to file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Save list from RAM to file

        :param file_name: (text) file
        :param list_of_product_objects: (list) of product and price
        :return: (nothing)
        """
        try:
            objF = open(file_name, "w")
            for row in list_of_product_objects:
                objF.write(str(row[0]) + "," + str(row[1]) + "\n")
            objF.close()
        except IOError:
            print("Unable to locate file")
        
    # read in data to RAM
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list table in RAM

        :param file_name: (string) of data
        :return: (list) of product and price
        """
        list_of_product_objects = []
        try:
            with open(file_name, "r") as objF:
                for row in objF:
                    list_of_product_objects.append(row.strip().split(","))     # removes '\n', etc
        except IOError:
            print("\tProduct database is empty.\nAdd new products.")
            with open(file_name, "a") as objF:
                lstrow = ["Product", "Price"]
                objF.write(str(lstrow[0]) + "," + str(lstrow[1]))

        return list_of_product_objects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Input and output functions
    
    """
    # docstring
    #  show menu to user
    @staticmethod
    def print_product_menu():
        """ Displays menu to user

        :return: (nothing)
        """
        print("""
        Menu
        1 - Display Product Price Inventory
        2 - Add New Product
        3 - Save Session
        4 - Exit Session        
        """)

    # get user's choice
    @staticmethod
    def input_menu_choice():
        """ Assign value option

        :return: (stirng)
        """
        try:
            choice = str(input("Which option would you like to perform? [1 - 4]: "))
        except TypeError:
            print(" Please enter menu options 1, 2, 3, or 4: ")

        print()
        return choice

    # show the current data from the file to user
    @staticmethod
    def print_Products_List(list_of_product_objects):
        """ Displays Products & Prices in list table

        :param list_of_product_objects: (list) of rows in RAM
        :return: (nothing)
        """
        print("""
        ********************************************
        Your current product data is:
        --------------------------------------------
        """)
        try:
            #print("\t\t\t", list_of_product_objects[0])    # ,list_of_product_objects[0], list_of_product_objects[1])
            for row in list_of_product_objects:
                print("\t\t" + row[0] + ", $" + row[1])
        except IOError as e:
            raise Exception("Problem with print statement" + str(e))
        print("""
        ********************************************
        """)

    # get product data from user
    @staticmethod
    def add_new_product():
        """ Ask for new product and price

        :return: (string)
        """
        try:
            prod_name = str(input("Enter the product name: "))     # removed string keyword
            prod_price = float(input("Enter the price: "))           # removed float keyword
        except ValueError as e:
            raise Exception("Data type is invalid\n" + str(e.__doc__))
        return prod_name, prod_price

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Data Code to the Main body
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
# print(lstOfProductObjects)

try:
    while (True):
        # Show user a menu of options
        IO.print_product_menu()

        # Get user's menu option choice
        strChoice = IO.input_menu_choice()

        # 1 - Show user current data in the list of product objects
        if strChoice == "1":
            IO.print_Products_List(lstOfProductObjects)

        # 2 - Let user add data to the list of product objects
        if strChoice == "2":
            (strProdName, fltProdPrice) = IO.add_new_product()
            objProd = Product(strProdName, fltProdPrice)
            # lstOfProductObjects += [objProd.__str__()]
            lstOfNewProd = [objProd.__str__().split(",")]
            # lstOfProductObjects.append(lstOfNewProd)
            lstOfProductObjects += lstOfNewProd
            # print(lstOfProductObjects[0])
            IO.print_Products_List(lstOfProductObjects)

        # 3 - let user save current data to file and exit program
        if strChoice == "3":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)

        # 4 - End session
        if strChoice == "4":
            strChoice = input("Do you wish to save data? [y/n]: ")
            if strChoice.lower() == "y":
                print("Session saved to file.")
                FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            else:
                print("session will end without saving new data.")
            break
                
except Exception as e:
    print("Error with Product app:\n" + str(e.__doc__))

input("Press the [Enter] key to close session window.")

# Main Body of Script  ---------------------------------------------------- #

