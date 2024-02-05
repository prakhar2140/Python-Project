from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import random,os,tempfile
import sqlite3

conn = sqlite3.connect('bills.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS bills (bill_no INTEGER PRIMARY KEY, customer_name TEXT, customer_phone TEXT, customer_email TEXT, order_items TEXT, total_price REAL)''')

root = Tk()
root.title("Canteen_Management_System")
root.iconbitmap('./img/Restaurant-Chef-Icon-PNG-Transparent-Background_-Free-Download-_13712-FreeIconsPNG.ico')
global c_name,c_phon,c_email
c_name = StringVar()
c_phon = StringVar()
bill_no = StringVar()
z = random.randint(1000, 9999)
bill_no.set(z)
c_email = StringVar()
prices = IntVar()
total = StringVar()

bg_img = PhotoImage(file="./img/main_frame.png")
bg = Label(root, image=bg_img)
bg.pack()
colour1 = '#0a0b0c'
colour2 = '#f5267b'
colour3 = '#ff3d8d'
colour4 = 'BLACK'
colour5 = '#FFEBCD'

my_img1 = ImageTk.PhotoImage(Image.open("./img/icons8-home-64.png"))
my_img2 = ImageTk.PhotoImage(Image.open("./img/icons8-order-48.png"))
my_img3 = ImageTk.PhotoImage(Image.open("./img/icons8-bill-64.png"))
my_img4 = ImageTk.PhotoImage(Image.open("./img/save-32.png"))
my_img5 = ImageTk.PhotoImage(Image.open("./img/icons8-notification-64.png"))
my_img6 = ImageTk.PhotoImage(Image.open("./img/icons8-about-50.png"))
my_img7 = ImageTk.PhotoImage(Image.open("./img/icons8-exit-30.png"))

def save_bill_to_file():
    bill_file = tempfile.NamedTemporaryFile(delete=False) 
    bill_file.write(text.get("1.0", "end-1c").encode()) 
    bill_file.seek(0) 
    os.startfile(bill_file.name)

def indicate(lb, page):
    hide_indicator()
    lb.config(bg="yellow")
    delete_pages()
    page()

def submit_click():
    text = Text()
    text.config(font=('courier', 15, 'normal'))
    text.config(width=100, height=50)
    text.pack(expand=YES, fill=BOTH)
    text.insert(END,f"\nCustomer Name : {c_name.get()}")
    text.insert(END,f"\nPhone No. : {c_phon.get()}")
    text.insert(END,f"\nEmail-Id. : {c_email.get()}")
        

def hide_indicator():
    home_indicate.config(bg='#2F6C60')
    about_indicate.config(bg='#2F6C60')
    save_indicate.config(bg='#2F6C60')
    order_indicate.config(bg='#2F6C60')
    notification_indicate.config(bg='#2F6C60')
    bill_indicate.config(bg='#2F6C60')
    exit_indicate.config(bg='#2F6C60')


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def home_page():
    def on_clear():
        c_name.set("")
        c_phon.set("")
        c_email.set("")

    def on_submit():        
        if not c_name.get() or not c_phon.get() or not c_email.get():
                messagebox.showerror("Error", "All fields are required!")
                return
        messagebox.showinfo("Success", f"Customer details have been submitted. Name: {c_name.get()}, Mobile No: {c_phon.get()}, Email: {c_email.get()}")
    
    home_frame = Frame(main_frame, width=1310, height=900)
    Btn = Button(home_frame, text='Submit',relief=FLAT, bg="#FFDEFC", activebackground="#F8FBFC", borderwidth=0, cursor="hand2",padx=3,pady=5,font=("Century"),command=on_submit)
    Btn.place(x=650, y=300)
    tbn = Button(home_frame, text='Clear',relief=FLAT, bg="#FFDEFC", activebackground="#F8FBFC", borderwidth=0, cursor="hand2",padx=3,pady=5,font=("Century"), command=on_clear)
    tbn.place(x=550, y=300)
    label_name = Label(home_frame, text="Customer Name:", font=("Century Schoolbook", 20, 'bold'), fg=colour4)
    label_name.place(x=250, y=100)

    entry_name = Entry(home_frame, textvariable=c_name, font=("Century Schoolbook", 15), bg=colour5,width=25)
    entry_name.place(x=500, y=100)

    label_mobile = Label(home_frame, text="Mobile No:", font=("Century Schoolbook", 20, 'bold'), fg=colour4)
    label_mobile.place(x=250, y=150)

    entry_mobile = Entry(home_frame, textvariable=c_phon, font=("Century Schoolbook", 15), bg=colour5,width=25)
    entry_mobile.place(x=500, y=150)

    label_email = Label(home_frame, text="Email:", font=("Century Schoolbook", 20, 'bold'),fg=colour4)
    label_email.place(x=250, y=200)

    entry_email = Entry(home_frame, textvariable=c_email, font=("Century Schoolbook", 15), bg=colour5,width=35)
    entry_email.place(x=500, y=200)

    home_frame.place(x=10, y=10)

