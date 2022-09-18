# Importing libraries
import random as rd
from datetime import date
from datetime import timedelta as td
import datetime as dt
import pandas as pd
import os

hotel_name = 'Southern Crest' # Name of hotel
# Path
path = f'D:/Advait/Python/Personal Projects/Hotel Booking Management System/Customer Data of Hotel {hotel_name}.xlsx'

# Check whether a path pointing to a file
isFile = os.path.isfile(path)
if isFile == True:
    # Importing existing data 
    sheet1 = pd.read_excel('Customer Data of Hotel {}.xlsx'.format(hotel_name), "Sheet1")
    name_list = [sheet1.iloc[:, 1][i] for i in range(len(sheet1.iloc[:, 1]))]
    phno_list = [sheet1.iloc[:, 2][i] for i in range(len(sheet1.iloc[:, 2]))]
    add_list = [sheet1.iloc[:, 3][i] for i in range(len(sheet1.iloc[:, 3]))]
    cust_list = [sheet1.iloc[:, 4][i] for i in range(len(sheet1.iloc[:, 4]))]
    room_no_list = [sheet1.iloc[:, 5][i] for i in range(len(sheet1.iloc[:, 5]))]
    room_type = [sheet1.iloc[:, 6][i] for i in range(len(sheet1.iloc[:, 6]))]
    checkin_list = [sheet1.iloc[:, 7][i] for i in range(len(sheet1.iloc[:, 7]))]
    checkout_list = [sheet1.iloc[:, 8][i] for i in range(len(sheet1.iloc[:, 8]))]
    room_charges = [sheet1.iloc[:, 9][i] for i in range(len(sheet1.iloc[:, 9]))]
    rest_charges = [sheet1.iloc[:, 10][i] for i in range(len(sheet1.iloc[:, 10]))]
    other_charges = [sheet1.iloc[:, 11][i] for i in range(len(sheet1.iloc[:, 11]))]
    net_price_list = [sheet1.iloc[:, 12][i] for i in range(len(sheet1.iloc[:, 12]))]
    payment_opt_list = [sheet1.iloc[:, 13][i] for i in range(len(sheet1.iloc[:, 13]))]
else:
    name_list = []
    phno_list = []
    add_list = []
    cust_list = []
    room_no_list = []
    room_type = []
    checkin_list = []
    checkout_list = []
    room_charges = []
    rest_charges = []
    other_charges = []
    net_price_list = []
    payment_opt_list = []

head_list = []

n_f = 4 # No. of floors in the hotel (should be multiple of 4)
# Hotel is divided in 4 sections as per rooms and bottom half is NON AC and top half is AC
n_rf = 2 # No. of rooms on each floor
n_days = 180 # No. of holidays for which booking is open
todays_date = date.today()
start_date = todays_date + td(1) # Booking starts from tomorrow till next 180 days
end_date = start_date + td(n_days)

class Customer(): # Class for storing customer details temporarily
    def __init__(self, name, age, gender, Mobile_no, address, head, checkin, checkout):
        self.name = name
        self.age = age
        self.gender = gender
        self.Mobile_no = Mobile_no
        self.add = address
        self.head = head
        self.checkin = checkin
        self.checkout = checkout

class HeadCustomer(): # Class for storing head customer's details
    def __init__(self, name, age, gender, Mobile_no, address, head, custid, checkin, checkout):
        self.name = name
        self.age = age
        self.gender = gender
        self.Mobile_no = Mobile_no
        self.add = address
        self.head = head
        self.Cust_ID = custid
        self.checkin = checkin
        self.checkout = checkout

# Home Function
def Home():
    print("\t\t  WELCOME TO HOTEL {}\n".format(hotel_name.upper()))
    file_home = open('home.txt', 'r')
    content = file_home.read()
    print(content)
    file_home.close()
    home_val = int(input("Enter the number for selecting one of the options: "))
    if home_val == 1:
        room_info(1)
    elif home_val == 2:
        booking()
    elif home_val == 3:
        restaurant()
    elif home_val == 4:
        other_services()
    elif home_val == 5:
        payment()
    elif home_val == 6:
        save_data(1)
    elif home_val == 7:
        record()
    elif home_val != 0:
        print("Invalid Option.")
        print("Please re-enter a correct option.")
        print("Or else enter 0 for exiting the menu.")
        Home()
    else:
        exit

