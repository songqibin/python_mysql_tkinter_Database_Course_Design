import pymysql as sql
import tkinter.font as tf
from tkinter import messagebox
from image import try_dun as bt
from tkinter import *
from PIL import Image, ImageTk
class Main(object):
    username="dasd "
    @staticmethod
    def setname(self,name):
        self.username=name
    @staticmethod
    def getname(self):
        return self.username

    def yemian(self):
        # 窗口主要参数------------------------------------
        root = Tk()  # 创建主窗口
        #root.config(background='#BEE7E9')
        root.resizable(width=False, height=False)
        # 屏幕参数设置
        width = 880
        height = 620
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int(screen_width / 2 - width / 2)
        y = int(screen_height / 2 - height / 2)
        size = '{}x{}+{}+{}'.format(width, height, x, y)
        #
        root.geometry(size)
        # 窗口主要参数------------------------------------
        #规定字体
        ft = tf.Font(family='Fixdsys', size=30, weight=tf.BOLD)  # 定义字体
        ft1 = tf.Font(family='Fixdsys', size=15, weight=tf.BOLD)  # 定义字体
        ft2 = tf.Font(family='Fixdsys', size=10, weight=tf.NORMAL)  # 定义字体
        return root,ft,ft1,ft2

    # 主框架
    def getframe(self,root):
        frame = Frame(root, width=850, height=620)
        frame.place(x=0, y=0)
        global photo
        img = Image.open('C:\python数据库课程设计\image\左贴图.jpg')  # 打开图片
        photo = ImageTk.PhotoImage(img)
        return frame, Label(frame, image=photo).place(x=0, y=0)

    def Frame_fun(self,root):
        #规定窗口内的画布
        # 少了这个就滚动不了
        def _on_mousewheel( event):
            canvas.yview_scroll(-1 * (event.delta / 120), "units")
        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200)

        canvas = Canvas(root)  # 创建画布
        canvas.place(x=85, y=0, height=400, width=800)  # 画布大小，对应着组件的位置

        myscrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)  # 创建滚动条
        myscrollbar.place(x=865, y=0, height=400)  # 滚动条的位置和范围这些
        canvas.configure(yscrollcommand=myscrollbar.set)

        rollFrame = Frame(canvas)  # 在画布上创建frame
        canvas.create_window((0, 0), window=rollFrame, anchor='nw')  # 要用create_window才能跟随画布滚动
        rollFrame.bind("<Configure>", myfunction)
        #rollFrame.bind("<MouseWheel>", _on_mousewheel)

        return rollFrame

    def Frame_fun2(self,root):
        frame=Frame(root,height=200,width=800)
        frame.place(x=85,y=400)
        return frame
    def mysql(self):
        cn=sql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='sqb123',
            db='Car_fix_sys',
            charset='utf8'
        )
        cur=cn.cursor()
        #创建各种表
        #管理员表
        '''
        cur.execute(

               ' create table IF NOT EXISTS Administration ('
               'Administration_num INTEGER primary key AUTOINCREMENT,'
               'Administration_name varchar(10) unique,'
               'Administration_money int,'
               'Administration_password varchar(10) not NULL;'
                ')'
        )
        #车主表
        cur.execute(
                'create table IF NOT EXISTS Car_master_user('
                'Car_master_num INTEGER primary key AUTOINCREMENT,'
                'Car_master_name varchar(10) unique,'
                'Car_master_phone varchar(11) unique,'
                'Car_master_cartype string,'
                'Car_master_user varchar(255) unique,'
                'primary key(Car_master_user,Administration_name)'
                'FOREIGN KEY (Car_master_user) REFERENCES Car_master_user(Car_master_user),'
                'FOREIGN KEY (Administration_name) REFERENCES Administration(Administration)'
                )
        )
        '''
        """
        #零件表
        cur.excute(
        'create table IF NOT EXISTS part('
        'part_num INTEGER primary key AUTOINCREMENT,'
        ‘part_name varchar(255) NOT NULL,’
        'part_money int ,'
        'part_left_num int,'
        'part_start varchar(255);'
        )
        """
        """
        #修理信息表
         cur.excute(
        'create table IF NOT EXISTS fix('
        'fix_num INTEGER primary key AUTOINCREMENT,'
        ‘Car_master_name varchar(255) NOT NULL,’
        'fix_money int ,'
        'fix_user varchar(255),'
        'fix_part varchar(255);'
        'primary key(Car_master_user,Administration_name)'
        'FOREIGN KEY (Car_master_user) REFERENCES Car_master_user(Car_master_user),'
        'FOREIGN KEY (Administration_name) REFERENCES Administration(Administration)'
        )
        """
        #
        return cn,cur