def save_page():
    save_frame = Frame(main_frame, bg='pink', width=1310, height=750)

    save_frame.pack()


def order_page():
    selected_items = []  # List to store selected items

    order_frame = Frame(main_frame, width=1638, height=930,bg="#69D1A8")

    def get_selected_value():
        selected_items.clear()  # Clear the list before updating
        for item_var, item_name in zip(item_vars, menu_items):
            if item_var.get():
                selected_items.append((item_name, menu_prices[item_name]))
        return selected_items

    Btngenerate_bill = Button(order_frame, text='Generate Bill', command=lambda: indicate(bill_indicate, lambda: bill_page(get_selected_value())),
                              relief=FLAT, bg="#A19F28", activebackground="#ba90c6", borderwidth=0, cursor="hand2",padx=3,pady=5,font="Harrington")
    Btngenerate_bill.place(x=950, y=680)

    menu_items = [
             "Aloo Parathe", "Chicken Paratha", "Paneer Paratha", "Egg Paratha", "Onion Paratha",
        "Butter Toast", "Jam Toast", "Butter Toast", "Veg Sandwich", "Chhole Bhature",
        "Paneer Sandwich", "Chhole Kulche", "Allo Pakoda", "Veg Rice", "Chicken Rice", "Daal Chawal",
        "Chhole Chawal", "Rajma Chawal", "Chicken Roll", "Chicken Thuppa", "Butter Roti",
        "Tawa Roti", "Plain Roti", "Jeera Rice", "Mix veg", "Kadhai Chicken", "Butter Chicken",
        "Chilli Chicken", "Pahaadi Chicken", "Kadhai Panner", "Butter Panner", "Chilli Paneer",
        "Veg-Manchurian", "Chilli Potato", "Plain Rice", "Jeera Rice", "Butter Roti",
        "Tea", "Special Tea", "Cold Coffee", "Black Tea", "Black Coffee", "Lassi", "Cold Drinks",
        "Lemon Tea", "Normal Coffee", "Custard Milk"
    ]
    menu_prices = {
    "Aloo Parathe": 50,
    "Chicken Paratha": 100,
    "Paneer Paratha": 80,
    "Egg Paratha": 60,
    "Onion Paratha": 40,
    "Butter Toast": 30,
    "Jam Toast": 30,
    "Veg Sandwich": 70,
    "Chhole Bhature": 120,
    "Paneer Sandwich": 90,
    "Chhole Kulche": 110,
    "Allo Pakoda": 60,
    "Veg Rice": 100,
    "Chicken Rice": 150,
    "Daal Chawal": 100,
    "Chhole Chawal": 110,
    "Rajma Chawal": 120,
    "Chicken Roll": 80,
    "Chicken Thuppa": 150,
    "Butter Roti": 20,
    "Tawa Roti": 15,
    "Plain Roti": 10,
    "Jeera Rice": 100,
    "Mix veg": 120,
    "Kadhai Chicken": 200,
    "Butter Chicken": 220,
    "Chilli Chicken": 180,
    "Pahaadi Chicken": 250,
    "Kadhai Panner": 180,
    "Butter Panner": 160,
    "Chilli Paneer": 160,
    "Veg-Manchurian": 160,
    "Chilli Potato": 120,
    "Plain Rice": 60,
    "Jeera Rice": 100,
    "Butter Roti": 20,
    "Tea": 20,
    "Special Tea": 30,
    "Cold Coffee": 60,
    "Black Tea": 20,
    "Black Coffee": 40,
    "Lassi": 50,
    "Cold Drinks": 40,
    "Lemon Tea": 30,
    "Normal Coffee": 40,
    "Custard Milk": 60
}


    item_vars = []  # List to store IntVars for Checkbuttons
    row_count = 0
    col_count = 0
    for item_name in menu_items:
        item_var = IntVar()
        item_vars.append(item_var)
        check_button = Checkbutton(order_frame, text=item_name, variable=item_var, font=("Lucida Handwriting", 20), bg="#69D1A8")
        check_button.grid(row=row_count, column=col_count, padx=10, pady=5, sticky=W)
        col_count += 1
        if col_count > 3:
            col_count = 0
            row_count += 1
    order_frame.place(x=0,y=5)


