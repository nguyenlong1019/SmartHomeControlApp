from tkinter import *
from PIL import Image, ImageTk

'''
Điều khiển đèn (5 đèn) => 6 button 
Điều khiển quạt (4) => 5 button 
Điều khiển cửa ra vào (4) => 5 button
'''

class SmartHome:
    # static properties
    btn_off = Image.open('./imgs/btn_off.png')
    btn_on = Image.open('./imgs/btn_on.png')
    re_btn_off = btn_off.resize((50,50))
    re_btn_on = btn_on.resize((50,50))

    light_off = Image.open('./imgs/light_off.png')
    light_on = Image.open('./imgs/light_on.png')
    re_light_off = light_off.resize((50,50))
    re_light_on = light_on.resize((50,50))

    fan_off = Image.open('./imgs/fan_off.png').resize((50,50))
    fan_on = Image.open('./imgs/fan_on.png').resize((50,50))

    close_door = Image.open('./imgs/close_door.png').resize((50,50))
    open_door = Image.open('./imgs/open_door.png').resize((50,50))

    humidity = Image.open('./imgs/humidity.png').resize((50,50))
    percentage = Image.open('./imgs/percentage.png').resize((50,50))
    weather = Image.open('./imgs/weather_news.png').resize((50,50))
    cloudy = Image.open('./imgs/cloudy.png').resize((50,50))
    temperature = Image.open('./imgs/hot.png').resize((50,50))
    degree_celsius = Image.open('./imgs/degree_celsius_1.png').resize((50,50))
    location = Image.open('./imgs/placeholder.png').resize((50,50))

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Control Panel')
        self.root.iconbitmap('./imgs/logo.ico')
        # self.root.minsize(700,700)
        self.root.resizable(0, 0)
        self.root.configure(background='#B2EFF1')

        self.__btn_off = ImageTk.PhotoImage(SmartHome.re_btn_off)
        self.__btn_on = ImageTk.PhotoImage(SmartHome.re_btn_on)
        self.__light_off = ImageTk.PhotoImage(SmartHome.re_light_off)
        self.__light_on = ImageTk.PhotoImage(SmartHome.re_light_on)

        self.__fan_off = ImageTk.PhotoImage(SmartHome.fan_off)
        self.__fan_on = ImageTk.PhotoImage(SmartHome.fan_on)
        self.__close_door = ImageTk.PhotoImage(SmartHome.close_door)
        self.__open_door = ImageTk.PhotoImage(SmartHome.open_door)

        self.__humidity = ImageTk.PhotoImage(SmartHome.humidity)
        self.__percentage = ImageTk.PhotoImage(SmartHome.percentage)
        self.__weather = ImageTk.PhotoImage(SmartHome.weather)
        self.__cloudy = ImageTk.PhotoImage(SmartHome.cloudy)
        self.__temperature = ImageTk.PhotoImage(SmartHome.temperature)
        self.__degree_celsius = ImageTk.PhotoImage(SmartHome.degree_celsius)
        self.__location = ImageTk.PhotoImage(SmartHome.location)

        self.__light_btns = ["btn1", "btn2", "btn3", "btn4", "btn5"]
        self.__light_states = ["light1", "light2", "light3", "light4", "light5"]

        self.__fan_btns = ["btn1", "btn2", "btn3", "btn4"]
        self.__fan_states = ["fan1", "fan2", "fan3", "fan4"]

        self.__door_btns = ["btn1", "btn2", "btn3", "btn4"]
        self.__door_states = ["door1", "door2", "door3", "door4"]

    def light_control_interface(self):
        self.__btn_group = LabelFrame(self.root, text='Light Controls', background='#ECBFEA')
        self.__btn_group.grid(row=0, column=0, padx=10, pady=10)

        for i in range(5):
            self.__light_btns[i] = Button(self.__btn_group, image=self.__btn_on, command=lambda idx=i: self.on(idx))
            self.__light_btns[i].grid(row=i, column=0, padx=10, pady=10)
            self.__light_states[i] = Label(self.__btn_group, image=self.__light_off)
            self.__light_states[i].grid(row=i, column=1, padx=10, pady=10)
        
        self.__light_controls = Button(self.__btn_group, image=self.__btn_on, command=self.toggle_light_alls)
        self.__light_controls.grid(row=5, column=0, padx=10, pady=10)
        self.__lighe_imgs = Label(self.__btn_group, image=self.__light_off)
        self.__lighe_imgs.grid(row=5, column=1, padx=10, pady=10)
        self.__light_alls = False

    def fan_control_interface(self):
        self.__fan_group = LabelFrame(self.root, text='Fan Controls', background='#ECBFEA')
        self.__fan_group.grid(row=0, column=1, padx=10, pady=10)

        for i in range(4):
            self.__fan_btns[i] = Button(self.__fan_group, image=self.__btn_on, command=lambda idx=i: self.fan_turn_on(idx))
            self.__fan_btns[i].grid(row=i, column=0, padx=10, pady=10)
            self.__fan_states[i] = Label(self.__fan_group, image=self.__fan_off)
            self.__fan_states[i].grid(row=i, column=1, padx=10, pady=10)

        self.__fan_controls = Button(self.__fan_group, image=self.__btn_on, command=self.toggle_fan_alls)
        self.__fan_controls.grid(row=5, column=0, padx=10, pady=10)
        self.__fan_imgs = Label(self.__fan_group, image=self.__fan_off)
        self.__fan_imgs.grid(row=5, column=1, padx=10, pady=10)
        self.__fan_alls = False

    def door_control_interface(self):
        self.__door_group = LabelFrame(self.root, text='Door Controls', background='#ECBFEA')
        self.__door_group.grid(row=0, column=2, padx=10, pady=10)

        for i in range(4):
            self.__door_btns[i] = Button(self.__door_group, image=self.__btn_on, command=lambda idx=i: self.unlock_door(idx))
            self.__door_btns[i].grid(row=i, column=0, padx=10, pady=10)
            self.__door_states[i] = Label(self.__door_group, image=self.__close_door)
            self.__door_states[i].grid(row=i, column=1, padx=10, pady=10)

        self.__door_controls = Button(self.__door_group, image=self.__btn_on, command=self.toggle_door_alls)
        self.__door_controls.grid(row=5, column=0, padx=10, pady=10)
        self.__door_imgs = Label(self.__door_group, image=self.__close_door)
        self.__door_imgs.grid(row=5, column=1, padx=10, pady=10)
        self.__door_alls = False

    def view_interface(self):
        self.__view_group = LabelFrame(self.root, text='Infomation', background='#ECBFEA')
        self.__view_group.grid(row=0, column=3, padx=10, pady=10)

        self.__weather_img = Label(self.__view_group, image=self.__weather)
        self.__weather_img.grid(row=0, column=0, padx=10, pady=10)
        self.__humidity_lbl = Label(self.__view_group, text="Ha Noi", font=("Arial", 18, "bold"), foreground='#222')
        self.__humidity_lbl.grid(row=0, column=1, padx=10, pady=10)
        self.__cloudy_img = Label(self.__view_group, image=self.__cloudy)
        self.__cloudy_img.grid(row=0, column=2, padx=10, pady=10)

        self.__humidity_img = Label(self.__view_group, image=self.__humidity)
        self.__humidity_img.grid(row=1, column=0, padx=10, pady=10)
        self.__humidity_lbl = Label(self.__view_group, text="78", font=("Arial", 18, "bold"), foreground='#222')
        self.__humidity_lbl.grid(row=1, column=1, padx=10, pady=10)
        self.__percentage_img = Label(self.__view_group, image=self.__percentage)
        self.__percentage_img.grid(row=1, column=2, padx=10, pady=10)


        self.__temperature_img = Label(self.__view_group, image=self.__temperature)
        self.__temperature_img.grid(row=2, column=0, padx=10, pady=10)
        self.__humidity_lbl = Label(self.__view_group, text="26", font=("Arial", 18, "bold"), foreground='#222')
        self.__humidity_lbl.grid(row=2, column=1, padx=10, pady=10)
        self.__degree_celsius_img = Label(self.__view_group, image=self.__degree_celsius)
        self.__degree_celsius_img.grid(row=2, column=2, padx=10, pady=10)
        
    # light on/off method
    def on(self, index):
        self.__light_btns[index].configure(image=self.__btn_off,command=lambda idx=index: self.off(idx))
        self.__light_states[index].configure(image=self.__light_on)
    def off(self, index):
        self.__light_btns[index].configure(image=self.__btn_on, command=lambda idx=index: self.on(idx))
        self.__light_states[index].configure(image=self.__light_off)

    def toggle_light_alls(self):
        if self.__light_alls:
            for i in range(5):
                self.__light_btns[i].configure(image=self.__btn_on, command=lambda idx=i: self.on(idx))
                self.__light_states[i].configure(image=self.__light_off)
            self.__light_controls.configure(image=self.__btn_on, command=self.toggle_light_alls)
            self.__lighe_imgs.configure(image=self.__light_off)
            self.__light_alls = False
            return
        else:
            for i in range(5):
                self.__light_btns[i].configure(image=self.__btn_off, command=lambda idx=i: self.off(idx))
                self.__light_states[i].configure(image=self.__light_on)
            self.__light_controls.configure(image=self.__btn_off, command=self.toggle_light_alls)
            self.__lighe_imgs.configure(image=self.__light_on)
            self.__light_alls = True
            return
    
    def fan_turn_on(self, index):
        self.__fan_btns[index].configure(image=self.__btn_off,command=lambda idx=index: self.fan_turn_off(idx))
        self.__fan_states[index].configure(image=self.__fan_on)

    def fan_turn_off(self, index):
        self.__fan_btns[index].configure(image=self.__btn_on, command=lambda idx=index: self.fan_turn_on(idx))
        self.__fan_states[index].configure(image=self.__fan_off)

    def toggle_fan_alls(self):
        if self.__fan_alls:
            for i in range(4):
                self.__fan_btns[i].configure(image=self.__btn_on, command=lambda idx=i: self.fan_turn_on(idx))
                self.__fan_states[i].configure(image=self.__fan_off)
            self.__fan_controls.configure(image=self.__btn_on, command=self.toggle_fan_alls)
            self.__fan_imgs.configure(image=self.__fan_off)
            self.__fan_alls = False
            return
        else:
            for i in range(4):
                self.__fan_btns[i].configure(image=self.__btn_off, command=lambda idx=i: self.fan_turn_off(idx))
                self.__fan_states[i].configure(image=self.__fan_on)
            self.__fan_controls.configure(image=self.__btn_off, command=self.toggle_fan_alls)
            self.__fan_imgs.configure(image=self.__fan_on)
            self.__fan_alls = True
            return

    def unlock_door(self, index):
        self.__door_btns[index].configure(image=self.__btn_off,command=lambda idx=index: self.lock_door(idx))
        self.__door_states[index].configure(image=self.__open_door)

    def lock_door(self, index):
        self.__door_btns[index].configure(image=self.__btn_on, command=lambda idx=index: self.unlock_door(idx))
        self.__door_states[index].configure(image=self.__close_door)

    def toggle_door_alls(self):
        if self.__door_alls:
            for i in range(4):
                self.__door_btns[i].configure(image=self.__btn_on, command=lambda idx=i: self.unlock_door(idx))
                self.__door_states[i].configure(image=self.__close_door)
            self.__door_controls.configure(image=self.__btn_on, command=self.toggle_door_alls)
            self.__door_imgs.configure(image=self.__close_door)
            self.__door_alls = False
            return
        else:
            for i in range(4):
                self.__door_btns[i].configure(image=self.__btn_off, command=lambda idx=i: self.lock_door(idx))
                self.__door_states[i].configure(image=self.__open_door)
            self.__door_controls.configure(image=self.__btn_off, command=self.toggle_door_alls)
            self.__door_imgs.configure(image=self.__open_door)
            self.__door_alls = True
            return

smartHome = SmartHome()
smartHome.light_control_interface()
smartHome.fan_control_interface()
smartHome.door_control_interface()
smartHome.view_interface()
smartHome.root.mainloop()