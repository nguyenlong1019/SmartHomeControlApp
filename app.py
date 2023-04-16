from tkinter import *
from PIL import Image, ImageTk

class SmartHome:
    def __init__(self):
        self.root = Tk()
        self.root.title('Control Panel')
        self.root.minsize(700,700)
        # self.root.maxsize(1200,700)
        self.root.configure(background='#B2EFF1')

        img_off = Image.open('off.png') # local variable
        img_on = Image.open('on.png') # local variable
        re_img_off = img_off.resize((50,50))  # local variable
        re_img_on = img_on.resize((50,50)) # local variable

        light_off = Image.open('lamp.png')
        light_on = Image.open('lightbulb.png')
        re_light_off = light_off.resize((50,50))
        re_light_on = light_on.resize((50,50))

        self.__img_off = ImageTk.PhotoImage(re_img_off)  # private
        self.__img_on = ImageTk.PhotoImage(re_img_on) # private
        self.__light_off = ImageTk.PhotoImage(re_light_off)
        self.__light_on = ImageTk.PhotoImage(re_light_on)

    def light_control_interface(self):
        self.btn_group = LabelFrame(self.root, text='Light Controls', background='#ECBFEA')
        self.btn_group.grid(row=0, column=0, padx=10, pady=10)
        self.btn = Button(self.btn_group, image=self.__img_on, command=self.on)
        self.btn.grid(row=0, column=0, padx=10, pady=10)
        self.light = Label(self.btn_group,image=self.__light_off)
        self.light.grid(row=0, column=1, padx=10, pady=10)

        self.btn1 = Button(self.btn_group, image=self.__img_on, command=self.on)
        self.btn1.grid(row=1, column=0, padx=10, pady=10)
        self.light1 = Label(self.btn_group,image=self.__light_off)
        self.light1.grid(row=1, column=1, padx=10, pady=10)

        self.btn2 = Button(self.btn_group, image=self.__img_on, command=self.on)
        self.btn2.grid(row=2, column=0, padx=10, pady=10)
        self.light2 = Label(self.btn_group,image=self.__light_off)
        self.light2.grid(row=2, column=1, padx=10, pady=10)

        self.btn3 = Button(self.btn_group, image=self.__img_on, command=self.on)
        self.btn3.grid(row=3, column=0, padx=10, pady=10)
        self.light3 = Label(self.btn_group,image=self.__light_off)
        self.light3.grid(row=3, column=1, padx=10, pady=10)

        self.btn4 = Button(self.btn_group, image=self.__img_on, command=self.on)
        self.btn4.grid(row=4, column=0, padx=10, pady=10)
        self.light4 = Label(self.btn_group,image=self.__light_off)
        self.light4.grid(row=4, column=1, padx=10, pady=10)
    def fan_control_interface(self):
        pass
    def door_control_interface(self):
        pass
    def view_interface(self):
        pass
    def on(self):
        self.btn.configure(image=self.__img_off,command=self.off)
        self.light.configure(image=self.__light_on)
    def off(self):
        self.btn.configure(image=self.__img_on, command=self.on)
        self.light.configure(image=self.__light_off)
        
smartHome = SmartHome()
smartHome.light_control_interface()
smartHome.root.mainloop()