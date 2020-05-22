
import socket
data=""
database={}
def server_program():
    # get the hostname

    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        else:
            receivedDataTuple=data.split(",")
        print("from connected user: " )
        print(receivedDataTuple)

        track=0
        for item in receivedDataTuple:
            if track==0:
                methodID=int(item)
                track+=1
            elif track==1:
                uName=item
                track+=1
            elif track==2:
                uAge=item
                track+=1
            elif track==3:
                uAddress=item
                track+=1
            elif track==4:
                uPhone=item
                track+=1

        if methodID==1:
            msgForClient=findCustomer(uName)
        elif methodID==2:
            msgForClient=addCustomer(uName,uAge,uAddress,uPhone)
        elif methodID==3:
            msgForClient=deleteCustomer(uName)
        elif methodID==4:
            msgForClient=updateCustomerAge(uName,uAge)
        elif methodID==5:
            msgForClient=updateCustomerAddress(uName,uAddress)
        elif methodID==6:
            msgForClient=updateCustomerPhone(uName,uPhone)
        elif methodID==7:
            msgForClient=printReport()
        elif methodID==8:
            msgForClient=write() #save before exit

        data = msgForClient #input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

# ---------------------------------------------------------------
def loadData():
    file1 = open("data.txt","r")
    lines=file1.readlines()#returns a list
    file1.close()
    for line in lines:
        temp =line.split("|")
        i=0
        value=[]#(age,address,phone) a list
        for item in temp:
            if i==0:
                key=item
                i+=1
            elif i==1:
                value.append(item) #adding age
                i+=1
            elif i==2:
                value.append(item) #address
                i+=1
            elif i==3:
                item=item.replace("\n","") #removing \n
                value.append(item) #phone
                i+=1

        database[key]=value


def findCustomer(findCustomerName):
    if findCustomerName not in database:
        return "customer not found"
    else:
        temp=database.get(findCustomerName)
        report=str(findCustomerName)
        for item in temp:
            if item!="":
                report=report+"|"+item
            else:
                report=report+"|  "+item
    return report
        #return "{} {}".format(findCustomerName,database[findCustomerName])


def addCustomer(name,age,address,phone):
    if name not in database:
        # inputLine="{}|{}|{}|{}\n".format(name,age,address,phone)
        # file1 = open("data.txt","a+")
        # file1.write(inputLine)
        # file1.close()
        # loadData()
        value=[]
        value.append(age)
        value.append(address)
        value.append(phone)
        database[name]=value
        return "customer {} age {} address {} phone {} has been added successfully".format(name,age,address,phone)
    else:
        return "Customer already exists"


def deleteCustomer(name):
    if name not in database:
        return "Customer does not exist"
    else:
        del database[name]
        return "Customer {} has been deleted successfully".format(name)


def updateCustomerAge(name,fieldToBeUpdate):
    if name not in database:
        return "Customer does not exist"
    else:
        userDetails=database.get(name)
        i=0
        value=[]
        for item in userDetails:
            if i==0:
                value.append(fieldToBeUpdate) #updating age
                i+=1
            elif i==1:
                value.append(item) #address remain same
                i+=1
            elif i==2:
                value.append(item) #phone remain same
                i+=1
        database[name]=value
        return "Customer {} has been updated with age {} successfully".format(name,fieldToBeUpdate)


def updateCustomerAddress(name,fieldToBeUpdate):
    if name not in database:
        return "Customer does not exist"
    else:
        userDetails=database.get(name)
        i=0
        value=[]
        for item in userDetails:
            if i==0:
                value.append(item) # age remain same
                i+=1
            elif i==1:
                value.append(fieldToBeUpdate) #updating address
                i+=1
            elif i==2:
                value.append(item) #phone remain same
                i+=1
        database[name]=value
        return "Customer {} has been updated with the address {} successfully".format(name,fieldToBeUpdate)


def updateCustomerPhone(name,fieldToBeUpdate):
    if name not in database:
        return "Customer does not exist"
    else:
        userDetails=database.get(name)
        i=0
        value=[]
        for item in userDetails:
            if i==0:
                value.append(item) #age remain same
                i+=1
            elif i==1:
                value.append(item) #address remain same
                i+=1
            elif i==2:
                value.append(fieldToBeUpdate) #updating phone
                i+=1
        database[name]=value
        return "Customer {} has been updated with the phone {} successfully".format(name,fieldToBeUpdate)


def printReport():
    report=""
    subReport=""
    for i in sorted(database.keys()):
        temp=database.get(i)
        subReport=str(i)
        for item in temp:
            if item!="":
                subReport=subReport+"|"+item
            else:
                subReport=subReport+"|  "+item
        subReport=subReport+"\n"
        report=report+subReport
    return report


def write():
    file1 = open("data.txt","w")
    for key,value in database.items():
        i=0;
        age=""
        address=""
        phone=""
        for eachVal in value:
            if i==0:
                age=eachVal
                i+=1
            elif i==1:
                address=eachVal
                i+=1
            elif i==2:
                phone=eachVal
                i+=1
        inputLine="{}|{}|{}|{}\n".format(key,age,address,phone)
        file1.write(inputLine)
    file1.close()
    return "Good bye"




loadData()
if __name__ == '__main__':
    server_program()
