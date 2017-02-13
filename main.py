import tkinter as tk
import platform
import tkinter.messagebox as messagebox
from d_help import *
from tkinter import ttk
from tkinter import *
from con_sql import Sql3
from export_excel import EXport_excel
from tkinter import Tk, StringVar, ttk

class appMain(Frame):
    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        master.minsize(width=500, height=520)
        self.defualt_value=["請選擇"]
        self.grid()
        
        self.createWindow()
    def createWindow(self):
        self.tt = Label(text=" ")
        self.tt.grid(row=0,column=0)
       
        notebook = ttk.Notebook(height=420,width=480)
        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        notebook.add(frame1, text='Frame Data')
        notebook.add(frame2, text='Frame Two')
        notebook.grid(row=1,column=1)
        ##################### frame1 ############################
        self.pline = Label(frame1, text=" ",width=10)
        self.pline.grid(row=0,column=0)

        self.inpnlab = Label(frame1, text=" Product number : ")
        self.inpnlab.grid(row=1,column=0,sticky=W ,pady=5)

        self.inpnlab2 = Label(frame1, text=" Product name : ")
        self.inpnlab2.grid(row=2,column=0,sticky=W ,pady=5)

        self.pninput = Entry(frame1,width=6)
        self.pninput.grid(row=1,column=1 , sticky=W ,pady=5)
        
        self.pninput2 = Entry(frame1,width=20)
        self.pninput2.grid(row=2,column=1 , sticky=W ,pady=5)
        
        self.inpbutton1 = Button(frame1, text="確認", width=8,font=("Courier", 10))
        self.inpbutton1.grid(row=4,column=1 ,pady=5)
        self.inpbutton1['command']=self.add_p_info

        self.outexcelbuton2 = Button(frame1, text="匯出", width=8,font=("Courier", 10))
        self.outexcelbuton2.grid(row=4,column=0 ,pady=5)
        self.outexcelbuton2['command']=self.ex_p_excel

        self.uppntitle = Label(frame1, text=" Update info " , font=("Arial", 25))
        self.uppntitle.grid(row=5,column=0,columnspan=3,sticky=W ,pady=5)

        self.uppnlab = Label(frame1, text=" Product number : ")
        self.uppnlab.grid(row=6,column=0,sticky=W ,pady=5)

        self.uppninput = Entry(frame1,width=6)
        self.uppninput.grid(row=6,column=1 , sticky=W ,pady=5)

        self.uppnlab2 = Label(frame1, text=" Product name : ")
        self.uppnlab2.grid(row=7,column=0,sticky=W ,pady=5)

        self.uppninput2 = Entry(frame1,width=20)
        self.uppninput2.grid(row=7,column=1 , sticky=W ,pady=5)

        self.uppbutton1 = Button(frame1, text="更新", width=8,font=("Courier", 10))
        self.uppbutton1.grid(row=8,column=1 ,pady=5)
        self.uppbutton1['command']=self.up_p_info

        self.delpntitle = Label(frame1, text=" Delete info " , font=("Arial", 25))
        self.delpntitle.grid(row=9,column=0,columnspan=3,sticky=W ,pady=5)

        self.delpnlab2 = Label(frame1, text=" Product name : ")
        self.delpnlab2.grid(row=10,column=0,sticky=W ,pady=5)

        self.delinput = Entry(frame1,width=6)
        self.delinput.grid(row=10,column=1 , sticky=W ,pady=5)

        self.delpbutton1 = Button(frame1, text="刪除", width=8,font=("Courier", 10))
        self.delpbutton1.grid(row=11,column=1 ,pady=5)
        self.delpbutton1['command']=self.del_p_info

        ###################### frame2 ############################
        #self.defualt_value=["請選擇"]

        self.inpbuton2 = Button(frame2, text="確認", width=8,font=("Courier", 10))
        self.inpbuton2.grid(row=6,column=0 ,pady=5)
        self.inpbuton2['command']=self.sayhello  #sayhello

        self.box_value = StringVar()
        self.box = ttk.Combobox(frame2, textvariable=self.box_value, state='readonly')
        self.box['values'] = ('uu', 'iiy', 'da')
        self.box.current(0)
        #self.box.bind("<<ComboboxSelected>>", self.change_box2) ##self.justamethod
        self.box.grid(row=0,column=0, columnspan=3 ,pady=20)

        self.box2_value = StringVar()
        self.box2 = ttk.Combobox(frame2, textvariable=self.box2_value,state='readonly' ,postcommand=self.justamethod ,values=["請選擇"])
        
        self.box2.current(0)
        self.box2.grid(row=1,column=0, columnspan=3 ,pady=5)

        self.standard = Label(frame2, text=" Standard Error : ")
        self.standard.grid(row=2,column=0,sticky=W ,pady=5)

        self.stainput = Entry(frame2,width=6)
        self.stainput.grid(row=2,column=1 , sticky=W ,pady=5)

        #######################################Standard Error###################

    def sayhello(self):
        mes_box=self.box.get()
        messagebox.showinfo("warning",mes_box)
        
    def justamethod (self):
        box2_menu=[]
        mes_box=self.box.get()
        
        cbx = Sql3()
        cbo =cbx.s_sql("select p_name from products where pn_name = '%s'" %(mes_box))
        box2_menu.append("請選擇")
        for coa in cbo:
             box2_menu.append(coa[0])
        cbx.del_con()
        self.box2['values']=box2_menu
        #combobox onchange event
        
    def change_box2(self ,event):
        pass
          
    def add_p_info(self):
        x=Sql3()
        pn_name = self.pninput.get()
        p_name = self.pninput2.get()
        #print("INSERT INTO products (pn_name,p_name) VALUES(%s,%s);" %(pn_name,p_name))
        #x.i_sql("INSERT INTO products ('pn_name','p_name') VALUES('%s','%s');" %(pn_name,p_name))
        a_ok = x.i_sql("INSERT INTO products ('pn_name','p_name') VALUES(?,?)",s_Help.check_str(pn_name),s_Help.check_str(p_name))
        x.del_con()
        if a_ok==True :
            self.pninput.delete(0, END)
            self.pninput2.delete(0, END)
            messagebox.showinfo("alert","新增成功")
        else:
            messagebox.showinfo("warning","錯誤的新增")
        
    def ex_p_excel(self):
        xc = EXport_excel()
        xc.w_excel()
        
    def up_p_info(self):
        ux = Sql3()
        upn_name = self.uppninput.get()
        up_name = self.uppninput2.get()
        ux.u_sql("UPDATE products SET p_name=? where pn_name=?",s_Help.check_str(up_name),s_Help.check_str(upn_name))
        ux.del_con()
        
    def del_p_info(self):
        dx = Sql3()
        del_name=self.delinput.get()
        dx.d_sql("DELETE FROM products WHERE pn_name=?",s_Help.check_str(del_name))
        dx.del_con()
        
if __name__ == '__main__':
   root = Tk() 
   root.wm_title("RPy")
   root.geometry("+150+100")
   app = appMain(master=root)
   root.iconbitmap('PRy.ico')
   app.mainloop()

#s_Help.check_str IS CHECK STR SYMBOL " ' " CHANGE \' FUNCTION
