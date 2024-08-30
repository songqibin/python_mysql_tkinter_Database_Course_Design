from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from main_pack.Save_excel import save_execel
from image import try_dun as bt

def check(a):
    if type(a)==type(None):
        return 'Null'
    else:
        return a

def fan_check(a):
    if a=='Null' or a=='':
        return None
    else:
        return int(a)

def change(cur,num,name,money,password,fix_num):
    print([name,fan_check(money),password,fan_check(fix_num),int(num)])
    sql='UPDATE administration SET Administration_name=%s ,Administration_money=%s,Administration_password=%s,Administration_fix_num=%s where Administration_num=%s'
    cur.execute(sql,[name,fan_check(money),password,fan_check(fix_num),int(num)])
    messagebox.showwarning(title="成功", message='信息更新成功！')

def input_name(name,cur,treeview):
    if name=="":
        messagebox.showwarning(title="错误", message='请输入信息！')
    else:
        sql="select * from administration where Administration_name like '%"+name+"%'"
        cur.execute(sql)
        n = cur.fetchall()
        print(n)
        messagebox.showwarning(title="正确", message='信息查询成功！')
        for i in range(len(n)):
            treeview.insert("",i,values=(n[i][0],n[i][1],n[i][2],n[i][3],n[i][4]))

def treeview_sort_column(tv, col, reverse):#Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    print(tv.get_children(''))
    l.sort(reverse=reverse)#排序方式
    for index, (val, k) in enumerate(l):#根据排序后索引移动
        tv.move(k, '', index)
        print(k)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))#重写标题，使之成为再点倒序的标题

def administration(Main,cur):
    root, ft, ft1, ft2 = Main.yemian(None)
    frame_new, label_tk = Main.getframe(None, root)
    global photo
    img = Image.open('C:\python数据库课程设计\image\左贴图.jpg')  # 打开图片
    photo = ImageTk.PhotoImage(img)
    Label(frame_new, image=photo).place(x=0, y=0)
    bt.button_fun(root, frame_new,cur,Main)#按钮
    def delete(cur, num, frame):  # 删除函数
        print(num)
        sql = "delete from administration where Administration_num=%s"
        cur.execute(sql, [int(num)])
        messagebox.showwarning(title="成功", message='信息删除成功！')
        frame.destroy()
        win()
    def win():
        frame=Main.Frame_fun(None,root)
        root.title('汽车修理管理系统——人员信息')
        n=cur.execute("select * from Administration")
        n=cur.fetchall()
        print(n)
        num=len(n)#数据量
        LabelList=[]#用户编号列表
        ButtonList=[[i for j in range(2)] for i in range(num)]#按钮列表——二维
        EntryList=[[i for j in range(4)] for i in range(num)]#输入框列表——num行4列
        for i in range(num):
            LabelList.append(i)
            #ButtonList.append(i)
        #创建标题行
        Label(frame, text="用户编号    ",font=ft1,bg='#d3d7d4').grid(row=0,column=1)
        Label(frame, text="用户名称    ",font=ft1,bg='#d3d7d4').grid(row=0,column=2)
        Label(frame, text="用户工资    ",font=ft1,bg='#d3d7d4').grid(row=0,column=3)
        Label(frame, text="用户密码    ",font=ft1,bg='#d3d7d4').grid(row=0,column=4)
        Label(frame, text="修理数量    ",font=ft1,bg='#d3d7d4').grid(row=0,column=5)
        Label(frame, text="具体",font=ft1,bg='#d3d7d4').grid(row=0,column=6)
        Label(frame, text="操作    ", font=ft1, bg='#d3d7d4').grid(row=0, column=7)
        for i in range(num):
            #编号
            LabelList[i]=Label(frame,text=n[i][0],font=ft1,anchor="nw")
            LabelList[i].grid(row=i+1, column=1)
            #输入框
            for j in range(4):
                EntryList[i][j]=Entry(frame, font=ft1, width=11)
                EntryList[i][j].grid(row=1 + i, column=2+j)
                EntryList[i][j].delete(0, "end")
                EntryList[i][j].insert(0,check(n[i][j+1]))
                if j==3:
                    ButtonList[i][0]=Button(frame, text="删除",font=ft2,background="#90d7ec",relief=FLAT,command=lambda f=LabelList[i].cget("text"):delete(cur,f,frame))#删除按钮
                    ButtonList[i][1]=Button(frame, text="修改", font=ft2,background="#90d7ec",relief=FLAT,\
                                            command=lambda f=LabelList[i].cget("text"),fname=EntryList[i][0].get(),fmoney=EntryList[i][1].get(),fpasword=EntryList[i][2].get(),fnum=EntryList[i][3].get()\
                                            :change(cur,f,fname,fmoney,fpasword,fnum)) # 修改按钮
                    ButtonList[i][0].grid(row=1 + i, column=6)
                    ButtonList[i][1].grid(row=1 + i, column=7)
    win()
    frame1 = Main.Frame_fun2(None, root)
    colums = ("用户编号", "用户名称", "用户工资", "用户密码", "修理数量")
    treeview = ttk.Treeview(frame1, height=190, show="headings", columns=colums)
    treeview.column("用户编号", width=100, anchor='center')
    treeview.column("用户名称", width=100, anchor='center')
    treeview.column("用户工资", width=100, anchor='center')
    treeview.column("用户密码", width=100, anchor='center')
    treeview.column("修理数量", width=100, anchor='center')
    treeview.heading('用户编号', text='用户编号')
    treeview.heading('用户名称', text='用户名称')
    treeview.heading('用户工资', text='用户工资')
    treeview.heading('用户密码', text='用户密码')
    treeview.heading('修理数量', text='修理数量')
    treeview.place(x=0, y=0)
    labe1=Label(frame1,text="用户姓名:",font=ft1)
    labe1.place(x=525,y=50)
    entry_next=Entry(frame1,font=ft1)
    entry_next.place(x=640,y=50,width=130)
    button_next=Button(frame1,text="查  询",font=ft2,command=lambda :input_name(entry_next.get(),cur,treeview))
    button_next.place(x=535,y=90,width=230)
    button_next_1=Button(frame1,text="导出数据",font=ft2,command=lambda :save_execel(cur,"administration"))
    button_next_1.place(x=535,y=130,width=230)
    button_next_2=Button(frame1,text="回到主页",font=ft2)
    #button_next_2.place(x=535,y=170,width=230)
    for col in colums:  # 给所有标题加（循环上边的“手工”）
        if col!="用户名称" and col!="用户密码":
            treeview.heading(col, text=col, command=lambda _col=col: treeview_sort_column(treeview, _col, False))

    root.mainloop()