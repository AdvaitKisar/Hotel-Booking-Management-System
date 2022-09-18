# Hotel Booking Management System
## Introduction
This project helps to book rooms in a hotel as per our choice and allots the same after checking for availability of the room as per our input. It also helps us to process and manage the billing system and maintains the financial records for the hotel as well. This system is designed in such a way that the entire hotel is divided into 4 equal sections, with top half having air conditioned rooms and bottom half having non-AC rooms. These halves are further divided such that the top half of each half has rooms with 3 beds and bottom half has rooms with 2 beds.
## Files used
The project mainly has a main python file (*main.py*) which invokes the function python file's (*func.py*) **'Home'** function. The **Home** function in turn prompts the user to select an option from 9 options, which are listed in the file (*home.txt*). As per the user's input for the previous prompt, the program invokes the corresponding function. The menu of the restaurant is stored in the text file (*menu.txt*) and excelsheet (*menu.xlsx*). The room info is stored in the text file (*room_info.txt*). The record of all customers is stored in the excelsheet (*Customer Data of Hotel <hotel_name>.xlsx*).
## Working of the Program
### Function File
When the main file invokes home function from function file, the function file firstly checks for excelsheet containing previous records of customers and if it's present in the directory, it will import all the data from each column for further computation. If it's not present, the program will create empty lists which can be used later for computation.

### Home Function
As per the input from the user, the program will redirect the user to room info for '1', booking for '2', restaurant for '3', other services for '4', payment for '5', saving the data manually (by hotel staff) for '6', generating record for '7', giving feedback/rating for '8' and exiting the program for '0'.

### Booking Function
The booking function prompts the user to enter the check-in and check-out dates in DD/MM/YYYY format. Also, the booking can only be done within a specific time duration which is 180 days in this program starting from the next day. Then the program checks if these dates are valid and within the range of the specified duration. It also checks if the check-in is before check-out, or else it will prompt the user to re-enter the dates. After that, the program will display the room info again followed by the prompt for choice of room type among the 4 options described in the introduction. Hence, the program will generate the room no. randomly within the range constrained by choice of room. The customer ID is also generated from 10000 onwards.
Now, for checking the availability,the criteria is that the duration of the customer's stay should not overlap with an old customer's duration of stay for a given room no. Hence, it can be mathematically proven that if product of separations of the check-in date of new customer and check-out date of old customer & check-in date of old customer and check-out date of new customer is negative, then that particular room is available for the new customer. Therefore, the program computes the products of separations for every old customer from the data obtained from the database w.r.t. the new customer. Also, it finds the rooms used till date. Now, if the randomly generated room no. is already used before or if the customer ID is already existing before, the program will check for availability as per the product of separations algorithm and determine the availability of the room. If it's available, then that particular room is allotted to the new customer or else new room no. is generated and process is repeated again. If the customer ID is found to be repeated, then it is incremented by 1. If all the rooms for a given choice of room type and interval are occupied, the loop will keep on running for searching the room until a max loop count is reached (here, 100), after which the program propts to change the choice or dates as it could not allot any room becuase of unavailability.
After the room is confirmed, the user is asked for any extra beds if required and then all the price values, and other details are stored in the lists. Next, comes the customer-info section, where the customer has to enter all his/her details and specify who is the head of their group. The head person's details are stored and the room is finally booked! All the data is automatically saved in the excelsheet while booking, no need to manually save anything.

### Restaurant Function
For entering the restaurant, the user has to enter his/her customer ID and then he has to select the items and their quantity he/she wants from the menu displayed. If a user enters wrong customer ID, then he/she would be propmted to enter the customer ID again. If a person doesn't want to order anything or if the order is finished, the user has to enter '0'. The program will compute the total amount of the restaurant charges and will generate a text file having the restaurant bill printed in it and it will also print the same on the terminal. The program will also add this cost to net cost and save all the data in the excelsheet of the database automatically. 

### Other Services Function
The other services function includes the services with input such as Cab for '1', Laundry for '2', Spa for '3', Valet Parking for '4' and for exitting the program , the user needs to enter '0'. For any of the inputs for the services above, the user has to enter the customer ID and enter service specific parameters and the net cost of the service is included in other charges and net price is also updated. All the data is again simultaneously updated in the excelsheet.

### Payment Function
For doing the payment, the user has to enter his/her customer ID and registered phone number. If a user enters wrong customer ID or phone no., then he/she would be propmted to enter the customer ID and phone no. again. The user is now asked to opt for a payment method, after which the program will compute the total amount of the restaurant charges, staying charges & other charges and will generate a text file having the bill printed in it and it will also print the same on the terminal.The program will save all the data in the excelsheet of the database automatically.

### Save Data Function
This function is called in several other functions to store the data during runtime, but one can also save the data manually by entering '6' in the Home function's input.

### Record Function
The record function prints all the details of all the customers who have stayed in the hotel till date.

### Feedback Function
The feedback function is either invoked through the home function where the user has to enter the customer ID himself/herself for giving the feedback and rating. Or else, it is invoked in the payment function if the customer hasn't given any rating/feedback earlier. In this case, he/she doesn't need to enter the customer ID again. The feedback function asks for a rating between 1 to 5 and a feedback in the form of a string. If the input is irrelevant, the function prompts the user to re-enter feedback or rating or both depending on the irrelevance of the previous input. Finally, the feedback and rating are stored in the lists made for them and updated in the excelsheet automatically.

## Salient Features of the Program
1. The program will never allot the same room to two customers during a specific interval and will search for the new room continuously by ensuring that room is vacant for all days of the stay of the customer.
2. The prices are computed simultaneously for all services during runtime.
3. No need to manually save the data each time as it is saved automatically while running each function.
4. Biggest advantage is that the data of the old customers remains intact even if the program stops running and the program starts running from where it stopped in the past.
5. All the financial payment data is also stored intact forever which can be retrieved later by the excelsheet or generating the record.
6. The bill receipts can be generated and saved for reference in future.
7. The same program can be modified further for generating invoices, quotations for businesses and can be used in many places like offices, medical stores, hospitals, banks, etc.
