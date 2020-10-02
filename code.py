from tkinter import *
from tkinter import messagebox
import random,os

class Billing_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x800+0+0")
        bg_color="#074463"
        self.root.title("Billing SOftware Machine By S@TVIK")
        Title=Label(self.root,text="Billing Software",bg=bg_color,font=("times new roman",30,"bold"),bd=20,relief=GROOVE,fg="gold").pack(fill=X,padx=4)
        #===================VARIABLES============================
        #---------COSMETICS-------------
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_gel=IntVar()
        self.hair_spray=IntVar()
        self.lotion=IntVar()
        
        #----------GROCERY-------------
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #-----------COLD DRINKS------------
        self.maza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.thumsup=IntVar()
        self.sprite=IntVar()
        self.limca=IntVar()

        #------------BILLING MENU------------
        self.Cosmetic_price=StringVar()
        self.Grocery_price=StringVar()
        self.Cold_drink_price=StringVar()
        self.Cosmetics_tax=StringVar()
        self.Grocery_tax=StringVar()
        self.Cold_drink_tax=StringVar()

        #------------CUSTOMER DETAILS------------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.Bill_no=StringVar()
        x=random.randint(1000,9999)
        self.Bill_no.set(str(x))


        #=======CUSTOMER DETAILS FRAME==============================
        F1=LabelFrame(self.root,text="Customer Details:",bg=bg_color,fg="white",font=("times new roman",20,"bold"),bd=10,relief=GROOVE,pady=10)
        F1.place(x=4,y=90,relwidth=1)
        
        c_name=Label(F1,text="Customer Name :",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=0,column=0)
        c_name_entry=Entry(F1,width=25,textvariable=self.c_name,font=("lucida",11,"bold"),bd=5).grid(row=0,column=1)

        c_no=Label(F1,text="Contact No. :",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=0,column=2)
        c_no_entry=Entry(F1,width=25,textvariable=self.c_phone,font=("lucida",11,"bold"),bd=5).grid(row=0,column=3)

        bill_no=Label(F1,text="Bill No. :",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=0,column=4)
        bill_no_entry=Entry(F1,width=25,textvariable=self.Bill_no,font=("lucida",11,"bold"),bd=5).grid(row=0,column=5)

        search_btn=Button(F1,text="Search",command=self.search_bill,width=15,bd=7,bg="cadet blue",fg="black",relief=GROOVE,font=("times new roman",11,"bold")).grid(row=0,column=6,padx=30,pady=10)

        #============COSMETICS FRAME=============================
        F2=LabelFrame(self.root,text="Cosmetics:",bg=bg_color,fg="white",font=("times new roman",20,"bold"),bd=10,relief=GROOVE,pady=10)
        F2.place(x=4,y=213,height=450,width=370)

        Bath_soap=Label(F2,text="Bath Soap",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=0,column=0)
        Bath_soap_entry=Entry(F2,width=13,textvariable=self.soap,font=("lucida",11,"bold"),bd=5).grid(row=0,column=1,padx=10,pady=17)

        
        Face_cream=Label(F2,text="Face Cream",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=1,column=0)
        Face_cream_entry=Entry(F2,width=13,textvariable=self.face_cream,font=("lucida",11,"bold"),bd=5).grid(row=1,column=1,padx=10,pady=17)

        
        Face_wash=Label(F2,text="Face Wash",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=2,column=0)
        Face_wash_entry=Entry(F2,width=13,textvariable=self.face_wash,font=("lucida",11,"bold"),bd=5).grid(row=2,column=1,padx=10,pady=17)

        
        Hair_gel=Label(F2,text="Hair Gell",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=3,column=0)
        Hair_gel_entry=Entry(F2,width=13,textvariable=self.hair_gel,font=("lucida",11,"bold"),bd=5).grid(row=3,column=1,padx=10,pady=17)

        
        Hair_spray=Label(F2,text="Hair Spray",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=4,column=0)
        Hair_spray_entry=Entry(F2,width=13,textvariable=self.hair_spray,font=("lucida",11,"bold"),bd=5).grid(row=4,column=1,padx=10,pady=17)
        
        Body_lotion=Label(F2,text="Body Lotion",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=5,column=0)
        Body_lotion_entry=Entry(F2,width=13,textvariable=self.lotion,font=("lucida",11,"bold"),bd=5).grid(row=5,column=1,padx=10,pady=17)

        #====== GROCERY FRAME======================
        F3=LabelFrame(self.root,text="Grocery:",bg=bg_color,fg="white",font=("times new roman",20,"bold"),bd=10,relief=GROOVE,pady=10)
        F3.place(x=378,y=213,height=450,width=372)

        
        Rice=Label(F3,text="Rice",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=0,column=0)
        Rice_entry=Entry(F3,width=13,textvariable=self.rice,font=("lucida",11,"bold"),bd=5).grid(row=0,column=1,padx=10,pady=17)

        
        Food_oil=Label(F3,text="Food Oil",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=1,column=0)
        Food_oil_entry=Entry(F3,width=13,textvariable=self.food_oil,font=("lucida",11,"bold"),bd=5).grid(row=1,column=1,padx=10,pady=17)

        
        Daal=Label(F3,text="Daal",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=2,column=0)
        Daal_entry=Entry(F3,width=13,textvariable=self.daal,font=("lucida",11,"bold"),bd=5).grid(row=2,column=1,padx=10,pady=17)

        
        Wheat=Label(F3,text="Wheat",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=3,column=0)
        Wheat_entry=Entry(F3,width=13,textvariable=self.wheat,font=("lucida",11,"bold"),bd=5).grid(row=3,column=1,padx=10,pady=17)

        
        Sugar=Label(F3,text="Sugar",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=4,column=0)
        Sugar_entry=Entry(F3,width=13,textvariable=self.sugar,font=("lucida",11,"bold"),bd=5).grid(row=4,column=1,padx=10,pady=17)
        
        Tea=Label(F3,text="Tea",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=5,column=0)
        Tea_entry=Entry(F3,width=13,textvariable=self.tea,font=("lucida",11,"bold"),bd=5).grid(row=5,column=1,padx=10,pady=17)

        #======= COLD DRINKS====================================
        F4=LabelFrame(self.root,text="Cold Drinks:",bg=bg_color,fg="white",font=("times new roman",20,"bold"),bd=10,relief=GROOVE,pady=10)
        F4.place(x=754,y=213,height=450,width=370)

        
        Maza=Label(F4,text="Maza",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=0,column=0)
        Maza_entry=Entry(F4,width=13,textvariable=self.maza,font=("lucida",11,"bold"),bd=5).grid(row=0,column=1,padx=10,pady=17)

        
        coke=Label(F4,text="coke",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=1,column=0)
        coke_entry=Entry(F4,width=13,textvariable=self.coke,font=("lucida",11,"bold"),bd=5).grid(row=1,column=1,padx=10,pady=17)

        
        Frooti=Label(F4,text="Frooti",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=2,column=0)
        Frooti_entry=Entry(F4,width=13,textvariable=self.frooti,font=("lucida",11,"bold"),bd=5).grid(row=2,column=1,padx=10,pady=17)

        
        Thumsup=Label(F4,text="Thumsup",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=3,column=0)
        Thumsup_entry=Entry(F4,width=13,textvariable=self.thumsup,font=("lucida",11,"bold"),bd=5).grid(row=3,column=1,padx=10,pady=17)

        
        Sprite=Label(F4,text="Sprite",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=4,column=0)
        Srite_entry=Entry(F4,width=13,textvariable=self.sprite,font=("lucida",11,"bold"),bd=5).grid(row=4,column=1,padx=10,pady=17)
        
        Limca=Label(F4,text="Limca",font=("times new roman",22,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=5,column=0)
        Limca_entry=Entry(F4,width=13,textvariable=self.limca,font=("lucida",11,"bold"),bd=5).grid(row=5,column=1,padx=10,pady=17)

        #==== BILL AREA===================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1128,y=213,height=450,width=416)

        Bill_title=Label(F5,text="BILL AREA",font=("times new roman",25,"bold"),fg="black",bd=5,relief=GROOVE).pack(fill=X)

        #========== SCROLL BAR================================
        scroll=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=============== BILLING MENU==========================
        F6=LabelFrame(self.root,text="Billing Menu:",bg=bg_color,fg="white",font=("times new roman",20,"bold"),bd=8,relief=GROOVE,pady=10)
        F6.place(x=4,y=665,height=130,width=1527)

        cosmetics_price=Label(F6,text="Total Cosmetics Price",font=("times new roman",13,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=0,column=0)
        cosmetics_price_entry=Entry(F6,width=15,textvariable=self.Cosmetic_price,font=("lucida",10,"bold"),bd=3).grid(row=0,column=1)

        
        grocery_price=Label(F6,text="Total Grocery Price",font=("times new roman",13,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=1,column=0)
        grocery_price_entry=Entry(F6,width=15,textvariable=self.Grocery_price,font=("lucida",10,"bold"),bd=3).grid(row=1,column=1)

        
        cold_drink_price=Label(F6,text="Total ColdDrink Price",font=("times new roman",13,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=2,column=0)
        cold_drink_entry=Entry(F6,width=15,textvariable=self.Cold_drink_price,font=("lucida",10,"bold"),bd=3).grid(row=2,column=1)

        
        cosmetics_tax=Label(F6,text="Cosmetics Tax",font=("times new roman",13,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=0,column=2)
        cosmetics_tax_entry=Entry(F6,width=15,textvariable=self.Cosmetics_tax,font=("lucida",10,"bold"),bd=3).grid(row=0,column=3)

        
        grocery_tax=Label(F6,text="Grocery Tax",font=("times new roman",13,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=1,column=2)
        grocery_tax_entry=Entry(F6,width=15,textvariable=self.Grocery_tax,font=("lucida",10,"bold"),bd=3).grid(row=1,column=3)
        
        cold_drink_tax=Label(F6,text="Cold Drink Tax",font=("times new roman",13,"bold"),bg=bg_color,fg="gold",padx=25).grid(row=2,column=2)
        cold_drink_tax_entry=Entry(F6,width=15,textvariable=self.Cold_drink_tax,font=("lucida",10,"bold"),bd=3).grid(row=2,column=3)

        #===============SUB FRAME========================
        mini_frame=Frame(F6,bd=10,height=75,width=800,relief=GROOVE)
        mini_frame.place(x=700,y=0)

        total_btn=Button(mini_frame,text="Total",width=15,bd=7,command=self.Total,relief=GROOVE,font=("times new roman",12,"bold"),bg=bg_color,fg="gold").grid(row=0,column=0,padx=17,pady=7)
        generate_bill_btn=Button(mini_frame,text="Generate Bill",command=self.bill_area,width=15,bd=7,relief=GROOVE,font=("times new roman",12,"bold"),fg="gold",bg=bg_color).grid(row=0,column=1,padx=17,pady=7)
        clear_btn=Button(mini_frame,text="Clear",width=15,bd=7,command=self.clear_data,relief=GROOVE,font=("times new roman",12,"bold"),bg=bg_color,fg="gold").grid(row=0,column=2,padx=17,pady=7)
        exit_btn=Button(mini_frame,text="Exit",width=15,bd=7,command=self.exit,relief=GROOVE,font=("times new roman",12,"bold"),bg=bg_color,fg="gold").grid(row=0,column=3,padx=17,pady=7)
        self.welcome()

    def Total(self):
        #-------COSMETICS PRICE
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*150
        self.c_hg_p=self.hair_gel.get()*100
        self.c_hs_p=self.hair_spray.get()*180
        self.c_l_p=self.lotion.get()*140
        self.total_cosmetics_price=float(
                                        self.c_s_p+
                                        self.c_fc_p+
                                        self.c_fw_p+
                                        self.c_hg_p+
                                        self.c_hs_p+
                                        self.c_l_p
                                        )
        self.Cosmetic_price.set("Rs. "+str(self.total_cosmetics_price))
        self.cos_Total_tax=(int(self.total_cosmetics_price*0.05))
        self.Cosmetics_tax.set("Rs. "+str(self.total_cosmetics_price*0.05))

        #-----------grocery price---------------
        self.g_r_p=self.rice.get()*100
        self.g_f_p=self.food_oil.get()*135
        self.g_d_p=self.daal.get()*120
        self.g_w_p=self.wheat.get()*300
        self.g_s_p=self.sugar.get()*250
        self.g_t_p=self.tea.get()*200
        self.total_grocery_price=float(
                                self.g_r_p+
                                self.g_f_p+
                                self.g_d_p+
                                self.g_w_p+
                                self.g_s_p+
                                self.g_t_p
                                )
        self.Grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_Total_tax=(int(self.total_grocery_price*0.1))
        self.Grocery_tax.set("Rs. "+str(self.total_grocery_price*0.1))

        #---------------- COLD DRINKS PRICE-----------
        self.c_m_p=self.maza.get()*75
        self.c_coke_p=self.coke.get()*90
        self.c_fr_p=self.frooti.get()*120
        self.c_th_p=self.thumsup.get()*100
        self.c_sprite_p=self.sprite.get()*85
        self.c_lim_p=self.limca.get()*90
        self.total_cold_drink_price=float(
                                    self.c_m_p+
                                    self.c_coke_p+
                                    self.c_fr_p+
                                    self.c_th_p+
                                    self.c_sprite_p+
                                    self.c_lim_p
                                    )
        self.Cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.c_Total_tax=(int(self.total_cold_drink_price*0.15))
        self.Cold_drink_tax.set("Rs. "+str(self.total_cold_drink_price*0.15))
    
    def welcome(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\t    WELCOME TO SATVIK STORE\n")
        self.txtarea.insert(END,f"\n Bill Number :  {self.Bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Contact Number :   {self.c_phone.get()}")
        self.txtarea.insert(END,"\n =============================================")
        self.txtarea.insert(END,"\n Product \t\t   QTY \t\t Price")
        self.txtarea.insert(END,"\n =============================================")

    def bill_area(self):
        self.welcome()
        if self.soap.get() !=0:
            self.txtarea.insert(END,f"\n   Bath Soap\t\t   {self.soap.get()} \t\t  {self.c_s_p}\n")
        if self.face_cream.get() !=0:
            self.txtarea.insert(END,f"  Face Cream\t\t   {self.face_cream.get()} \t\t  {self.c_fc_p}\n")
        if self.face_wash.get() !=0:
            self.txtarea.insert(END,f"  Face Wash\t\t   {self.face_wash.get()} \t\t  {self.c_fw_p}\n")
        if self.hair_gel.get() !=0:
            self.txtarea.insert(END,f"  Hair Gell\t\t   {self.hair_gel.get()} \t\t  {self.c_hg_p}\n")
        if self.hair_spray.get() !=0:
            self.txtarea.insert(END,f"  Hair Spray\t\t   {self.hair_spray.get()} \t\t  {self.c_hs_p}\n")
        if self.lotion.get() !=0:
            self.txtarea.insert(END,f"  Lotion\t\t   {self.lotion.get()} \t\t  {self.c_l_p}\n")

        if self.rice.get() !=0:
            self.txtarea.insert(END,f"  Rice\t\t   {self.rice.get()} \t\t  {self.g_r_p}\n")
        if self.food_oil.get() !=0:
            self.txtarea.insert(END,f"  Food Oil\t\t   {self.food_oil.get()} \t\t  {self.g_f_p}\n")
        if self.daal.get() !=0:
            self.txtarea.insert(END,f"  Daal\t\t   {self.daal.get()} \t\t  {self.g_d_p}\n")
        if self.wheat.get() !=0:
            self.txtarea.insert(END,f"  Wheat\t\t   {self.wheat.get()} \t\t  {self.g_w_p}\n")
        if self.sugar.get() !=0:
            self.txtarea.insert(END,f"  Sugar\t\t   {self.sugar.get()} \t\t  {self.g_s_p}\n")
        if self.tea.get() !=0:
            self.txtarea.insert(END,f"  Tea\t\t   {self.tea.get()} \t\t  {self.g_t_p}\n")

        if self.maza.get() !=0:
            self.txtarea.insert(END,f"  Maza\t\t   {self.maza.get()} \t\t  {self.c_m_p}\n")
        if self.coke.get() !=0:
            self.txtarea.insert(END,f"  Coke\t\t   {self.coke.get()} \t\t  {self.c_coke_p}\n")
        if self.frooti.get() !=0:
            self.txtarea.insert(END,f"  Frooti\t\t   {self.frooti.get()} \t\t  {self.c_fr_p}\n")
        if self.thumsup.get() !=0:
            self.txtarea.insert(END,f"  ThumsUp\t\t   {self.thumsup.get()} \t\t  {self.c_th_p}\n")
        if self.limca.get() !=0:
            self.txtarea.insert(END,f"  Limca\t\t   {self.limca.get()} \t\t  {self.c_lim_p}\n")
        if self.sprite.get() !=0:
            self.txtarea.insert(END,f"  Sprite\t\t   {self.sprite.get()} \t\t  {self.c_sprite_p}\n")

        self.txtarea.insert(END,"\n =============================================\n")
        self.txtarea.insert(END,f"\n Cosmetics Tax \t\t\t\t {str(self.total_cosmetics_price*0.05)}\n")
        self.txtarea.insert(END,f" Grocery Tax \t\t\t\t {str(self.total_grocery_price*0.1)}\n")
        self.txtarea.insert(END,f" Cold Drink Tax \t\t\t\t {str(self.total_cold_drink_price*0.15)}\n")
        self.txtarea.insert(END,"\n ---------------------------------------------")
        self.txtarea.insert(END,f"\n Total Bill \t\t\t\t {(int(self.total_cold_drink_price))+(int(self.total_cosmetics_price))+(int(self.total_grocery_price))+(self.cos_Total_tax)+(self.g_Total_tax)+(self.c_Total_tax)}\n")
        self.save_bill()

    def exit(self):
        ans=messagebox.askyesno("Exit","You Really Want To Exit......!!!!!")
        if ans>0:
            root.quit()
    
    def clear_data(self):
        #---------COSMETICS-------------
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.hair_gel.set(0)
        self.hair_spray.set(0)
        self.lotion.set(0)
        
        #----------GROCERY-------------
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)

        #-----------COLD DRINKS------------
        self.maza.set(0)
        self.coke.set(0)
        self.frooti.set(0)
        self.thumsup.set(0)
        self.sprite.set(0)
        self.limca.set(0)

        #------------BILLING MENU------------
        self.Cosmetic_price.set("")
        self.Grocery_price.set("")
        self.Cold_drink_price.set("")
        self.Cosmetics_tax.set("")
        self.Grocery_tax.set("")
        self.Cold_drink_tax.set("")


        #------------CUSTOMER DETAILS------------
        self.c_name.set("")
        self.c_phone.set("")
        self.Bill_no.set("")
        x=random.randint(1000,9999)
        self.Bill_no.set(str(x))
        self.welcome()

    def save_bill(self):
        save=messagebox.askyesno("Save","Do You Want Save This Bill")
        if save>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("Bills/"+str(self.Bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. {self.Bill_no.get()} Saved Successfully.")
        else:
            return
    
    def search_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split(".")[0]==self.Bill_no.get():
                f1=open(f"Bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                    present="yes"
                f1.close()
        if present=="no":
            messagebox.showerror("Error",f"Inavlid Bill No. {self.Bill_no.get()}")

root=Tk()
obj=Billing_App(root)
root.mainloop()
