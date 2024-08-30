import Car_pack.Car_fun as cf
import Staff_pack.staff_fun as stf
import Staff_pack.fix_fun as fi
import Administration_pack.Administration_information as ad
import main_pack.main_python as  ma
from tkinter import *
from PIL import Image, ImageTk

from main_pack.main_python import main2


def button_fun(root,frame,cur,Main):
    # 按钮重绘过程----------------------------------------------------------------------------------
    # ----------------------------------------------------------
    img_log = Image.open("C:\python数据库课程设计\image\log.png")
    global img_log_tk
    img_log_tk = ImageTk.PhotoImage(img_log)
    Button_log = Button(frame, image=img_log_tk, compound=TOP, width=78,
                        height=80, text="系统主页", bd=1, bg="#3fcefe", relief=GROOVE,
                        command=lambda: [root.destroy(), main2(cur)])
    Button_log.place(x=0, y=80)
    img_staff_information = Image.open("C:\python数据库课程设计\image\imformation.png")
    global img_staff_information_tk
    img_staff_information_tk = ImageTk.PhotoImage(img_staff_information)

    img_carmain_information = Image.open("C:\python数据库课程设计\image\Boss.png")
    global img_carmain_information_tk
    img_carmain_information_tk = ImageTk.PhotoImage(img_carmain_information)

    img_carlinjian_information = Image.open("C:\python数据库课程设计\image\零件.png")
    global img_carlinjian_information_tk
    img_carlinjian_information_tk = ImageTk.PhotoImage(img_carlinjian_information)

    img_fix_information = Image.open("C:\python数据库课程设计\image\修理信息.png")
    global img_fix_information_tk
    img_fix_information_tk = ImageTk.PhotoImage(img_fix_information)

    img_tui = Image.open("C:\python数据库课程设计\image\退出.png")
    global img_tui_tk
    img_tui_tk = ImageTk.PhotoImage(img_tui)

    Button_staff_information = Button(frame, image=img_staff_information_tk, compound=TOP, width=78,
                                      height=80, text="人员信息", bd=1, bg="#3fcefe", relief=GROOVE,
                                      command=lambda: [root.destroy(), ad.administration(Main, cur)])
    Button_carmain_information = Button(frame, image=img_carmain_information_tk, compound=TOP, width=78,
                                        height=80, text="车主信息", bd=1, bg="#3fcefe", relief=GROOVE,
                                        command=lambda: [root.destroy(), cf.car_master(Main, cur)])
    Button_carlinjian_information = Button(frame, image=img_carlinjian_information_tk, compound=TOP, width=78,
                                           height=80, text="零件信息", bd=1, bg="#3fcefe", relief=GROOVE
                                           , command=lambda: [root.destroy(), stf.Staff(Main, cur)])
    Button_fix_information = Button(frame, image=img_fix_information_tk, compound=TOP, width=78,
                                    height=80, text="修理信息", bd=1, bg="#3fcefe", relief=GROOVE,
                                    command=lambda: [root.destroy(), fi.Fix_fun(Main, cur)])
    Button_tui = Button(frame, image=img_tui_tk, compound=TOP, width=78,
                                    height=80, text="退出登录", bd=1, bg="#3fcefe", relief=GROOVE,
                                    command=lambda: [root.destroy(), ma.main_pace(cur)])
    Button_staff_information.place(x=0, y=170)
    Button_carmain_information.place(x=0, y=260)
    Button_carlinjian_information.place(x=0, y=350)
    Button_fix_information.place(x=0, y=440)
    Button_tui.place(x=0, y=530)
    # ----------------------------------------------------------
    # 按钮重绘过程----------------------------------------------------------------------------------