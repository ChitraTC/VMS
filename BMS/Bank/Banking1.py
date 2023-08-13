import mysql.connector
mydb=mysql.connector.connect(host="localhost", user='root', password='chitra123')
mycurser=mydb.cursor()
mycurser.execute("Create database if not exists Bank_db1")
mycurser.execute("use Bank_db1")

#create table
mycurser.execute("create table if not exists Bank_Account(Acc_no int AUTO_INCREMENT,Name varchar(50),"
                 "City varchar(50),Mobile_number varchar(15),Balance int(12),primary key(Acc_no))")
mycurser.execute("create table if not exists Transaction(Acc_no int,Amount int(12),Tx_type char(1),"
                 "foreign key(Acc_no) references Bank_Account(Acc_no)) ")

print("Welcome To STAR BANK")
while True:
    print("1.Create Account 2.Deposit Money 3.Withdraw Money 4.View Account Details 5.Close Account 6.Balance Enquiry 7.Exit")
    ch=int(input("Enter your choice:"))
#create new acc
    if ch==1:
        Name=input("Enter your name:")
        City=input("Enter city name:")
        Mobile_number=input("Enter your mobile number:")
        Balance=0
        sql="insert into Bank_Account(Name,City,Mobile_number,Balance)values(%s,%s,%s,%s)"
        val=(Name,City,Mobile_number,Balance)
        mycurser.execute(sql,val)
        mydb.commit()
        mycurser.execute("select * from Bank_Account where Name='"+Name+"'")
        # mydb.commit()
        print("Account is Successfully created!!")
        for i in mycurser:
            print(i)
    #Deposit Money
    elif ch==2:
        Acc_no=input("Enter the account number :")
        dp=int(input("Enter the amount to be deposited :"))
        Tx_type="d"
        mycurser.execute("insert into Transaction values('"+Acc_no+"','"+str(dp)+ "', '"+ Tx_type + "')")
        mydb.commit()
        mycurser.execute("update Bank_Account set Balance=Balance+'"+str(dp)+"'where Acc_no='"+Acc_no+"'")
        mydb.commit()
        print("Rs.",dp,"has been deposited successfully in account number:",Acc_no)
    #Withdraw Money
    elif ch==3:
        Acc_no=input("Enter the account number :")
        wd=int(input("Enter the amount to be withdrawn:"))
        select_Query="Select balance from Bank_Account where Acc_no='"+Acc_no+"'"
        mycurser.execute(select_Query)
        # mydb.commit()
        bal=mycurser.fetchone()[0]
        if wd<bal:
            Tx_type="w"
            mycurser.execute("insert into Transaction values('"+Acc_no+"','"+str(wd)+"','"+Tx_type+"') ")
            mydb.commit()
            mycurser.execute("update Bank_Account set Balance=Balance-'"+str(wd)+"'where Acc_no="+Acc_no+"")
            mydb.commit()
            print("Rs.", wd, "has been withdrawn successfully from account number:", Acc_no)
        else:
            print("Withdrawl Failure!!Insufficient Balance!")
#Display Account Details
    elif ch==4 :
        Acc_no = input("Enter the account number :")
        mycurser.execute("select *from Bank_Account where Acc_no='"+Acc_no+"'")
        #mydb.commit()
        for i in mycurser:
            print(i)
#Close Account
    elif ch==5 :
        Acc_no = input("Enter the account number :")
        mycurser.execute("DELETE FROM Bank_Account where Acc_no='"+Acc_no+"'")

        mydb.commit()

        print("Account Number : ",Acc_no," is successfully closed")

#Balance Enquiry
    elif ch==6 :
        Acc_no = input("Enter the account number :")
        # mycurser.execute("select Balance from Bank_Account where Acc_no='" + Acc_no + "'")

        select_Query = "Select balance from Bank_Account where Acc_no='" + Acc_no + "'"
        mycurser.execute(select_Query)
        # mydb.commit()
        bal = mycurser.fetchone()[0]
        print("Your Balance is :",bal, "Rs")

    else:
        break