def room_info(j): # Function printing room info
    print("\t\t\t ROOM INFO\n")
    file_room_info = open('room_info.txt', 'r')
    content = file_room_info.read()
    print(content)
    file_room_info.close()
    if j == 1:
        n = int(input("Enter 1 for Home and 0 for Exit.\n"))
        if n == 1:
            Home()
        else:
            exit()  

def room_prices(type_room): # Function for finding room prices per day as per type of room
    if type_room == 1:
        p = 4000
    elif type_room == 2:
        p = 3500
    elif type_room == 3:
        p = 2000
    elif type_room == 4:
        p = 1500
    else:
        print("Your input is incorrect.\n")
    return p

def room_type_func(type_room): # Function for writing type of room as per input
    if type_room == 1:
        rt = "AC Room with 3 beds"
    elif type_room == 2:
        rt = "AC Room with 2 beds"
    elif type_room == 3:
        rt = "Non-AC Room with 3 beds"
    elif type_room == 4:
        rt = "Non-AC Room with 2 beds"
    else:
        print("Your input is incorrect.\n")
    return rt

def booking(): # Function for booking a room
    print("The booking can be done between any dates including {} and {} inclusively.".format(start_date, end_date))
    check_in_date = str(input("Enter Check-in Date in DD/MM/YYYY format: "))
    check_out_date = str(input("Enter Check-out Date in DD/MM/YYYY format: "))
    check_in_date.split('/') # Splitting the dates
    check_out_date.split('/')
    ci_dd, ci_mm, ci_yyyy = int(check_in_date[0:2]), int(check_in_date[3:5]), int(check_in_date[6:10])
    co_dd, co_mm, co_yyyy = int(check_out_date[0:2]), int(check_out_date[3:5]), int(check_out_date[6:10])
    date(ci_dd, ci_mm, ci_yyyy) # Finding if this date is within the range of booking
    date(co_dd, co_mm, co_yyyy)
    stay = (dt.date(co_yyyy, co_mm, co_dd) - dt.date(ci_yyyy, ci_mm, ci_dd)).days # Duration of stay
    if stay > 0:
        pass
    else:
        print("The Check-out date should be after the check-in date.")
        print("Please re-enter the new correct dates")
        booking()
    print()
    print("\t\t\t SELECT ROOMS")
    room_info(0)
    print()
    type_room = int(input("Enter the choice of room you want: "))
    while type_room not in [1, 2, 3, 4]:
        print("The input for type of room is invalid")
        type_room = int(input("Enter the choice of room you want: "))
    floor_no = rd.randint(1 + (4 - type_room)*(n_f/4), (5 - type_room)*(n_f/4)) # Finding random floor no. for given type of room
    room_no = rd.randint(1, n_rf) # Finding random room no. for given type of room
    rn = 100*floor_no+room_no # Finding corresponding room no. on the floor no. generated
    cust_id = 10000 +  len(room_no_list) # Generating customer id from 10000 onwards
    loop_count = 0
    prod_arr = [0 for l in range(len(room_no_list))]
    for k in range(len(room_no_list)): # Finding the product of separation of previous customers w.r.t. new customer to ensure that none of the two customers get the same room in same period
        old_person_checkin = checkin_list[k]
        old_person_checkin.split('/')
        old_person_checkout = checkout_list[k]
        old_person_checkout.split('/')
        op_ci_dd, op_ci_mm, op_ci_yyyy = int(old_person_checkin[0:2]), int(old_person_checkin[3:5]), int(old_person_checkin[6:10])
        op_co_dd, op_co_mm, op_co_yyyy = int(old_person_checkout[0:2]), int(old_person_checkout[3:5]), int(old_person_checkout[6:10])
        sepn_a = (dt.date(ci_yyyy, ci_mm, ci_dd) - dt.date(op_co_yyyy, op_co_mm, op_co_dd)).days
        sepn_b = (dt.date(op_ci_yyyy, op_ci_mm, op_ci_dd) - dt.date(co_yyyy, co_mm, co_dd)).days
        prod_arr[k] = sepn_a*sepn_b
    
    rooms_used = []
    i = 0
    for i in range(len(room_no_list)): # Finding the list of rooms used
        if room_no_list[i] not in rooms_used:
            rooms_used.append(room_no_list[i])

    room_avail = 0 # Indicator for checking the availability for given input
    temp_prod = []
    while room_avail == 0:
        if rn in rooms_used or cust_id in cust_list: # If either the room is used or else if customer id is same, new room no. and customer ID will be generated
            temp_prod = [(prod_arr[q]) for q in range(len(prod_arr))]
            for k in range(len(room_no_list)):
                if room_no_list[k] != rn:
                    temp_prod[k] = 0
            loop_count = loop_count + 1
            room_count = 0
            prod_count = 0
            for l in range(len(room_no_list)):
                if room_no_list[l] == rn:
                    room_count = room_count + 1
                if temp_prod[l] < 0: # If product of separation is negative, the room is available or else it's not
                    prod_count = prod_count + 1
            if room_count == prod_count and prod_count > 0:
                room_avail = 1 # Turns indicator as 1 when room is available
            else: # Generates new room no. and customer ID
                floor_no = rd.randint(1 + (4 - type_room)*(n_f/4), (5 - type_room)*(n_f/4))
                room_no = rd.randint(1, n_rf)
                rn = 100*floor_no+room_no
                if cust_id in cust_list:
                    cust_id = cust_id + 1
            if loop_count > 100: # Stops the loop if it is executed more than 100 times as room is not available for given input
                print("Sorry, the room type which you want is currently not available")
                print("Kindly change the type of room you want.\n")
                n = int(input("Enter 1 for Home, 2 for Booking and 0 for Exit.\n"))
                if n == 1:
                    Home()
                elif n == 2:
                    booking()
                else:
                    exit()
            if room_avail == 1:
                break
        else:
            room_avail = 1
        
    price = room_prices(type_room)*stay
    bed = input("Do you want any extra beds?: ")
    if bed[0] == 'Y' or bed[0] == 'y':
        n_bed = int(input("Enter the no. of beds you want: "))
        price = price + 200*n_bed*stay
    room_charges.append(price)
    rest_charges.append(0)
    net_price_list.append(0)
    other_charges.append(0)
    net_price_calculate() # Calculates net price
    room_no_list.append(rn)
    room_type.append(room_type_func(type_room))
    payment_opt_list.append('Not selected yet')
    # Taking details of customers
    n_p = int(input("Enter total no. of people: "))
    for i in range(n_p):
        while True:
            name = input("Enter the name of Person No. {} : ".format(i+1))
            Mobile_no = int(input("Enter the Mobile No. of Person No. {} : ".format(i+1)))
            address = input("Enter the address of Person No. {} : ".format(i+1))
            if name != '' and Mobile_no >= pow(10, 9) and Mobile_no < pow(10, 10) and address != '':
                break
            else:
                print("The fields of Name, Address and Mobile No. are mandatory and mobile no. should be 10 digit no.")
        age = int(input("Enter the age of Person No. {} : ".format(i+1)))
        gender = input("Enter the gender of Person No. {} : ".format(i+1))
        head = 0
        if n_p == 1:
            head = 1
        else:
            head = int(input("Enter 1 if you are the head of the group or else enter 0: "))
            Person = Customer(name, age, gender, Mobile_no, address, head, check_in_date, check_out_date)
        if head == 1 and name not in name_list:
                HeadPerson = HeadCustomer(name, age, gender, Mobile_no, address, head, cust_id, check_in_date, check_out_date)
                head_list.append(HeadPerson)
                name_list.append(HeadPerson.name)
                phno_list.append(HeadPerson.Mobile_no)
                add_list.append(HeadPerson.add)
                checkin_list.append(HeadPerson.checkin)
                checkout_list.append(HeadPerson.checkout)
                cust_list.append(HeadPerson.Cust_ID)
        elif head == 1 and name in name_list and name != name_list[-1]:
                HeadPerson = HeadCustomer(name, age, gender, Mobile_no, address, head, cust_id, check_in_date, check_out_date)
                head_list.append(HeadPerson)
                name_list.append(HeadPerson.name)
                phno_list.append(HeadPerson.Mobile_no)
                add_list.append(HeadPerson.add)
                checkin_list.append(HeadPerson.checkin)
                checkout_list.append(HeadPerson.checkout)
                cust_list.append(HeadPerson.Cust_ID)
    print("Congratulations! Your booking in Hotel {} is successful for the duration from {} to {}.".format(hotel_name, check_in_date, check_out_date))
    print("Your room no is {} and your customer ID is {} and the total staying charges are Rs. {}.\n".format(rn, cust_id, price))
    print()
    save_data(0) # Saving data in excelsheet
    output()
    n = int(input("Enter 1 for Home and 0 for Exit.\n"))
    if n == 1:
        Home()
    else:
        exit()

