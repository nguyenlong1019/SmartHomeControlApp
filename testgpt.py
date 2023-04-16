from tkinter import *
from PIL import Image, ImageTk

class SmartHome:
    def __init__(self):
        self.root = Tk()
        self.root.title('Control Panel')
        self.root.minsize(700,700)
        self.root.configure(background='#B2EFF1')
        
        self.light_imgs = []
        self.light_states = []

        for i in range(5):
            img_off = Image.open('off.png')
            img_on = Image.open('on.png')
            re_img_off = img_off.resize((50,50))
            re_img_on = img_on.resize((50,50))
            self.light_imgs.append((ImageTk.PhotoImage(re_img_off), ImageTk.PhotoImage(re_img_on)))
            self.light_states.append(False)

        # self.light_control_interface()
        
    def light_control_interface(self):
        self.btn_group = LabelFrame(self.root, text='Light Controls', background='#ECBFEA')
        self.btn_group.grid(row=0, column=0, padx=10, pady=10)

        for i in range(5):
            self.light_states[i] = False

            btn = Button(self.btn_group, image=self.light_imgs[i][0], command=lambda index=i: self.toggle_light(index))
            btn.grid(row=i, column=0, padx=10, pady=10)

            light = Label(self.btn_group,image=self.__light_off)
            light.grid(row=i, column=1, padx=10, pady=10)

    def toggle_light(self, index):
        self.light_states[index] = not self.light_states[index]

        if self.light_states[index]:
            self.btns[index].configure(image=self.light_imgs[index][1])
            self.lights[index].configure(image=self.__light_on)
        else:
            self.btns[index].configure(image=self.light_imgs[index][0])
            self.lights[index].configure(image=self.__light_off)

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
