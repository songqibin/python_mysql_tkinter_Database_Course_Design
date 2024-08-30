from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import Image, ImageTk

from main_pack.Save_excel import save_execel
from image import try_dun as bt


def treeview_sort_column(tv, col, reverse):#Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    print(tv.get_children(''))
    l.sort(reverse=reverse)#排序方式
    for index, (val, k) in enumerate(l):#根据排序后索引移动
        tv.move(k, '', index)
        print(k)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))#重写标题，使之成为再点倒序的标题

def delButton(tree):#删除条目
    x=tree.get_children()
    for item in x:
        tree.delete(item)

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
    sql='UPDATE fix SET car_master_name=%s ,fix_money=%s,fix_user=%s,fix_part=%s where fix_num=%s'
    cur.execute(sql,[name,int(money),password,fix_num,int(num)])
    messagebox.showwarning(title="成功", message='信息更新成功！')

def input_name(name,cur,treeview):
    if name=="":
        messagebox.showwarning(title="错误", message='请输入信息！')
    else:
        sql="select * from fix where fix_user like '%"+name+"%'"
        cur.execute(sql)
        n = cur.fetchall()
        print(n)
        messagebox.showwarning(title="正确", message='信息查询成功！')
        for i in range(len(n)):
            treeview.insert("",i,values=(n[i][0],n[i][1],n[i][2],n[i][3],n[i][4]))


