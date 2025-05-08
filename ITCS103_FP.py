import tkinter as tk
from tkinter import ttk
from tkinter import *

sales= 0.0
revenue=0.0
profit=0.0
expenses=0.0
peso= "₱"


pesos=peso,sales
rpeso=peso,revenue
ppeso=peso,profit
xpeso=peso,expenses




def Sales():
    sales_w=tk.Toplevel(background="green4")
    sales_w.geometry("850x480")
    sales_w.resizable(height= False, width= False)
    sales_w.title("Sales")

    sbg=PhotoImage(file='benta.png')
    tk.Label(sales_w,image=sbg).pack()

    # menu_frame = tk.Frame(sales_w,bg="green4", width=885)
    # menu_frame.pack(padx=5,pady=5, fill=BOTH)

    # tk.Label(menu_frame,text="Sales Overview",foreground="White",bg="green4",font=("Times", 25)).pack(side=LEFT,expand=True,padx=50)
    # tk.Button(menu_frame, text="Home",font=("Times", 15),foreground="green4", bg="white",command=sales_w.destroy).pack(side=RIGHT,expand=True,padx=50)

    # sales_frame = tk.Frame(sales_w, width=890, height=200,bg="green3")
    # sales_frame.pack(padx=5, pady=5)

    # tk.Label(sales_frame, text="Sales", font=("Times", 25),bg="green3",fg="white").place(rely=0,relx=.01)
    # tk.Label(sales_frame, text=pesos,font=("Times",20),fg="white", bg="green3").place(rely=.18,relx=.03)

    # tk.Label(sales_frame, text="Products Sold",font=("Times",25),fg="white", bg="green3").place(rely=0,relx=.52)
    # tk.Label(sales_frame, text="Sinigang na Bubog",font=("Times",15),fg="white", bg="green3").place(rely=.18,relx=.52)


    # profit_frame = tk.Frame(sales_w, width=160, height=200,bg="green3")
    # profit_frame.pack(padx=5, pady=5, side=LEFT)

    # tk.Label(profit_frame, text="Revenue", font=("times", 25),bg="green3",fg="white").place(rely=0,relx=.03)
    # tk.Label(profit_frame, text=rpeso,font=("Times",20),fg="white", bg="green3").place(rely=.18,relx=.03)
    

    # sold_frame = tk.Frame(sales_w, width=160, height=200,bg="green3")
    # sold_frame.pack(padx=5, pady=5, side=LEFT)

    # tk.Label(sold_frame, text="Profit", font=("times", 25),bg="green3",fg="white").place(rely=0,relx=.03)
    # tk.Label(sold_frame, text=ppeso,font=("Times",20),fg="white", bg="green3").place(rely=.18,relx=.03)

    # expenses_frame=Frame(sales_w,width=160, height=200,bg="green3")
    # expenses_frame.pack(padx=5,pady=5,side=RIGHT)

    # tk.Label(expenses_frame, text="Expenses", font=("times", 25),bg="green3",fg="white").place(rely=0,relx=.03)
    # tk.Label(expenses_frame, text=xpeso,font=("Times",20),fg="white", bg="green3").place(rely=.18,relx=.03)

    sales_w.mainloop()



def Products():
    product_w=tk.Toplevel()
    product_w.geometry("850x480")
    product_w.resizable(width=False,height=False)
    product_w.title("Products")

    pbg=PhotoImage(file='prod.png')
    tk.Label(product_w,image=pbg).pack()

    tk.Label(product_w,text="Products Overview",foreground="White",bg="black",font=("arial", 30)).place(rely=.03,relx=.03)
    tk.Button(product_w, text="Home",font=("Times", 15),foreground="green4", bg="white",command=product_w.destroy).place(rely=.85,relx=.83)
    tk.Button(product_w, text="Kapeng\nMatapang",font=("Times", 15),foreground="green4", bg="white").place(rely=.83,relx=.01)


    # prod_frame = tk.Frame(product_w, width=890, height=350,bg="green3")
    # prod_frame.pack(padx=5, pady=5)

    # add_prod_frame=Frame(product_w, width= 300,height=80,bg="green3")
    # add_prod_frame.pack(pady=5)

    # pName=Entry(add_prod_frame,fg="white",bg="green3")
    # pName.insert(0,"Product Name")
    # pName.place(rely=.02,relx=.03)

    # pIM=Entry(add_prod_frame,fg="white",bg="green3")
    # pIM.insert(0,"Materials/Ingredients")
    # pIM.place(rely=.30,relx=.03,height=50)
    
    # pCost=Entry(add_prod_frame,fg="white",bg="green3")
    # pCost.insert(0,"Expenses")
    # pCost.place(rely=.02,relx=.48,width=60)

    # pPrice=Entry(add_prod_frame,fg="white",bg="green3")
    # pPrice.insert(0,"Price")
    # pPrice.place(rely=.02,relx=.75,width=60)

    # add_button=Button(add_prod_frame,text="Add product",fg="white",bg="Green")
    # add_button.place(rely=.30,relx=.45,height=50,width=75)

    # delete=Button(add_prod_frame,text="Delete product",fg="white",bg="Green")
    # delete.place(rely=.30,relx=.72,height=50,width=80)

    product_w.mainloop()


windows=tk.Tk()
windows.geometry("850x480")
windows.resizable(height=False,width=False)
windows.title("Sales Information Software")

home=PhotoImage(file='homepage.png')
tk.Label(windows,image=home).pack()

l1=Label(windows,text="Dashboad",foreground="White",bg="black",font=("arial",30),bd=0)
l1.place(relx=.02,rely=.02)

search=Entry(windows,font=("arial",20),fg="black",bd=0)
search.place(rely=.165,relx=.09,width=200)

tk.Button(windows, text = "Products Overview", width=15,bd=0,fg = "White",bg="blue4",font=("arial",13),command=Products).place(relx=.45,rely=.004)
tk.Button(windows, text = "Sales Overview", width=15,bd=0,fg = "White",bg="medium blue",font=("arial",13),command=Sales).place(relx=.62,rely=.004)
tk.Button(windows, text = "Logout", width=15,bd=0,fg = "White",bg="#3533cd",font=("arial",13),command=Sales).place(relx=.80,rely=.004)


# b2 = Button(pane, text = "Products", fg = "White",bg="Green",command=Prodcts)
# b2.config(font=("Times",30))
# b2.pack(side = RIGHT,expand=True,fill=BOTH)

# b3 = Button(text = "Logout", fg = "White",bg="Green",command=windows.destroy)
# b3.config(font=("Times",30))
# b3.pack(expand=True,fill=BOTH)

windows.mainloop()