def date(dd, mm, yyyy): # Function for checking if the date entered is valid or not
    date_entered = dt.date(yyyy, mm, dd)
    if int((date_entered - start_date).days) <= n_days and int((date_entered - start_date).days) >= 0:
        pass
    else: 
        print("Booking not possible")
        print("Re-enter correct dates")
        booking()

def restaurant(): # Function for restaurant
    CI = int(input("Enter your Customer ID: "))
    if CI not in cust_list:
        print("You have entered an invalid Customer ID.")
        print("Please re-enter correct Customer ID.")
        n = int(input("Enter 1 for Home, 2 for Restaurant and 0 for Exit.\n"))
        if n == 1:
            Home()
        elif n == 2:
            restaurant()
        else:
            exit()
    CI_index = cust_list.index(CI)
    CI_ind = 0
    for i in range(len(cust_list)):
        if cust_list[i] == CI:
            CI_ind = 1
            break
    if CI_ind == 1: # If customer ID is valid, the program will display the menu from text file
        rc = 0
        print("\t\t\t RESTAURANT MENU ")
        file_menu = open('menu.txt', 'r')
        content = file_menu.read()
        print(content)
        file_menu.close()
        menu = pd.read_excel('menu.xlsx', "Sheet1")
        item_list = [menu.iloc[:, 1][i] for i in range(len(menu.iloc[:, 1]))] # List of items
        food_item_price_list = [menu.iloc[:, 2][i] for i in range(len(menu.iloc[:, 2]))] # List of prices
        order_matrix = [] # Matrix for storing the order list
        food_item = 1
        while food_item != 0: # Taking the order from customer
            print("Enter 0 if you don't want to order anything or else if your orders are finished.")
            food_item= int(input("Enter the serial no. one at a time for any dish you want to have: "))
            if food_item != 0:
                quantity = int(input(f"Enter the no. of {item_list[food_item-1]} you want: "))
                order_matrix.append([food_item, quantity, food_item_price_list[food_item - 1]])
        for j in range(len(order_matrix)): # Finding sum of all items
            rc = rc + int(order_matrix[j][2])*int(order_matrix[j][1])
        now = dt.datetime.now()
        date_time_str = now.strftime("%d/%m/%Y %I:%M:%S %p")
        if rc != 0: # Prints the bill summary if sum is not zero and saves it as a text file as well
            with open(f'Restaurant Bill of {name_list[CI_index]}.txt', 'a') as b:
                print("                      HOTEL {}".format(hotel_name.upper()), file=b)
                print("                    RESTAURANT BILL SUMMARY                ", file=b)
                print("Name:           {}".format(name_list[CI_index]), file=b)
                print("Mobile No:      {}".format(phno_list[CI_index]), file=b)
                print("Customer ID:    {}".format(CI), file=b)
                print("Room No.        {}".format(room_no_list[CI_index]), file=b)
                print("Date:           {}".format(date_time_str), file=b)
                print("Sr. No.   Title                                     Rate (in Rs.)   Quantity     Charges (in Rs.)", file=b)
                for j in range(100):
                    if j!= 100-1:
                        print("-", end="", file=b)
                    else:
                        print("-", file=b)
                for i in range(len(order_matrix)):
                    print(f"{i+1}.        {item_list[int(order_matrix[i][0])-1].ljust(20)}                          {str(food_item_price_list[int(order_matrix[i][0])-1]).ljust(6)}          {order_matrix[i][1]}             {float(order_matrix[i][2])*int(order_matrix[i][1])}", file=b)
                for j in range(100):
                    if j!= 100-1:
                        print("-", end="", file=b)
                    else:
                        print("-", file=b)
                print(f"          SUM:-              Rs. {rc}", file=b)
                print(f"          GST:- 18% X {str(rc).ljust(4)}:- Rs. {round(rc*0.18, 2)}", file=b)
                print(f"          TOTAL AMOUNT:-     Rs. {round(rc*1.18, 2)} (including GST)", file=b)
            print("                      HOTEL {}".format(hotel_name.upper()))
            print("                    RESTAURANT BILL SUMMARY                ")
            print("Name:           {}".format(name_list[CI_index]))
            print("Mobile No:      {}".format(phno_list[CI_index]))
            print("Customer ID:    {}".format(CI))
            print("Room No.        {}".format(room_no_list[CI_index]))
            print("Date:           {}".format(date_time_str))
            print("Sr. No.   Title                                     Rate (in Rs.)   Quantity     Charges (in Rs.)")
            for j in range(100):
                if j!= 100-1:
                    print("-", end="")
                else:
                    print("-")
            for i in range(len(order_matrix)):
                print(f"{i+1}.        {item_list[int(order_matrix[i][0])-1].ljust(20)}                          {str(food_item_price_list[int(order_matrix[i][0])-1]).ljust(6)}          {order_matrix[i][1]}             {float(order_matrix[i][2])*int(order_matrix[i][1])}")
            for j in range(100):
                if j!= 100-1:
                    print("-", end="")
                else:
                    print("-")
            print(f"          SUM:-              Rs. {rc}")
            print(f"          GST:- 18% X {str(rc).ljust(4)}:- Rs. {round(rc*0.18, 2)}")
            print(f"          TOTAL AMOUNT:-     Rs. {round(rc*1.18, 2)} (including GST)")
        rest_charges[CI_index] = rest_charges[CI_index] + rc*1.18 # Stores the restaurant charges in the main list
        save_data(0) # Saves data in excelsheet
    else:
        print("Your customer ID is invalid.")
    n = int(input("Enter 1 for Home and 0 for Exit.\n"))
    if n == 1:
        Home()
    else:
        exit()