def Fix_fun(Main,cur):
    root, ft, ft1, ft2 = Main.yemian(None)
    frame_new, label_tk = Main.getframe(None, root)
    global photo
    img = Image.open('C:\python数据库课程设计\image\左贴图.jpg')  # 打开图片
    photo = ImageTk.PhotoImage(img)
    Label(frame_new, image=photo).place(x=0, y=0)
    bt.button_fun(root, frame_new,cur,Main)#按钮
    # 弹窗插入数据页面——新建一个页面
    def win_new():
        root_new = Tk()
        root_new.title("零件信息表——插入数据")
        # frame_new=Frame(root_new,width=300,height=250,bg='#BEE7E9')
        # frame_new.place(x=20)
        # 屏幕参数设置
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int(screen_width / 2 - width / 2)
        y = int(screen_height / 2 - height / 2)
        size = '{}x{}+{}+{}'.format(width, height, x, y)
        #输入框
        labe1_new=Label(root_new,text="车主名字：",font=ft1)
        labe2_new=Label(root_new,text='修理费用：',font=ft1)
        labe3_new=Label(root_new,text="所用零件：",font=ft1)
        #labe4_new = Label(root_new, text="生产地区：", font=ft1)
        labe1_new.place(x=30,y=40)
        labe2_new.place(x=30,y=80)
        labe3_new.place(x=30,y=120)
        #labe4_new.place(x=30,y=160)
        entry1_new=Entry(root_new,width=30)
        entry2_new=Entry(root_new,width=30)
        entry3_new=Entry(root_new,width=30)
        #entry4_new=Entry(root_new,width=30)
        entry1_new.place(x=120,y=40)
        entry2_new.place(x=120,y=80)
        entry3_new.place(x=120,y=120)
       # entry4_new.place(x=120,y=160)
        button1_new=Button(root_new,text="确定",font=ft2,width=15,command=lambda :insert_fun(cur,entry1_new.get(),entry2_new.get(),entry3_new.get(),root_new))
        button2_new=Button(root_new,text="取消",font=ft2,width=15,command=root_new.destroy)
        button1_new.place(x=40,y=160)
        button2_new.place(x=180,y=160)
        root_new.geometry(size)
        # 输入框设置

        root_new.mainloop()
    def delete(cur, num, frame):  # 删除函数
        print(num)
        sql = "delete from part where part_num=%s"
        cur.execute(sql, [int(num)])
        messagebox.showwarning(title="成功", message='信息删除成功！')
        frame.destroy()
        win()

    def insert_fun(cur, name, phnum, cartype,root):

        if name == "" or phnum == "" or cartype == "":
            messagebox.showwarning(title="失败", message='请输入完整信息')
        else:

            sql = "insert into fix(car_master_name,fix_money,fix_user,fix_part)values(%s,%s,%s,%s)"
            cur.execute(sql, [name, phnum, "SONG",cartype])
            messagebox.showwarning(title="成功", message='信息插入成功！')
            root.destroy()
            win()


    def win():
        frame=Main.Frame_fun(None,root)
        root.title('汽车修理管理系统——修理信息')
        cur.execute("select * from fix")
        n=cur.fetchall()
        num=len(n)#数据量
        LabelList=[]#用户编号列表
        ButtonList=[[i for j in range(2)] for i in range(num)]#按钮列表——二维
        EntryList=[[i for j in range(4)] for i in range(num)]#输入框列表——num行4列
        for i in range(num):
            LabelList.append(i)
            #ButtonList.append(i)
        #创建标题行
        Label(frame, text="事件编号    ",font=ft1,bg='#d3d7d4').grid(row=0,column=1)
        Label(frame, text="车主姓名    ",font=ft1,bg='#d3d7d4').grid(row=0,column=2)
        Label(frame, text="修理价格    ",font=ft1,bg='#d3d7d4').grid(row=0,column=3)
        Label(frame, text="经手员工    ",font=ft1,bg='#d3d7d4').grid(row=0,column=4)
        Label(frame, text="所用零件    ",font=ft1,bg='#d3d7d4').grid(row=0,column=5)
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
                                            command=lambda f=LabelList[i].cget("text"),fname=EntryList[i][0].get(),
                                                           fmoney=EntryList[i][1].get(),fpasword=EntryList[i][2].get(),fnum=EntryList[i][3].get()\
                                            :change(cur,f,fname,fmoney,fpasword,fnum)) # 修改按钮
                    ButtonList[i][0].grid(row=1 + i, column=6)
                    ButtonList[i][1].grid(row=1 + i, column=7)
    win()
    frame1 = Main.Frame_fun2(None, root)
    colums = ("事件编号", "车主姓名", "修理价格", "经手员工", "所用零件")
    treeview = ttk.Treeview(frame1, height=190, show="headings", columns=colums)
    treeview.column("事件编号", width=100, anchor='center')
    treeview.column("车主姓名", width=100, anchor='center')
    treeview.column("修理价格", width=100, anchor='center')
    treeview.column("经手员工", width=100, anchor='center')
    treeview.column("所用零件", width=100, anchor='center')
    treeview.heading('事件编号', text='事件编号')
    treeview.heading('车主姓名', text='车主姓名')
    treeview.heading('修理价格', text='修理价格')
    treeview.heading('经手员工', text='经手员工')
    treeview.heading('所用零件', text='所用零件')
    treeview.place(x=0, y=0)
    labe1=Label(frame1,text="经手员工:",font=ft1)
    labe1.place(x=525,y=50)
    entry_next=Entry(frame1,font=ft1)
    entry_next.place(x=640,y=50,width=130)
    button_next=Button(frame1,text="查  询",font=ft2,command=lambda :[delButton(treeview),input_name(entry_next.get(),cur,treeview)])
    button_next.place(x=535,y=90,width=230)
    button_next_1=Button(frame1,text="导出数据",font=ft2,command=lambda :save_execel(cur,"fix"))
    button_next_1.place(x=535,y=130,width=230)
    button_next_2=Button(frame1,text="插入数据",font=ft2,command=win_new)
    button_next_2.place(x=535,y=170,width=230)
    for col in colums:  # 给所有标题加（循环上边的“手工”）
        if col!="车主姓名" and col!="经手员工" and col!="所用零件":
            treeview.heading(col, text=col, command=lambda _col=col: treeview_sort_column(treeview, _col, False))


    root.mainloop()