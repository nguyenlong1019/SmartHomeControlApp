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

        self.light_btns = ["btn1", "btn2", "btn3", "btn4", "btn5"]
        self.light_states = ["light1", "light2", "light3", "light4", "light5"]

    def light_control_interface(self):
        self.btn_group = LabelFrame(self.root, text='Light Controls', background='#ECBFEA')
        self.btn_group.grid(row=0, column=0, padx=10, pady=10)

        for i in range(5):
            self.light_btns[i] = Button()
            self.light_states[i] = Label()
            self.light_btns[i] = Button(self.btn_group, image=self.__img_on, command=lambda idx=i: self.on(idx))
            self.light_btns[i].grid(row=i, column=0, padx=10, pady=10)
            self.light_states[i] = Label(self.btn_group, image=self.__light_off)
            self.light_states[i].grid(row=i, column=1, padx=10, pady=10)

    def fan_control_interface(self):
        pass
    def door_control_interface(self):
        pass
    def view_interface(self):
        pass
    def on(self, index):
        # print(type(self.light_btns[index]))
        self.light_btns[index].configure(image=self.__img_off,command=lambda idx=index: self.off(idx)) # lỗi do truyền self.off[idx]
        self.light_states[index].configure(image=self.__light_on)
    def off(self, index):
        # print(type(self.light_btns[index]))
        self.light_btns[index].configure(image=self.__img_on, command=lambda idx=index: self.on(idx))
        self.light_states[index].configure(image=self.__light_off)
        
smartHome = SmartHome()
smartHome.light_control_interface()
smartHome.root.mainloop()