def payment(): # Function for payment for the stay
    net_price_calculate() # Net price is calculated till now
    CI = int(input("Enter your Customer ID: "))
    if CI not in cust_list:
        print("You have entered an invalid Customer ID.")
        print("Please re-enter correct customer ID.")
        n = int(input("Enter 1 for Home, 2 for Payment and 0 for Exit.\n"))
        if n == 1:
            Home()
        elif n == 2:
            payment()
        else:
            exit()
    CI_index = cust_list.index(CI)
    CI_ind = 0
    for i in range(len(cust_list)):
        if cust_list[i] == CI:
            CI_ind = 1
            break
    if CI_ind == 1: # If customer ID is valid, it asks for phone no. which should also be valid
        ph = int(input("Enter your Mobile No.: "))
        if ph == phno_list[CI_index]:
            payment_opt_list[CI_index] = payment_opt() # Asks for payment option
            now = dt.datetime.now()
            date_time_str = now.strftime("%d/%m/%Y %I:%M:%S %p")
            with open(f'Bill of {name_list[CI_index]}.txt', 'a') as b: # Prints the bill in the terminal and stores it in a text file as well
                print("                 HOTEL {}".format(hotel_name.upper()), file=b)
                print("                     BILL SUMMARY                ", file=b)
                print("Name:           {}".format(name_list[CI_index]), file=b)
                print("Mobile No:      {}".format(ph), file=b)
                print("Customer ID:    {}".format(CI), file=b)
                print("Room No.        {}".format(room_no_list[CI_index]), file=b)
                print("Payment Method: {}".format(payment_opt_list[CI_index]), file=b)
                print("Date:           {}".format(date_time_str), file=b)
                print("Sr. No.   Title                  Charges (in Rs.)", file=b)
                for j in range(100):
                    if j!= 100-1:
                        print("-", end="", file=b)
                    else:
                        print("-", file=b)
                print("1.        Stay                        {}      ".format(room_charges[CI_index]), file=b)
                if rest_charges[CI_index] != 0:
                    print("2.        Meals                       {}      ".format(round(rest_charges[CI_index], 2)), file=b)
                if rest_charges[CI_index] != 0 and other_charges[CI_index] != 0:
                    print("3.        Other Charges               {}      ".format(round(other_charges[CI_index]), 2), file=b)
                if rest_charges[CI_index] == 0 and other_charges[CI_index] != 0:
                    print("2.        Other Charges               {}      ".format(round(other_charges[CI_index]), 2), file=b)
                for j in range(100):
                    if j!= 100-1:
                        print("-", end="", file=b)
                    else:
                        print("-", file=b)
                print("          TOTAL AMOUNT               {}      ".format(round(net_price_list[CI_index], 2)), file=b)
                print(f"The total amount you have to pay is Rs. {round(net_price_list[CI_index], 2)} for your stay at Hotel {hotel_name} from {checkin_list[CI_index]} to {checkout_list[CI_index]} in Room No. {room_no_list[CI_index]}", file=b)
                print("THANK YOU FOR YOUR STAY AT OUR HOTEL!!!", file=b)
                print("PLEASE VISIT US AGAIN", file=b)
            print("                 HOTEL {}".format(hotel_name.upper()))
            print("                     BILL SUMMARY                ")
            print("Name:           {}".format(name_list[CI_index]))
            print("Mobile No:      {}".format(ph))
            print("Customer ID:    {}".format(CI))
            print("Room No.        {}".format(room_no_list[CI_index]))
            print("Payment Method: {}".format(payment_opt_list[CI_index]))
            print("Date:           {}".format(date_time_str))
            print("Sr. No.   Title                  Charges (in Rs.)")
            for j in range(100):
                    if j!= 100-1:
                        print("-", end="")
                    else:
                        print("-")
            print("1.        Stay                        {}      ".format(room_charges[CI_index]))
            if rest_charges[CI_index] != 0:
                print("2.        Meals                       {}      ".format(round(rest_charges[CI_index], 2)))
            if rest_charges[CI_index] != 0 and other_charges[CI_index] != 0:
                print("3.        Other Charges               {}      ".format(round(other_charges[CI_index]), 2))
            if rest_charges[CI_index] == 0 and other_charges[CI_index] != 0:
                print("2.        Other Charges               {}      ".format(round(other_charges[CI_index]), 2))
            for j in range(100):
                    if j!= 100-1:
                        print("-", end="")
                    else:
                        print("-")
            print("          TOTAL AMOUNT               {}      ".format(round(net_price_list[CI_index], 2)))
            print(f"The total amount you have to pay is Rs. {round(net_price_list[CI_index], 2)} for your stay at Hotel {hotel_name} from {checkin_list[CI_index]} to {checkout_list[CI_index]} in Room No. {room_no_list[CI_index]}")
            print("THANK YOU FOR YOUR STAY AT OUR HOTEL!!!")
            print("PLEASE VISIT US AGAIN")
            save_data(0)
            n = int(input("Enter 1 for Home, 2 for Payment and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                payment()
            else:
                exit()
        else:
            print("The Mobile No. is not registered with us.\n")
            n = int(input("Enter 1 for Home, 2 for Payment and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                payment()
            else:
                exit()

def payment_opt(): # Function for choosing the payment option
    print("Options available for payment are displayed below")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Cash")
    pm_opt = int(input("Enter the serial no. for the payment option you wish to choose: "))
    if pm_opt == 1:
        opt_selected = "Credit Card"
    elif pm_opt == 2:
        opt_selected = "Debit Card"
    elif pm_opt == 3:
        opt_selected = "UPI"
    elif pm_opt == 4:
        opt_selected = "Cash"
    else:
        print("The input is invalid.")
        print("Please re-enter one of the valid inputs.")
        payment_opt()
    return opt_selected

def output(): # Printing output on the terminal
    print(name_list)
    print(phno_list)
    print(room_no_list)
    print(cust_list)
    print(checkin_list)
    print(checkout_list)
    print(room_charges)
    print(rest_charges)
    print(net_price_list)

def save_data(j): # Function for saving the excelsheet's data
    serial_no = [(i+1) for i in range(len(name_list))]
    net_price_calculate()
    df = pd.DataFrame()
    df['Sr. No.'] = serial_no
    df['Name'] = name_list
    df['Mobile No.'] = phno_list
    df['Address'] = add_list
    df['Customer ID'] = cust_list
    df['Room No.'] = room_no_list
    df['Room Type'] = room_type
    df['Check-In Date'] = checkin_list
    df['Check-Out Date'] = checkout_list
    df['Room Charges'] = room_charges
    df['Rest. Charges'] = rest_charges
    df['Other Charges'] = other_charges
    df['Total Bill'] = net_price_list
    df['Payment Option used'] = payment_opt_list
    if j == 1:
        n = int(input("Enter 1 for Home and 0 for Exit.\n"))
        if n == 1:
            Home()
        else:
            exit()
    df.to_excel('Customer Data of Hotel {}.xlsx'.format(hotel_name), index=False)

def record(): # Prints the record on terminal
    net_price_calculate()
    now = dt.datetime.now()
    date_time_str = now.strftime("%d/%m/%Y %I:%M:%S %p")
    print(f"Printing record of all customers till date as on {date_time_str}.")
    print("\t\t\t\t\t\t HOTEL {} RECORD".format(hotel_name.upper()))
    print("| Sr.No. | Name | Mobile No. | Address | Customer ID | Room No. | Room Type | Check-In Date | Check-Out Date | Total Bill (in Rs.)")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    for i in range(len(room_no_list)):
        print("|", (i+1), "|", name_list[i], "|", phno_list[i], "|", add_list[i], "|", cust_list[i], "|", room_no_list[i], "|", room_type[i], "|", checkin_list[i], "|", checkout_list[i], "|", net_price_list[i])
    n = int(input("Enter 1 for Home and 0 for Exit.\n"))
    if n == 1:
        Home()
    else:
        exit()

def net_price_calculate(): # Function for finding net price at any instant
    for i in range(len(room_charges)):
        net_price_list[i] = room_charges[i] + rest_charges[i] + other_charges[i]

def other_services(): # Function for other services
    print("Following are the other services at our hotel: ")
    print("1. CAB")
    print("2. LAUNDRY")
    print("3. SPA")
    print("4. VALET PARKING")
    print("0. HOME")
    other_svcs_inp = int(input("Enter the serial no. of the service you want: "))
    if other_svcs_inp == 1: # Function for cab service
        CI = int(input("Enter your Customer ID: "))
        if CI not in cust_list:
            print("You have entered an invalid Customer ID.")
            print("Please re-enter correct customer ID.")
            n = int(input("Enter 1 for Home, 2 for Other Services and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                other_services()
            else:
                exit()
        CI_index = cust_list.index(CI)
        CI_ind = 0
        for i in range(len(cust_list)):
            if cust_list[i] == CI:
                CI_ind = 1
                break
        if CI_ind == 1:
            os_price = 0
            print("Types of cab with their hourly rentals and daily rentals are: ")
            print("1. Mini Car  - Rs. 200 / hour - Rs. 4000 / day")
            print("2. Sedan Car - Rs. 300 / hour - Rs. 6000 / day")
            print("3. SUV       - Rs. 400 / hour - Rs. 8000 / day")
            yn = input("Do you wish to proceed: ")
            if yn[0] == 'y' or yn[0] == 'Y':
                ct = int(input("Enter the serial no. of the cab you would like to book: "))
                n_c = int(input("Enter the no. of cabs of type {}.: ".format(ct)))
                hd = int(input("Enter 1 if planning to book for hourly rentals or else 0 for daily rentals.: "))
                if hd == 1:
                    h = int(input("Enter no. of hours: "))
                    os_price = n_c*(100*(ct+1))*h
                elif hd == 0:
                    d = int(input("Enter no. of days: "))
                    os_price = n_c*(2000*(ct+1))*d
                else:
                    print("Incorrect input. Please opt for a valid choice.")
                    other_services()
            elif yn[0] == 'n' or yn[0] == 'N':
                os_price = 0
            else:
                print("Incorrect input.")
                other_services()
            other_charges[CI_index] = other_charges[CI_index] + os_price
            save_data(0) # Saving data in excelsheet
            n = int(input("Enter 1 for Home, 2 for Other Services and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                other_services()
            else:
                exit()
    
    elif other_svcs_inp == 2: # Function for laundry services
        CI = int(input("Enter your Customer ID: "))
        if CI not in cust_list:
            print("You have entered an invalid Customer ID.")
            print("Please re-enter correct customer ID.")
            n = int(input("Enter 1 for Home, 2 for Other Services and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                other_services()
            else:
                exit()
        CI_index = cust_list.index(CI)
        CI_ind = 0
        for i in range(len(cust_list)):
            if cust_list[i] == CI:
                CI_ind = 1
                break
        if CI_ind == 1:
            os_price = 0
            print("Types of services in the laundry are: ")
            print("1. Normal Press - Rs. 20/cloth")
            print("2. Urgent Press - Rs. 30/cloth")
            print("3. Dryclean - Rs. 200/cloth")
            ct = int(input("Enter the serial no. of the option you would like to choose: "))
            n_c = int(input("Enter the no. of clothes: "))
            yn = input("Do you wish to proceed?: ")
            if yn[0] == 'y' or yn[0] == 'Y':
                if ct == 1:
                    os_price = n_c*20
                elif ct == 2:
                    os_price = n_c*30
                elif ct == 3:
                    os_price = n_c*200
                else:
                    print("Incorrect input. Please opt for a valid choice.")
                    other_services()
            elif yn[0] == 'n' or yn[0] == 'N':
                os_price = 0
            else:
                print("Incorrect input.")
                other_services()
            other_charges[CI_index] = other_charges[CI_index] + os_price
            save_data(0) # Saving Data in excelsheet
            n = int(input("Enter 1 for Home, 2 for Other Services and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                other_services()
            else:
                exit()
        
    elif other_svcs_inp == 3: # Fuc=nction for Spa
        CI = int(input("Enter your Customer ID: "))
        if CI not in cust_list:
            print("You have entered an invalid Customer ID.")
            print("Please re-enter correct customer ID.")
            n = int(input("Enter 1 for Home, 2 for Other Services and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                other_services()
            else:
                exit()
        CI_index = cust_list.index(CI)
        CI_ind = 0
        for i in range(len(cust_list)):
            if cust_list[i] == CI:
                CI_ind = 1
                break
        if CI_ind == 1:
            os_price = 0
            print("Types of services in the spa are: ")
            print("1. Face Massage - Rs. 200")
            print("2. Facial       - Rs. 300")
            print("3. Body Massage - Rs. 500")
            ct = int(input("Enter the serial no. of the option you would like to choose: "))
            yn = input("Do you wish to proceed?: ")
            if yn[0] == 'y' or yn[0] == 'Y':
                if ct == 1:
                    os_price = 200
                elif ct == 2:
                    os_price = 300
                elif ct == 3:
                    os_price = 500
                else:
                    print("Incorrect input. Please opt for a valid choice.")
                    other_services()
            elif yn[0] == 'n' or yn[0] == 'N':
                os_price = 0
            else:
                print("Incorrect input.")
                other_services()
            other_charges[CI_index] = other_charges[CI_index] + os_price
            save_data(0) # Saving data in excelsheet
            n = int(input("Enter 1 for Home, 2 for Other Services and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                other_services()
            else:
                exit()

    elif other_svcs_inp == 4: # Function for valet parking
        CI = int(input("Enter your Customer ID: "))
        if CI not in cust_list:
            print("You have entered an invalid Customer ID.")
            print("Please re-enter correct customer ID.")
            n = int(input("Enter 1 for Home, 2 for Other Services and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                other_services()
            else:
                exit()
        CI_index = cust_list.index(CI)
        CI_ind = 0
        for i in range(len(cust_list)):
            if cust_list[i] == CI:
                CI_ind = 1
                break
        if CI_ind == 1:
            os_price = 0
            vn = input("Enter your vehicle's registration no: ")
            print("The valet parking charges are Rs.50.")
            yn = input("Do you wish to proceed?: ")
            if yn[0] == 'y' or yn[0] == 'Y':
                os_price = 50
            elif yn[0] == 'n' or yn[0] == 'N':
                os_price = 0
            else:
                print("Incorrect input.")
                other_services()
            other_charges[CI_index] = other_charges[CI_index] + os_price
            save_data(0)
            n = int(input("Enter 1 for Home, 2 for Other Services and 0 for Exit.\n"))
            if n == 1:
                Home()
            elif n == 2:
                other_services()
            else:
                exit()
        
    elif other_svcs_inp == 0:
        Home()

    else:
        print("Incorrect input. Please try again.")
        n = int(input("Enter 1 for Home, 2 for Other Services and 0 for Exit.\n"))
        if n == 1:
            Home()
        if n == 2:
            other_services()
        else:
            exit()
