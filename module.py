from tkinter import *
import random # 生成随机数


def tz():
    print('凌菲小姐姐声音好甜')

# 创建窗口
tk =Tk()
# tk.geometry('550x250+300+200')
# 画布大小 以像素为单位 px
canvas = Canvas(tk,width = 400,height = 400)
canvas.pack()

# # 画一条直线
# canvas.create_line(0,0,100,50)
# # 绘制矩形
# canvas.create_rectangle(50,50,100,100)
# # 绘制圆形 extent 角度 359为圆
# canvas.create_arc(10,10,50,30,extent = 359)

# 创建按钮
# button = Button(tk,text = '潭州课堂',command = tz)
# # 显示按钮
# button.pack()

# 绘制多边形 fill 颜色
# canvas.create_polygon(200,10,240,30,150,100,160,120,fill = 'red')

# 颜色列表
myColor = ['red','orange','yellow','green','cyan','blue','purple']

def random_rectangle(width,height,myColor):
    # 随机生成一个0-100以内的数
    x = random.randrange(width) # 6
    y = random.randrange(width)
    x1 = x + random.randrange(height)
    y1 = y + random.randrange(height)
    # dash 虚线 10 10段 绘制矩形
    canvas.create_rectangle(x,y,x1,y1,dash = 10,fill = myColor,outline = myColor,stipple = 'gray12')
    # 绘制直线
    canvas.create_line(x,y,x1,y1,fill = myColor)

# 随机生成200个矩形
for numbers in range(200):
    random_rectangle(300,300,myColor[numbers%7])

# 运行窗口 消息循环
tk.mainloop()