def bill_page(selected_items):
    bill_frame = Frame(main_frame, bg='red', width=1310, height=750)
    global text
    text = Text(bill_frame)
    text.config(font=('courier', 15, 'normal'))
    text.config(width=100, height=50)
    text.pack(expand=YES, fill=BOTH)
    sb=Scrollbar(bill_frame)
    sb.pack(side=RIGHT,fill=Y)
    sb.config(command=text.yview)
    text.insert(END,"                             Welcome To Canteen Management System\n")
    text.insert(END,f"\nBill No. : {bill_no.get()}")
    text.insert(END,f"\nCustomer Name : {c_name.get()}")
    text.insert(END,f"\nPhone No. : {c_phon.get()}")
    text.insert(END,f"\nEmail-Id. : {c_email.get()}")
    text.insert(END,"\n====================================================================================================")
    text.insert(END,"\n     Order                                   Price   \n")
    text.insert(END,"\n====================================================================================================\n")    
    total_price = 0
    for item, price in selected_items:
        text.insert(END, f"- {item}\t\t\t\t\t\t\t{price}-/₹\n")
        total_price += price
    text.insert(END, "\n====================================================================================================")
    text.insert(END, f"\n\t\t\t\t\t\t\tTotal: {total_price}-/₹\n")

    order_items_str = ', '.join(f"{item} - {price}-/₹" for item, price in selected_items)
    c.execute("INSERT INTO bills (bill_no, customer_name, customer_phone, customer_email, order_items, total_price) VALUES (?, ?, ?, ?, ?, ?)",
              (bill_no.get(), c_name.get(), c_phon.get(), c_email.get(), order_items_str, total_price))
    conn.commit()
    sb.config(command=text.yview)

    btn = Button(bill_frame, text="Print_Bill", font=("courier",15), command=save_bill_to_file)
    btn.place(x=700,y=155)
    bill_frame.pack()

def about_page():
    about_frame= Frame(main_frame, bg='Grey',width=1310,height=750)
    b1= Button(main_frame,text="About Page")   
    b1.pack()
    about_frame.pack()   

def notification_page():
    notification_frame= Frame(main_frame, bg='Blue',width=1310,height=750)

    notification_frame.pack()  

# ... Existing code for buttons ...
button_1 = Button(root, text="HOME", fg="black", font=("Arial", 10, 'bold'), pady=10,
                  background=colour2, foreground=colour4, width=150, height=50, highlightthickness=2,
                  highlightcolor="WHITE", activebackground=colour5, cursor='hand2', highlightbackground='black',
                  image=my_img1, compound=LEFT, command=lambda: indicate(home_indicate, home_page))
