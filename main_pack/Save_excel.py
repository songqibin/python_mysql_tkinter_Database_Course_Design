import xlwt
from tkinter import messagebox
def save_execel(curs,tablename):
    sql='select * from '+tablename
    curs.execute(sql)
    rows = curs.fetchall()  # 获取所有数据
#二、初始化excel文件
    w=xlwt.Workbook(encoding='utf-8')
    style=xlwt.XFStyle()#初始化样式
    font=xlwt.Font()#创建字体样式
    font.name="微软雅黑"
    style.font=font#把字体添加到样式中
    if tablename=="administration":
        ws = w.add_sheet("用户信息", cell_overwrite_ok=True)
        # 三、把数据写入excel
        '''创建excel的列名'''
        title = "用户ID,用户名,用户工资,密码,修理数量"
        title = title.split(",")
    elif tablename=="car_master":
        ws = w.add_sheet("车主信息", cell_overwrite_ok=True)
        # 三、把数据写入excel
        '''创建excel的列名'''
        title = "车主ID,车主名,手机号码,车辆类型,负责人员"
        title = title.split(",")
    elif tablename=="part":
        ws = w.add_sheet("零件信息", cell_overwrite_ok=True)
        # 三、把数据写入excel
        '''创建excel的列名'''
        title = "零件编号,零件名称,零件价格,剩余数量,生产地区"
        title = title.split(",")
    else:
        ws = w.add_sheet("修理信息", cell_overwrite_ok=True)
        # 三、把数据写入excel
        '''创建excel的列名'''
        title = "事件编号,车主姓名,修理价格,经手员工,所用零件"
        title = title.split(",")



    '''#使用循环写入数据'''
    for i in range(len(title)):
        ws.write(0, i, title[i], style)
    # 开始写入数据
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            if row[j]:
                item = row[j]
                ws.write(i + 1, j, item, style)
    path='./'+tablename+".xls"
    w.save(path)
    messagebox.showwarning(title="成功", message='信息保存成功，请到本地目录查看！')
