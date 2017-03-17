#encoding=utf-8  
__author__ = 'freedom'  
  
from Tkinter import *  
from serial import *  
import ttk
import matplotlib.pyplot as plt
import numpy as np
  
class GUI(Frame):
    global ram
    ram = 0
    def __init__(self,master):  
        frame = Frame(master)  
        frame.pack()
        
        #串口号提示  
        self.lab1 = Label(frame,text = 'Serial Number:COM1')  
        self.lab1.grid(row = 0,column = 0,sticky = W)   
        #波特率选择提示  
        self.lab2 = Label(frame,text = 'Baudrate Set:9600')  
        self.lab2.grid(row = 1,column = 0,sticky = W)  
        #数据位提示
        self.lab3 = Label(frame,text = 'Bytesize:8')
        self.lab3.grid(row = 2,column = 0,sticky = W)
        #校验位提示
        self.lab4 = Label(frame,text = 'Parity:None')
        self.lab4.grid(row = 3,column = 0,sticky = W)
        #停止位提示
        self.lab5 = Label(frame,text = 'Stopbits:2')
        self.lab5.grid(row = 4,column = 0,sticky = W)
        #输出框提示  
        self.lab3 = Label(frame,text = 'Message Show')  
        self.lab3.grid(row = 0,column = 1,sticky = W)  
        #输出框  
        self.show = Text(frame,width = 40,height = 5,wrap = WORD)  
        self.show.grid(row = 1,column = 1,rowspan = 4,sticky = W)  
        #输入框提示  
        self.lab4 = Label(frame,text = 'Input here,please!')  
        self.lab4.grid(row = 5,column = 1,sticky = W)  
        #输入框  
        self.input = Entry(frame,width = 40)  
        self.input.grid(row = 6,column = 1,rowspan = 4,sticky = W)  
        #输入按钮  
        self.button1 = Button(frame,text = "Input",command = self.Submit)  
        self.button1.grid(row = 11,column = 1,sticky = E)  
        #串口开启按钮  
        self.button2 = Button(frame,text = 'Open Serial',command = self.open)  
        self.button2.grid(row = 7,column = 0,sticky = W)  
        #串口关闭按钮  
        self.button3 = Button(frame,text = 'Close Serial',command = self.close)  
        self.button3.grid(row = 10,column = 0,sticky = W)  
        #串口信息提示框  
        self.showSerial = Text(frame,width = 20,height = 2,wrap = WORD)  
        self.showSerial.grid(row = 12,column = 0,sticky = W)  
         
    def Submit(self):  
        context1 = self.input.get()
        print context1
        global ram
        if context1[0] == '@'and context1[1] == 'd':
            textlen = len(context1)
            ddata = int(context1[2:textlen-1])
            ddata = ddata/2
            ddata = str(ddata)
            print ddata
            context1 = '@d'+ddata+'.'
            print 'context1:'+context1
            plt.axis([0,100,0,255])
            plt.ion()
            plt.grid(True)
            for i in range(1000):
                y = ddata
                if i >= ram:
                    plt.scatter(i,self.f(y))
                    #plt.plot(i,self.f(y),'k')
                    ram = i
                    plt.pause(0.02)
                else:
                    plt.scatter(i+ram,self.f(y))
                    #plt.plot(i,self.f(y),'k')
                    plt.pause(0.02)
                    
        n = self.ser.write(context1)
        print n
        #output = self.ser.read(n)  
        #print output
        while 1:
            n = self.ser.inWaiting()
        #    #print n
            output = self.ser.read(n)
        #    output = 'abc'
        #    #self.show.delete(0.0,END)  
            self.show.insert(END,output)  
    def open(self):  
        #串口初始化配置  
        self.ser = Serial(  
            port='COM1',                
            baudrate=9600,          # baud rate  
            bytesize=EIGHTBITS,     # number of databits  
            parity=PARITY_NONE,     # enable parity checking  
            stopbits=STOPBITS_TWO,  # number of stopbits  
            timeout=0,           # set a timeout value, None for waiting forever  
        )  
        if self.ser.isOpen() == True:  
            self.showSerial.delete(0.0,END)  
            self.showSerial.insert(0.0,"Serial has been opened!")        
    def close(self):  
        self.ser.close()  
        if self.ser.isOpen() == False:  
            self.showSerial.delete(0.0,END)  
            self.showSerial.insert(0.0,"Serial has been closed!")
    def hexShow(self, argv):    
        result = ''    
        hLen = len(argv)    
        for i in xrange(hLen):    
            hvol = ord(argv[i])    
            hhex = '%02x'%hvol    
            result += hhex+' '    
        return result
    def f(self,t):
        return t
root = Tk()  
root.title("Serial GUI")  
#root.geometry("3000x4000")  
app = GUI(root)  
root.mainloop()