button_1.place(x=20, y=80)

button_2 = Button(root, text="ORDER", fg="black", font=("arial", 10, 'bold'), pady=10, background=colour2,
                  foreground=colour4, width=150, height=50, highlightthickness=2,
                  highlightcolor="WHITE", activebackground=colour5, cursor='hand2', highlightbackground='black',
                  image=my_img2, compound=LEFT, command=lambda: indicate(about_indicate, order_page))
button_2.place(x=20, y=165)
button_3 = Button(root, text="BILL", fg="black", font=("arial", 10, 'bold'), pady=5, background=colour2,
                  foreground=colour4, width=150, height=50, highlightthickness=2,
                  highlightcolor="WHITE", activebackground=colour5, cursor='hand2', highlightbackground='black',
                  image=my_img3, compound=LEFT, command=lambda: indicate(bill_indicate, lambda: bill_page))
button_3.place(x=20, y=250)
button_4 = Button(root, text="SAVE BILL", fg="black", font=("arial", 10, 'bold'), pady=5, background=colour2,
                  foreground=colour4, width=150, height=50, highlightthickness=2,
                  highlightcolor="WHITE", activebackground=colour5, cursor='hand2', highlightbackground='black',
                  image=my_img4, compound=LEFT, command=lambda: indicate(save_indicate, save_page))
button_4.place(x=20, y=325)

button_5 = Button(root, text="NOTIFICATION", fg="black", font=("arial", 10, 'bold'), pady=5, background=colour2,
                  foreground=colour4, width=150, height=50, highlightthickness=2,
                  highlightcolor="WHITE", activebackground=colour5, cursor='hand2', highlightbackground='black',
                  image=my_img5, compound=LEFT, command=lambda: indicate(order_indicate, notification_page))
button_5.place(x=20, y=400)

button_6 = Button(root, text="ABOUT", fg="black", font=("arial", 10, 'bold'), pady=5, background=colour2,
                  foreground=colour4, width=150, height=50, highlightthickness=2,
                  highlightcolor="WHITE", activebackground=colour5, cursor='hand2', highlightbackground='black',
                  image=my_img6, compound=LEFT, command=lambda: indicate(notification_indicate, about_page))
button_6.place(x=20, y=475)

button_7 = Button(root, text="EXIT", fg="black", font=("arial", 10, 'bold'), pady=2,
                  command=lambda: (exit_indicate, root.quit()), background=colour2, foreground=colour4, width=150,
                  height=50, highlightthickness=2,
                  highlightcolor="WHITE", activebackground=colour5, cursor='hand2', highlightbackground='black',
                  image=my_img7, compound=LEFT)
button_7.place(x=20, y=550)

home_indicate = Label(root, text='', bg=colour2)
home_indicate.place(x=14, y=80, width=7, height=77)
about_indicate = Label(root, text='', bg=colour2)
about_indicate.place(x=14, y=165, width=7, height=77)
bill_indicate = Label(root, text='', bg=colour2)
bill_indicate.place(x=14, y=250, width=7, height=69)
save_indicate = Label(root, text='', bg=colour2)
save_indicate.place(x=14, y=325, width=7, height=67)
order_indicate = Label(root, text='', bg=colour2)
order_indicate.place(x=14, y=400, width=7, height=67)
notification_indicate = Label(root, text='', bg=colour2)
notification_indicate.place(x=14, y=475, width=7, height=67)
exit_indicate = Label(root, text='', bg=colour2)
exit_indicate.place(x=14, y=550, width=7, height=62)
main_frame = Frame(root, width=1310, height=750, borderwidth=5, bd=9) #background="#9681A1")
bg_img1 = PhotoImage(file="./img/home-1.png")
lbl1 = Label(main_frame, image=bg_img1)
lbl1.pack()
main_frame.place(x=210, y=8)
root.mainloop()