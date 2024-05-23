from tkinter import *
from tkinter import messagebox

tables = [
    {"id": 1, "capacity": 2, "is_available": False},
    {"id": 2, "capacity": 4, "is_available": False},
    {"id": 3, "capacity": 6, "is_available": False},
    {"id": 4, "capacity": 2, "is_available": True},
    {"id": 5, "capacity": 6, "is_available": False},
    {"id": 6, "capacity": 2, "is_available": False},
    {"id": 7, "capacity": 2, "is_available": False},
    {"id": 8, "capacity": 6, "is_available": True},
    {"id": 9, "capacity": 4, "is_available": False},
    {"id": 10, "capacity": 4, "is_available": False}
]

menu=[
    {"first":{"Home Bread":12,"Fresh Salad":18,"Hummus":16,"French Fries":17}},
    {"main":{"Kebab":24,"Chicken":24,"Steak":113,"Combination":160}},
    {"desserts":{"Malabi":15,"Chocolate Cake":17,"Ice-Cream":8}},
    {"drinks":{"Coca-Cola":12,"Diet-Coke":12,"Mineral-Water":10,"Orange juice":12}}
]

order=[]

check=[]

def check_table():
    global tableNum,avialbleLbl,thankYouBtn
    avialbleLbl=Label(host,text=" ")
    num_of_guests = int(hostEntry.get())
    # בדיקה אם יש שולחן פנוי מתאים
    available_table = False
    for table in tables:
        if table["capacity"] >= num_of_guests and table["is_available"]:
            available_table = True
            table["is_available"]= False
            tableNum = table["id"]
            break
    # הצגת הודעה מתאימה
    if available_table:
        avialbleLbl.config(text=f"please go to table number {tableNum}")
        avialbleLbl.pack(pady=4)
        thankYouBtn=Button(host,text="Thanks !",command=give_menu)
        thankYouBtn.pack()
        return tableNum
    else:
        avialbleLbl.pack_forget()
        thankYouBtn.pack_forget()
        avialbleLbl=Label(host,text="we don`t have an available table right now,\nplease wait.")
        avialbleLbl.pack(pady=4)

def give_menu():
    waiterBtn.place(x=150,y=70)
    global low
    hostessBtn.destroy()
    menuPage=Tk()
    host.destroy()
    menuPage.geometry("350x620+200+15")
    menuPage.config(bg="brown")
    menuLbl=Label(menuPage,text="Menu",font=("David bold",22),bg="brown").pack(pady=4)
    for category in menu:
        category_name = list(category.keys())[0]  # Access the first key (category name) directly
        catLbl = Label(menuPage, text=category_name+" dishes :", font=("Arial bold", 16),bg="brown",fg="white").pack(pady=3)
        for dish in category.values():
            for item in dish.keys():
                dishBtn=Label(menuPage,text=f"{item}:    ₪{dish[item]}",font=("David bold",12),bg="brown")
                dishBtn.pack(pady=3)

    menuPage.mainloop()
        
def call_host():
    global host,hostEntry
    host=Tk()
    host.geometry("320x200+870+100")
    host.title("Hostess")
    hostLbl=Label(host, text="Hello\nWellcome to Oved-Bakfar.\nSeats for how much people ?",font=("Arial",12)).pack()
    hostEntry=Entry(host,font=("Arial",12))
    hostEntry.pack(pady=4)
    checkBtn=Button(host,text="check",bg="brown",command=check_table)
    checkBtn.pack(pady=8)
    host.mainloop()

def showCats():
    breadBtn.pack_forget()
    saladBtn.pack_forget()
    hummusBtn.pack_forget()
    friesBtn.pack_forget()
    backBtn.place_forget()
    
    firstBtn.pack(pady=3)
    
    mainBtn.pack(pady=3)
    
    dessertsBtn.pack(pady=3)
    
    drinksBtn.pack(pady=3)
    
def showCatsMain():
    kebabBtn.pack_forget()
    chickenBtn.pack_forget()
    steakBtn.pack_forget()
    combinationBtn.pack_forget()
    backBtn2.place_forget()
    
    
    firstBtn.pack(pady=3)
    
    mainBtn.pack(pady=3)
    
    dessertsBtn.pack(pady=3)
    
    drinksBtn.pack(pady=3)

def showCatsDrinks():
    cocaBtn.pack_forget()
    dietBtn.pack_forget()
    waterBtn.pack_forget()
    orangeBtn.pack_forget()
    backBtn3.place_forget()
    
    firstBtn.pack(pady=3)
    
    mainBtn.pack(pady=3)
    
    dessertsBtn.pack(pady=3)
    
    drinksBtn.pack(pady=3)

def showCatsDes():
    malabiBtn.pack_forget()
    chocolateBtn.pack_forget()
    ice_creamBtn.pack_forget()
    backBtn3.place_forget()
    
    firstBtn.pack(pady=3)
    
    mainBtn.pack(pady=3)
    
    dessertsBtn.pack(pady=3)
    
    drinksBtn.pack(pady=3)

def showFirst():
    global breadBtn,saladBtn,hummusBtn,friesBtn,backBtn
    firstBtn.pack_forget()
    mainBtn.pack_forget()
    dessertsBtn.pack_forget()
    drinksBtn.pack_forget()

    
    breadBtn = Button(waiter,text="Home Bread",command=lambda: addToOrder("Home Bread"))
    breadBtn.pack()
    saladBtn = Button(waiter,text="fresh salad",command=lambda: addToOrder("Fresh Salad"))
    saladBtn.pack()
    hummusBtn = Button(waiter,text="hummus",command=lambda: addToOrder("Hummus"))
    hummusBtn.pack()
    friesBtn = Button(waiter,text="french fries",command=lambda: addToOrder("French Fries"))
    friesBtn.pack()
    backBtn = Button(waiter,text="back",command=showCats)
    backBtn.place(x=5,y=300)
    