def main2(cur):
    root,ft,ft1,ft2=Main.yemian(None)
    frame,label_tk=Main.getframe(None,root)
    global photo
    img = Image.open('C:\python数据库课程设计\image\左贴图.jpg')  # 打开图片
    photo = ImageTk.PhotoImage(img)
    Label(frame, image=photo).place(x=0, y=0)

    root.title('汽车修理管理系统——')
    lab1 = Label(frame, text='汽车修理管理系统欢迎您！',  font=ft, height=5, width=30)
    #--------------
    lab1.place(x=130,y=10)
    lab2=Label(frame,text="当前用户：SONG",font=ft1,height=3,width=20)
    lab3=Label(frame,text="制作：",font=ft1,height=2,width=20)
    lab4 = Label(frame, text="*进入系统则代表所有操作均由账号本人负责", font=ft2, height=2, width=40)
    lab2.place(x=325,y=280)
    lab3.place(x=325,y=240)
    lab4.place(x=300,y=340)
    bt.button_fun(root,frame,cur,Main)
    root.mainloop()



def checklog(username,password,cur):#登录
   # '{}x{}+{}+{}'.format(width, height, x, y)
    sql_1='select Administration_name from Administration'
    cur.execute(sql_1)
    n=cur.fetchall()
    name=[]
    for i in n:
        name.append(i[0])
    print(name)
    #sql_2='select Administration_password from Administration where Administration_name=“{}”'.format(username)
    sql_2='select * from Administration'
    cur.execute(sql_2)
    n=cur.fetchall()
    name_password=[]
    for i in n:
        if username==i[1]:
            name_password.append(i)
    print(name_password)
    if username not in name:
        return '用户信息不存在，请重新输入'
    elif username in name and password !=name_password[0][3]:
        return '密码错误'
    else :
        return True

def log_in(username,password,cur,root):#登录
   if username=="" and password=="":
       messagebox.showwarning(title="错误提示",message='请输入完整信息！')
   elif checklog(username,password,cur)=='用户信息不存在，请重新输入':
       messagebox.showwarning(title="错误提示", message='用户信息不存在，请重新输入')
   elif checklog(username,password,cur)=='密码错误':
       messagebox.showwarning(title="错误提示", message='密码错误，请重新输入')
   else:
       root.destroy()
       main2(cur)

def checksregister(username,password,cur):#注册
    sql_1='select Administration_name from Administration'
    n=cur.execute(sql_1)
    n=cur.fetchall()
    print(n)
    name=[]
    for i in n:
        name.append(i[0])
    if username in name:
        return False
    else:
        sql_2='insert into Administration(Administration_name,Administration_password)values(%s,%s)'
        cur.execute(sql_2,(username,password))
        return True

def register_in(username,password,cur,root):#注册
    if username == "" or password == "":
        messagebox.showwarning(title="错误提示", message='请输入完整信息！')
    elif checksregister(username,password,cur)==False:
        messagebox.showwarning(title="错误提示", message='已存在该用户，请重新输入！')
    else:
        root.destroy()
        main2(cur)

def main_pace(cur):
    root,ft,ft1,ft2=Main.yemian(None)
    root.title('汽车修理管理系统——')
    frame, label_tk = Main.getframe(None,root)
    lab1 = Label(frame, text='汽车修理管理系统', font=ft, height=5,width=30)
    Label_username = Label(frame, text="用户名：",font=ft1)
    Entry_username = Entry(frame,width=30,relief=RIDGE,bd=1)
    Entry_username.place(x=370,y=302)
    Label_username.place(x=290,y=300)
    Label_password = Label(frame, text="密  码：",font=ft1)
    Entry_password = Entry(frame,width=30,relief=RIDGE,bd=1)
    Label_password.place(x=290,y=350)
    Entry_password.place(x=370,y=352)
    lab1.place(x=130,y=10)
    Button_login = Button(frame, text="登录",font=ft2,width=8,background="#90d7ec",relief=FLAT,
                          command=lambda :[log_in(Entry_username.get(),Entry_password.get(),cur,root)])
    Button_login.place(x=330,y=390)
    Button_cancer = Button(frame, text="注册",font=ft2,width=8,background="#90d7ec",relief=FLAT,
                           command=lambda :[register_in(Entry_username.get(),Entry_password.get(),cur,root)])
    Button_cancer.place(x=480,y=390)
    img_log=Image.open("C:\python数据库课程设计\image\log.png")
    global img_log_tk
    img_log_tk=ImageTk.PhotoImage(img_log)
    Button_log = Button(frame,image=img_log_tk,compound=TOP,width=78,height=80,text="进入系统",bd=1,bg="#3fcefe",relief=GROOVE)
    Button_log.place(x=0,y=80)
    #用户图片
    img_user=Image.open(r"C:\python数据库课程设计\image\tk_user.png")
    global img_user_tk
    img_user_tk=ImageTk.PhotoImage(img_user)
    Label(frame, image=img_user_tk).place(x=180, y=280)
    root.mainloop()

if __name__ == '__main__':
    cn,cur=Main.mysql(None)
    n=cur.execute("select * from Administration")
    n=cur.fetchall()
    main_pace(cur)
    #关闭数据库
    cn.commit()
    cur.close()
    cn.close()