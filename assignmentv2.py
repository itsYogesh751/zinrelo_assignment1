import re
import csv
import datetime
import sys
import os

"""Order class for initializing orderId and user object"""
class Order:                           
    def __init__(self,orderId,user):
        self.orderId=orderId
        self.user=user

"""User class for Initializing name,email,birthdate,zipcode and state and 
   has all user validation functions"""
class User:
    """Initialzing User object"""
    def __init__(self,name,email,birthdate,zipcode,state):
        self.name=name
        self.email=email
        self.birthdate=birthdate
        self.zipcode=zipcode
        self.state=state
    
    """To get day for the given date"""
    def get_day_from_date(self,birthdate):
        setOfDays=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
        return setOfDays[birthdate.weekday()]
    
    """To check whether email is valid or not by using regular expression"""
    def is_valid_email(self):
        regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{1,3}\b'
        if(re.fullmatch(regex, self.email)):
             return True
        return False

    """To check whether zipcode has consecutive digits"""
    def zipcode_not_have_consecutive_digits(self):
        n=len(self.zipcode)
        while n>1:
            if abs(int(self.zipcode[n-1])-int(self.zipcode[n-2]))==1:
                return False
            n-=1
        return True
    
    """To check whether age is 21 or older using datetime object"""
    def is_valid_age(self,current_date):
        birthdate = datetime.datetime.strptime(self.birthdate, "%m/%d/%Y").date()
        current_date=datetime.datetime.strptime(current_date,"%Y-%m-%d").date()
        age=current_date.year-birthdate.year
        if age > 21:
            return True
        elif age==21:
            if current_date.month < birthdate.month:
                return False
            else:
                return True
        return False 

    """To check whether birthday is first monday or not"""
    def is_valid_birthdate(self):
        birthdate = datetime.datetime.strptime(self.birthdate, "%m/%d/%Y").date()
        if birthdate.day > 7:
            return True
        else:
            if self.get_day_from_date(birthdate) != 'Monday':
                return True
        return False
    
    """To check whether state is restricted state or not"""
    def is_not_in_restricted_state(self):
        statesThatNeedToBeExcluded = {'NJ', 'CT', 'OR', 'ID', 'PA', 'MA', 'IL'}
        if self.state not in statesThatNeedToBeExcluded:
            return True
        return False
    
"""Class for reading and writing to valid and invalid csv files"""
class AcmeWine:
    """Initialization of valid,invalid and order csv files"""
    def __init__(self, orderFile):
        self.orderFile = orderFile
        self.validCsvFile = "valid1.csv"
        self.invalidCsvFile = "invalid1.csv"

    """To read orders csv file and store objects of order class into listOfOrders"""
    def read_csv_file(self):
        listOfOrders = []
        with open(self.orderFile, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header row

            for row in csvreader:
                orderId = row[0]
                name = row[1]
                email = row[3]
                birthdate = row[2]
               # birthdate = datetime.datetime.strptime(row[2], "%m/%d/%Y").date()
                zipcode = row[5]
                state=row[4]

                user = User(name, email, birthdate, zipcode,state)
                order = Order(orderId, user)
                listOfOrders.append(order)

        return listOfOrders

    """To write to valid csv file"""
    def write_to_valid_csv_file(self, orderId):
        with open(self.validCsvFile, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([orderId])

    """To write to invalid csv file"""
    def write_to_invalid_csv_file(self, orderId):
        with open(self.invalidCsvFile, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([orderId])

    """To process orders and run is_valid_order function"""
    def process_orders(self):
        orders = self.read_csv_file()

        for order in orders:
            if self.is_valid_order(order):
                self.write_to_valid_csv_file(order.orderId)
            else:
                self.write_to_invalid_csv_file(order.orderId)

    """To check if order is valid using all validation functions defined in user class"""
    def is_valid_order(self, order):
    
        return (
            order.user.is_not_in_restricted_state()
            and order.user.is_valid_age(str(datetime.date.today()))
            and order.user.is_valid_birthdate()
            and order.user.is_valid_email()
            and order.user.zipcode_not_have_consecutive_digits()
        )

def main():
    if len(sys.argv) < 2:
        print("Please provide the order file path as a command-line argument.")
        return

    orderFile = sys.argv[1]
    os.remove("/home/zinrelo/Downloads/zinrelo_assignnment1/invalid1.csv")
    os.remove("/home/zinrelo/Downloads/zinrelo_assignnment1//valid1.csv")

    processor = AcmeWine(orderFile)
    processor.process_orders()


if __name__ == "__main__":
    main()