def showMain():
    global kebabBtn,chickenBtn,steakBtn,combinationBtn,backBtn2
    firstBtn.pack_forget()
    mainBtn.pack_forget()
    dessertsBtn.pack_forget()
    drinksBtn.pack_forget()

    
    kebabBtn = Button(waiter,text="Kebab",command=lambda: addToOrder("Kebab"))
    kebabBtn.pack()
    chickenBtn = Button(waiter,text="Chicken",command=lambda: addToOrder("Chicken"))
    chickenBtn.pack()
    steakBtn = Button(waiter,text="Steak",command=lambda: addToOrder("Steak"))
    steakBtn.pack()
    combinationBtn = Button(waiter,text="Combination",command=lambda: addToOrder("Combination"))
    combinationBtn.pack()
    backBtn2 = Button(waiter,text="back",command=showCatsMain)
    backBtn2.place(x=5,y=300)
    
def showDesserts():
    global malabiBtn,chocolateBtn,ice_creamBtn,backBtn3
    firstBtn.pack_forget()
    mainBtn.pack_forget()
    dessertsBtn.pack_forget()
    drinksBtn.pack_forget()

    
    malabiBtn = Button(waiter,text="Malabi",command=lambda: addToOrder("Malabi"))
    malabiBtn.pack()
    chocolateBtn = Button(waiter,text="Chocolate Cake",command=lambda: addToOrder("Chocolate Cake"))
    chocolateBtn.pack()
    ice_creamBtn = Button(waiter,text="Ice-Cream",command=lambda: addToOrder("Ice-Cream"))
    ice_creamBtn.pack()
    backBtn3 = Button(waiter,text="back",command=showCatsDes)
    backBtn3.place(x=5,y=300)
    
def showDrinks():
    global cocaBtn,dietBtn,waterBtn,orangeBtn,backBtn
    firstBtn.pack_forget()
    mainBtn.pack_forget()
    dessertsBtn.pack_forget()
    drinksBtn.pack_forget()
    
    cocaBtn = Button(waiter,text="Coca-Cola",command=lambda: addToOrder("Coca-Cola"))
    cocaBtn.pack()
    dietBtn = Button(waiter,text="Chocolate Cake",command=lambda: addToOrder("Diet-Coke"))
    dietBtn.pack()
    waterBtn = Button(waiter,text="Mineral-Water",command=lambda: addToOrder("Mineral-Water"))
    waterBtn.pack()
    orangeBtn = Button(waiter,text="Orange juice",command=lambda: addToOrder("Orange juice"))
    orangeBtn.pack()
    backBtn3 = Button(waiter,text="back",command=showCatsDrinks)
    backBtn3.place(x=5,y=300)
    
def call_waiter():
    
    global waiter,firstBtn,mainBtn,dessertsBtn,orderTxt,drinksBtn
    waiter=Tk()
    waiter.geometry("350x400+500+150")
    waiter.configure(bg="black")
    waiterLbl=Label(waiter,bg="black",fg="white",text="Wellcome, we glad to have you !").pack()
    
    orderTxt=Text(waiter,height=8,width=17)
    orderTxt.pack(pady=15)
    
    firstBtn = Button(waiter,text="First dishes",command=showFirst)
    firstBtn.pack(pady=3)
    mainBtn = Button(waiter,text="Main dishes",command=showMain)
    mainBtn.pack(pady=3)
    dessertsBtn = Button(waiter,text="Desserts",command=showDesserts)
    dessertsBtn.pack(pady=3)
    drinksBtn = Button(waiter,text="Drinks",command=showDrinks)
    drinksBtn.pack(pady=3)
    doneBtn = Button(waiter,text="Done !",command=createCheck)
    doneBtn.place(x=300,y=300)
    
    
    waiter.mainloop()

def createCheck():
    for ord in order:
        for category in menu:
            for dish in category.values():
                for item in dish.keys():
                        if ord==item:
                            check.append(dish[item])
    checkBtn.place(x=110,y=150)
    waiter.destroy()
    return check,order

def giveCheck():
    global total
    checkWin = Tk()
    checkWin.title("check")
    checkWin.geometry("+550+100")
    checkWin.configure(border=12)
    total = 0

    order_prices = {}

    checkLbl = Label(checkWin,text="check :",font=("Arial bold",22))
    checkLbl.pack(pady=4)
    for price, dish in zip(check, order):
        total += price

        if dish not in order_prices:
            order_prices[dish] = 0

        order_prices[dish] += price

    for dish, price in order_prices.items():
        itemLbl = Label(checkWin, text=f"{dish}  :     {price}$")
        itemLbl.pack()

    totalLbl = Label(checkWin, text=f"Your total price is: {total}$")
    totalLbl.pack(pady=20)

    checkWin.mainloop()


def addToOrder(item_name):
    order.append(item_name)
    orderTxt.delete('1.0', END)  # נקה את הטקסט הנוכחי
    for item in order:
        orderTxt.insert(END, f"{item}\n")


global waiterBtn,hostessBtn
root = Tk()
root.title("Oved-Bakfar")
root.configure(bg="brown")
root.geometry("350x250+500+150")


wellcomeLbl=Label(root,text="Wellcome to Oved-Bakfar !\n we will be with you in a minute",bg="brown",fg="white",font=4)
wellcomeLbl.pack()

hostessBtn=Button(root,text="talk to Hostess",command=call_host)
hostessBtn.place(x=20,y=70)

waiterBtn=Button(root,text="talk to a waiter",command=call_waiter)

checkBtn=Button(root,text="i`m Done! \ngive me check please",command=giveCheck)


root.mainloop()