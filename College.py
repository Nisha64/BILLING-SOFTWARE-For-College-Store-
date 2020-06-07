from tkinter import*
import math,random,os
from tkinter import messagebox
class Collegestore_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1690x790+0+0")
        self.root.title("Bill")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #========Variables==========
        #============Records============
        self.rg=IntVar()
        self.rn=IntVar()
        self.fg=IntVar()
        self.fn=IntVar()
        #========Other Equipments=====
        self.pn=IntVar()
        self.pl=IntVar()
        self.sc=IntVar()
        self.nb=IntVar()
        self.gp=IntVar()
        self.mp=IntVar()
        self.cp=IntVar()
        self.es=IntVar()
        self.cm=IntVar()
        self.sk=IntVar()
        self.wp=IntVar()
        self.pc=IntVar()
        self.ib=IntVar()
        self.sp=IntVar()
        self.gu=IntVar()
        self.dr=IntVar()
        self.wh=IntVar()
        self.a4=IntVar()
        self.st=IntVar()
        self.ss=IntVar()
        self.fl=IntVar()
        #=========Total Product_rice & Tax Variables==============
        self.m1=StringVar()
        self.m2=StringVar()
        
        self.c1=StringVar()
        self.c2=StringVar()
        #=========Customer=================
        self.c_name=StringVar()
        self.c_ph=StringVar()
        self.billno=StringVar()
        Q=random.randint(1000,9999)
        self.billno.set(str(Q))
        self.search_bill=StringVar()



        
        #===============Customer Details Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=50,relwidth=1)


        c_name_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        c_name_txt=Entry(F1,width=15,textvariable=self.c_name,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        c_ph_lbl=Label(F1,text="Customer Phone No",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        c_ph_txt=Entry(F1,width=15,textvariable=self.c_ph,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)

        billno_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        billno_txt=Entry(F1,width=15,textvariable=self.search_bill,font="ariel 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)

        bill_btn=Button(F1,text="search",command=self.find_bill,width=12,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=15,pady=15)



        #========Records Frame================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Records",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=150,width=350,height=440)

        
        rg_lbl=Label(F2,text="Rough Record(Graph)",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=0,column=0,padx=13,pady=13,sticky="w")
        rg_txt=Entry(F2,width=10,textvariable=self.rg,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=13,pady=13)

        rn_lbl=Label(F2,text="Rough Record",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=2,column=0,padx=13,pady=12,sticky="w")
        rn_txt=Entry(F2,width=10,textvariable=self.rn,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=13,pady=13)
        
        fg_lbl=Label(F2,text="Fair Record(Graph)",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=3,column=0,padx=13,pady=13,sticky="w")
        fg_txt=Entry(F2,width=10,textvariable=self.fg,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=13,pady=13)

        fn_lbl=Label(F2,text="Fair Record",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=4,column=0,padx=13,pady=13,sticky="w")
        fn_txt=Entry(F2,width=10,textvariable=self.fn,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=13,pady=13)


         #========Other Equipments Frame================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Other Equipments",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=350,y=150,width=775,height=440)

        pn_lbl=Label(F3,text="Pen",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=0,column=0,padx=12,pady=12,sticky="w")
        pn_txt=Entry(F3,width=10,textvariable=self.pn,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=12,pady=12)

        pl_lbl=Label(F3,text="Pencil",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=1,column=0,padx=12,pady=12,sticky="w")
        pl_txt=Entry(F3,width=10,textvariable=self.pl,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=12,pady=12)

        sc_lbl=Label(F3,text="Scale",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=2,column=0,padx=8,pady=12,sticky="w")
        sc_txt=Entry(F3,width=10,textvariable=self.sc,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=12,pady=12)

        nb_lbl=Label(F3,text="Note Book",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=3,column=0,padx=12,pady=12,sticky="w")
        nb_txt=Entry(F3,width=10,textvariable=self.nb,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=12,pady=12)

        mp_lbl=Label(F3,text="Marker Pen",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=5,column=0,padx=12,pady=12,sticky="w")
        mp_txt=Entry(F3,width=10,textvariable=self.mp,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=12,pady=12)

        cp_lbl=Label(F3,text="Chart Paper",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=6,column=0,padx=12,pady=12,sticky="w")
        cp_txt=Entry(F3,width=10,textvariable=self.cp,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=12,pady=12)

        gp_lbl=Label(F3,text="Graph Paper",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=4,column=0,padx=12,pady=12,sticky="w")
        gp_txt=Entry(F3,width=10,textvariable=self.gp,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=12,pady=12)

        pc_lbl=Label(F3,text="Pro Circle",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=4,column=5,padx=12,pady=12,sticky="w")
        pc_txt=Entry(F3,width=10,textvariable=self.pc,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=6,padx=12,pady=12)

        es_lbl=Label(F3,text="eraser",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=0,column=5,padx=12,pady=12,sticky="w")
        es_txt=Entry(F3,width=10,textvariable=self.es,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=6,padx=12,pady=12)

        sp_lbl=Label(F3,text="sharpener",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=2,column=5,padx=12,pady=12,sticky="w")
        sp_txt=Entry(F3,width=10,textvariable=self.sp,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=6,padx=12,pady=12)

        a4_lbl=Label(F3,text="A4 Sheet",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=3,column=10,padx=12,pady=12,sticky="w")
        a4_txt=Entry(F3,width=10,textvariable=self.a4,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=11,padx=12,pady=12)

        wh_lbl=Label(F3,text="Whitener",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=2,column=10,padx=12,pady=12,sticky="w")
        wh_txt=Entry(F3,width=10,textvariable=self.wh,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=11,padx=12,pady=12)

        ib_lbl=Label(F3,text="Instrument Box",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=5,column=5,padx=12,pady=12,sticky="w")
        ib_txt=Entry(F3,width=10,textvariable=self.ib,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=6,padx=12,pady=12)

        cm_lbl=Label(F3,text="Compass",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=1,column=5,padx=8,pady=12,sticky="w")
        cm_txt=Entry(F3,width=10,textvariable=self.cm,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=6,padx=12,pady=12)

        sk_lbl=Label(F3,text="Sketch Pen",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=6,column=5,padx=12,pady=12,sticky="w")
        sk_txt=Entry(F3,width=10,textvariable=self.sk,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=6,padx=12,pady=12)

        dr_lbl=Label(F3,text="Drafter",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=1,column=10,padx=12,pady=12,sticky="w")
        dr_txt=Entry(F3,width=10,textvariable=self.dr,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=11,padx=12,pady=12)
        
        ss_lbl=Label(F3,text="Scissors",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=5,column=10,padx=10,pady=12,sticky="w")
        ss_txt=Entry(F3,width=10,textvariable=self.ss,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=11,padx=12,pady=2)
        
        gu_lbl=Label(F3,text="Gum",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=0,column=10,padx=12,pady=12,sticky="w")
        gu_txt=Entry(F3,width=10,textvariable=self.gu,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=11,padx=12,pady=12)     

        st_lbl=Label(F3,text="Stapler",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=4,column=10,padx=8,pady=12,sticky="w")
        st_txt=Entry(F3,width=10,textvariable=self.st,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=11,padx=8,pady=12)

        wp_lbl=Label(F3,text="Writing Pad",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=3,column=5,padx=12,pady=12,sticky="w")
        wp_txt=Entry(F3,width=10,textvariable=self.wp,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=6,padx=12,pady=12)

        fl_lbl=Label(F3,text="File",bg=bg_color,fg="lightgreen",font=("times new roman",13,"bold")).grid(row=6,column=10,padx=12,pady=12,sticky="w")
        fl_txt=Entry(F3,width=10,textvariable=self.fl,font=("times new roman",13,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=11,padx=12,pady=12)




        #=============Bill Area==================
        F4=Frame(self.root,bd=10,relief=GROOVE)
        F4.place(x=1125,y=150,width=415,height=440)
        bill_title=Label(F4,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F4,orient=VERTICAL)
        self.txtarea=Text(F4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #======ButtonFrame======================
        F5=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F5.place(x=0,y=590,relwidth=1,height=211)
        
        m1=Label(F5,text="Total Record Price",bg=bg_color,fg="white",font=("times of new roman",13,"bold")).grid(row=0,column=0,padx=5,pady=25,sticky="w")
        m1_txt=Entry(F5,width=13,textvariable=self.m1,font="ariel 14 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=25)

        m2=Label(F5,text="Total Other Equipment Price",bg=bg_color,fg="white",font=("times of new roman",13,"bold")).grid(row=1,column=0,padx=9,pady=25,sticky="w")
        m2_txt=Entry(F5,width=13,textvariable=self.m2,font="ariel 14 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=25)

         
        c1=Label(F5,text="Record Tax",bg=bg_color,fg="white",font=("times of new roman",13,"bold")).grid(row=0,column=2,padx=10,pady=25,sticky="w")
        c1_txt=Entry(F5,width=13,textvariable=self.c1,font="ariel 14 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=25)

        c1=Label(F5,text="Other Equipment Tax",bg=bg_color,fg="white",font=("times of new roman",13,"bold")).grid(row=1,column=2,padx=9,pady=25,sticky="w")
        c1_txt=Entry(F5,width=13,textvariable=self.c2,font="ariel 14 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=5,pady=25)

        btn_F=Frame(F5,bd=7,relief=GROOVE)
        btn_F.place(x=780,width=728,height=169)
        
        total_btn=Button(btn_F,text="TOTAL",bg="cadetblue",fg="white",pady=15,bd=5,width=15,height=5,command=self.total,font="arial 12 bold").grid(row=0,column=0,padx=6,pady=7)
        Gbill_btn=Button(btn_F,text="GENARATE BILL",command=self.bill_area,bg="cadetblue",fg="white",pady=15,bd=5,width=15,height=5,font="arial 12 bold").grid(row=0,column=1,padx=6,pady=7)
        clear_btn=Button(btn_F,text="CLEAR",command=self.clear_data,bg="cadetblue",fg="white",pady=15,bd=5,width=15,height=5,font="arial 12 bold").grid(row=0,column=2,padx=6,pady=7)
        Exit_btn=Button(btn_F,text="EXIT",command=self.Exit_app,bg="cadetblue",fg="white",pady=15,bd=5,width=15,height=5,font="arial 12 bold").grid(row=0,column=3,padx=6,pady=7)
        self.welcome_bill()
        
    def total(self):
        self.a=self.rg.get()*40
        self.b=self.rn.get()*40
        self.c=self.fg.get()*80
        self.dd=self.fn.get()*80
        self.total_record_price=float(
                                       self.a+
                                       self.b+
                                       self.c+
                                       self.dd
                                      )
        self.m1.set("Rs. "+str(self.total_record_price))
        self.r_tax=round((self.total_record_price*0.02),2)
        self.c1.set("Rs. "+str(self.r_tax))

        self.e=self.pn.get()*5
        self.f=self.pl.get()*5
        self.g=self.sc.get()*5
        self.h=self.nb.get()*40
        self.z=self.gp.get()*2
        self.j=self.mp.get()*10
        self.k=self.cp.get()*5
        self.l=self.es.get()*5
        self.m=self.cm.get()*20
        self.n=self.sp.get()*5
        self.o=self.wp.get()*40
        self.p=self.pc.get()*10
        self.q=self.ib.get()*100
        self.rr=self.sk.get()*20
        self.s=self.gu.get()*5
        self.t=self.dr.get()*600
        self.u=self.wh.get()*25
        self.v=self.a4.get()*.5
        self.w=self.st.get()*50
        self.x=self.ss.get()*20
        self.y=self.fl.get()*20
                                                
                                                
        self.total_other_equipment_price=float(
                                                 self.e+
                                                 self.f+
                                                 self.g+
                                                 self.h+
                                                 self.z+
                                                 self.j+
                                                 self.k+
                                                 self.l+
                                                 self.m+
                                                 self.m+
                                                 self.o+
                                                 self.p+
                                                 self.q+
                                                 self.rr+
                                                 self.s+
                                                 self.t+
                                                 self.u+
                                                 self.v+
                                                 self.w+
                                                 self.x+
                                                 self.y
                                                )
        self.m2.set("Rs. "+str(self.total_other_equipment_price))
        self.o_tax=round((self.total_other_equipment_price*0.02),2)
        self.c2.set("Rs. "+str(self.o_tax))

        self.Total_bill=round((self.total_record_price+self.total_other_equipment_price+self.r_tax+self.o_tax),0)
        

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,f"\t\t COLLEGE STORE")
        self.txtarea.insert(END,f"\n\n Bill Number   : {self.billno.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n phone Number  : {self.c_ph.get()}")
        self.txtarea.insert(END,f"\n =============================================")
        self.txtarea.insert(END,f"\n   Item Name      \t\t\t QTY\t     Price")
        self.txtarea.insert(END,f"\n =============================================")
        
        
    def bill_area(self):
        if self.c_name.get()=="" or self.c_ph.get()=="":
            messagebox.showerror("error","Customer details are must")
        elif self.m1.get()=="Rs. 0.0" and self.m2.get()=="Rs. 0.0" :
            messagebox.showerror("error","No Item purchased")
            
        else:
            self.welcome_bill()
        #=======Records=========
        if self.rg.get()!=0:
            self.txtarea.insert(END,f"\n Rough Record(Graph)\t\t\t {self.rg.get()}\t     {self.a}")
        if self.rn.get()!=0:
            self.txtarea.insert(END,f"\n Rough Record\t\t\t {self.rn.get()}\t     {self.b}")
        if self.fg.get()!=0:
            self.txtarea.insert(END,f"\n Fair Record(Graph)\t\t\t {self.fg.get()}\t     {self.c}")
        if self.fn.get()!=0:
            self.txtarea.insert(END,f"\n Fair Record\t\t\t {self.fn.get()}\t     {self.dd}")
        #=======Other Equipments=======
        if self.pn.get()!=0:
            self.txtarea.insert(END,f"\n Pen\t\t\t {self.pn.get()}\t     {self.e}")
        if self.pl.get()!=0:
            self.txtarea.insert(END,f"\n Pencil\t\t\t {self.pl.get()}\t     {self.f}")
        if self.sc.get()!=0:
            self.txtarea.insert(END,f"\n Scale\t\t\t {self.sc.get()}\t     {self.g}")
        if self.nb.get()!=0:
            self.txtarea.insert(END,f"\n Note Book\t\t\t {self.nb.get()}\t     {self.h}")
        if self.gp.get()!=0:
            self.txtarea.insert(END,f"\n Graph Paper\t\t\t {self.gp.get()}\t     {self.z}")
        if self.mp.get()!=0:
            self.txtarea.insert(END,f"\n Marker Pen\t\t\t {self.mp.get()}\t     {self.j}")
        if self.cp.get()!=0:
            self.txtarea.insert(END,f"\n Chart Paper\t\t\t {self.cp.get()}\t     {self.k}")
        if self.es.get()!=0:
            self.txtarea.insert(END,f"\n Eraser\t\t\t {self.es.get()}\t     {self.l}")
        if self.cm.get()!=0:
            self.txtarea.insert(END,f"\n Compass\t\t\t {self.cm.get()}\t     {self.m}")
        if self.sk.get()!=0:
            self.txtarea.insert(END,f"\n Sharpener\t\t\t {self.sk.get()}\t     {self.n}")
        if self.wp.get()!=0:
            self.txtarea.insert(END,f"\n Writing Pad\t\t\t {self.wp.get()}\t     {self.o}")
        if self.pc.get()!=0:
            self.txtarea.insert(END,f"\n Pro Circle\t\t\t {self.pc.get()}\t     {self.p}")
        if self.ib.get()!=0:
            self.txtarea.insert(END,f"\n Instrument Box\t\t\t {self.ib.get()}\t     {self.q}")
        if self.sp.get()!=0:
            self.txtarea.insert(END,f"\n Sketch Pen\t\t\t {self.sp.get()}\t     {self.rr}")
        if self.gu.get()!=0:
            self.txtarea.insert(END,f"\n Gum\t\t\t {self.gu.get()}\t     {self.s}")
        if self.dr.get()!=0:
            self.txtarea.insert(END,f"\n Drafter\t\t\t {self.dr.get()}\t     {self.t}")
        if self.wh.get()!=0:
            self.txtarea.insert(END,f"\n Whitener\t\t\t {self.wh.get()}\t     {self.u}")
        if self.a4.get()!=0:
            self.txtarea.insert(END,f"\n A4 Sheet\t\t\t {self.a4.get()}\t     {self.v}")
        if self.st.get()!=0:
            self.txtarea.insert(END,f"\n Stapler\t\t\t {self.st.get()}\t     {self.w}")
        if self.ss.get()!=0:
            self.txtarea.insert(END,f"\n Scissors\t\t\t {self.ss.get()}\t     {self.x}")
        if self.fl.get()!=0:
            self.txtarea.insert(END,f"\n File\t\t\t {self.fl.get()}\t     {self.y}")

        self.txtarea.insert(END,f"\n ---------------------------------------------")
        if self.c1.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n   GST on Record \t\t\t\t {self.c1.get()}")
        if self.c2.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n   GST on Other Equipment \t\t\t\t {self.c2.get()}")
        self.txtarea.insert(END,f"\n   Total Bill\t\t\t\t Rs. {self.Total_bill}")
        self.txtarea.insert(END,f"\n ---------------------------------------------")
        self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.billno.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.billno.get()}Bill saved Successfully")
        else:
            return
        
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                 self.txtarea.insert(END,d)
                f1.close()
                present="yes"
            if present=="no":
                messagebox.showerror("Error","Invalid Billno")
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really clear to Data?")
        if op>0:
         
            #============Records============
            self.rg.set(0)
            self.rn.set(0)
            self.fg.set(0)
            self.fn.set(0)
            #========Other Equipments=====
            self.pn.set(0)
            self.pl.set(0)
            self.sc.set(0)
            self.nb.set(0)
            self.gp.set(0)
            self.mp.set(0)
            self.cp.set(0)
            self.es.set(0)
            self.cm.set(0)
            self.wp.set(0)
            self.pc.set(0)
            self.ib.set(0)
            self.sp.set(0)
            self.gu.set(0)
            self.dr.set(0)
            self.wh.set(0)
            self.a4.set(0)
            self.st.set(0)
            self.ss.set(0)
            self.fl.set(0)
            #=========Total Product_rice & Tax Variables==============
            self.m1.set("")
            self.m2.set("")
            
            self.c1.set("")
            self.c2.set("")
            #=========Customer=================
            self.c_name.set("")
            self.c_ph.set("")
            self.billno.set("")
            Q=random.randint(1000,9999)
            self.billno.set(str(Q))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to Exit?")
        if op>0:
            self.root.destroy()
         
               
               
                
root=Tk()
obj = Collegestore_App(root)
root.mainloop()

