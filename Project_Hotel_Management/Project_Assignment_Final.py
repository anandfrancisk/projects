#Hotel Management System

class hotel:
    def __init__(self,rate='',count1=0,count2=0,count3=0,count4=0,count5=1000,name='',add='',checkin='',checkout='',room=101):
        print("\033[1;36m!!!WELCOME TO HOTEl GRAND COURT!!!")
        self.rate=rate
        self.count1=count1
        self.count2=count2
        self.count3=count3
        self.count4=count4
        self.count5=count5
        self.name=name
        self.add=add
        self.checkin=checkin
        self.checkout=checkout
        self.room=room

    def data(self):
        self.name=input("\nEnter your fullname:")
        self.add=input("Enter your address:")
        self.checkin=input("Enter your check-in date:")
        self.checkout=input("Enter your check-out date:")

    def rent(self):
        print("\033[1;34m\n***THE ROOM LIST***\n")
        print("1.Suite Room (INR 5000/- per night)")
        print("2.Deluxe Room costing (INR 3000/- per night)")
        print("3.Premium Room costing (INR 2000/- per night)")
        print("4.Standard Room costing (INR 1000/- per night)")
        num1=int(input("\nEnter the number of your choice:"))
        num2=int(input("Enter the number of nights you will be staying:"))
        if(num1==1):
            print("\n**You have selected a suite room**\n")
            self.count1=5000*num2
        elif(num1==2):
            print("\n**You have selected a deluxe room**\n")
            self.count1=3000*num2
        elif(num1==3):
            print("\n**You have selected a premium room**\n")
            self.count1=2000*num2
        elif(num1==4):
            print("\n**You have selected a standard room**\n")
            self.count1=1000*num2
        else:
            print("!!!Invalid choice!!!")

        print("Your room rent is =",self.count1,"\n")

    def food(self):
        print("\033[1;31m\n***THE RESTAURANT MENU***\n")
        print("1.Breakfast (INR 90/-)")
        print("2.Lunch (INR 110/-)")
        print("3.Dinner (INR 150/-)")
        print("4.Dessert (INR 100/-)")
        print("5.Drinks (INR 50/-)")
        print("6.Exit")

        while(1):
            num3=int(input("\nEnter the number of your choice:"))
            if(num3==1):
                num4=int(input("Enter the quantity:"))
                self.count3=self.count3+(90*num4)
            elif(num3==2):
                num4=int(input("Enter the quantity:"))
                self.count3=self.count3+(110*num4)
            elif(num3==3):
                num4=int(input("Enter the quantity:"))
                self.count3=self.count3+(150*num4)
            elif(num3==4):
                num4=int(input("Enter the quantity:"))
                self.count3=self.count3+(100*num4)
            elif(num3==5):
                num4=int(input("Enter the quantity:"))
                self.count3=self.count3+(50*num4)
            elif(num3==6):
                break;
            else:
                print("!!!Invalid choice!!!")

        print("Total food cost =",self.count3,"\n")

    def display(self):
        print("\033[1;31m\n***HOTEL BILL***\n")
        print("Customer name:",self.name)
        print("Customer address:",self.add)
        print("Check-in date:",self.checkin)
        print("Check-out date:",self.checkout)
        print("Room no:",self.room)
        print("Room rent is:",self.count1)
        print("Food bill is:",self.count3)
        self.rate=self.count1+self.count2+self.count3+self.count4
        print("Total purchase amount is:",self.rate)
        print("Additional service charge is",self.count5)
        print("Grand total is:",self.rate+self.count5)
        self.room+=1

def main():
    obj1=hotel()
    while (1):
        print("\033[1;33m\n1.Enter Customer Data")
        print("2.Calculate Room Rent")
        print("3.Calculate Food Bill")
        print("4.Show Grand Total")
        print("5.Exit")
        count6=int(input("\nEnter your choice:"))
        if(count6==1):
            obj1.data()
        elif(count6==2):
            obj1.rent()
        elif(count6==3):
            obj1.food()
        elif(count6==4):
            obj1.display()
        elif(count6==5):
            quit()
main()