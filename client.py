
import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number


    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server


    flag=1
    while(flag==1):
    #while message.lower().strip() != 'bye':


        #---------------------------------------------


        print("\n Python DB Menu \n \n1. Find customer  \n 2. Add customer \n 3. Delete customer \n 4. Update customer age \n 5. Update customer address \n 6. Update customer phone \n 7. Print report \n 8. Exit  \n\nSelect:")
        userInput = int(input("Enter your preffered option, i.e: enter any number between 1 to 8: "))
        if userInput==1:
            findCustomerName = input("Enter the name of the customer: ").lower()
            message=str(1)
            message+=","+findCustomerName
                #findCustomer()
        elif userInput==2:
            name = input("Enter the name of the customer: ").lower()
            while (name ==""):
                name = input("Name can not be empty! Enter the name of the customer: ").lower()
            age = input("Enter the age of the customer: ")
            if(age!=""):
                while (not age.isdigit()):
                    age = input("Age has to be a number. Enter the age of the customer: ")
            address = input("Enter the address of the customer: ")
            phone = input("Enter the phone number of the customer: ")
            message=str(2)+","+name+","+age+","+address+","+phone
                #addCustomer()
        elif userInput==3:
            name = input("Enter the name of the customer you wants to delete: ").lower()
            message=str(3)+","+name
                #deleteCustomer()
        elif userInput==4:
            name = input("Enter the name of the customer you wants to update the age: ").lower()
            fieldToBeUpdate=input("Enter the age of the customer you wants to update: ")
            if(fieldToBeUpdate!=""):
                while (not fieldToBeUpdate.isdigit()):
                    fieldToBeUpdate = input("Age has to be a number. Enter the age of the customer: ")
            message=str(4)+","+name+","+fieldToBeUpdate
                #updateCustomerAge()
        elif userInput==5:
            name = input("Enter the name of the customer you wants to update the address: ").lower()
            fieldToBeUpdate=input("Enter the address of the customer you wants to update: ")
            message=str(5)+","+name+","+" "+","+fieldToBeUpdate+","+" "
                #updateCustomerAddress()
        elif userInput==6:
            name = input("Enter the name of the customer you wants to update the phone number: ").lower()
            fieldToBeUpdate=input("Enter the phone number of the customer you wants to update: ")
            message=str(6)+","+name+","+" "+","+" "+","+fieldToBeUpdate
                #updateCustomerPhone()
        elif userInput==7:
            message=str(7)
                #printReport()
        elif userInput==8:
            message=str(8)
                #write()
            flag=0
            #break
        else:
            print("Enter a valid input between 1 to 8: ")

        #---------------------------------------------
        #message = input(" -> ")  # again take input
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: \n' + data)  # show in terminal
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
