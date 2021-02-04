import tkinter
from PIL import Image, ImageTk

img_width = 1024 
img_height = 576
blank = 0

#参考にさせていただいたサイト
#https://qiita.com/jedi/items/31ae12f45b560ecca646

class Scribble:
    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y,
                                outline = self.color.get(),
                                width = self.width.get())


    def on_dragged(self, event):
        self.canvas.create_line(self.sx, self.sy, event.x, event.y,
                            fill = self.color.get(),
                            width = self.width.get())
        self.sx = event.x
        self.sy = event.y

    def click1(self,event):
        now_color = self.color.get()
        if now_color =="white":
            now_image = self.dead_white_img 
        elif now_color =="orange":
            now_image =  self.dead_orange_img
        elif now_color =="green":
            now_image = self.dead_green_img
        elif now_color =="yellow":
            now_image = self.dead_yellow_img
        elif now_color =="purple":
            now_image = self.dead_purple_img
        elif now_color =="blue":
            now_image = self.dead_blue_img
        elif now_color =="red":
            now_image = self.dead_red_img
        elif now_color =="pink":
            now_image = self.dead_pink_img
        elif now_color =="brown":
            now_image = self.dead_brown_img
        elif now_color =="black":
            now_image = self.dead_black_img
        elif now_color =="limegreen":
            now_image = self.dead_limegreen_img
        elif now_color =="lightblue":
            now_image = self.dead_lightblue_img

        if self.now_x == self.sx and self.now_y == self.sy:  
            self.now_x += 8
            self.now_y += 8
            self.sx, self.sy = self.now_x, self.now_y
            self.canvas.create_image(self.now_x, self.now_y, image = now_image)    
        else:
            self.canvas.create_image(self.sx, self.sy, image = now_image)
            self.now_x, self.now_y = self.sx, self.sy
            
        
        
    def click2(self,event):
        now_color = self.color.get()
        if now_color =="white":
            now_image = self.white_img
        elif now_color =="orange":
            now_image =  self.orange_img
        elif now_color =="green":
            now_image = self.green_img
        elif now_color =="yellow":
            now_image = self.yellow_img
        elif now_color =="purple":
            now_image = self.purple_img
        elif now_color =="blue":
            now_image = self.blue_img
        elif now_color =="red":
            now_image = self.red_img
        elif now_color =="pink":
            now_image = self.pink_img
        elif now_color =="brown":
            now_image = self.brown_img
        elif now_color =="black":
            now_image = self.black_img
        elif now_color =="limegreen":
            now_image = self.limegreen_img
        elif now_color =="lightblue":
            now_image = self.lightblue_img
        
       
        if self.now_x == self.sx and self.now_y == self.sy:  
            self.now_x += 8
            self.now_y += 8
            self.sx, self.sy = self.now_x, self.now_y
            self.canvas.create_image(self.now_x, self.now_y, image = now_image) 
        else:
            self.canvas.create_image(self.sx, self.sy, image = now_image)
            self.now_x, self.now_y = self.sx, self.sy
            

            
    def click3(self, event):
        now_color = self.color.get()
        if now_color =="white":
            now_image = self.white_img 
        elif now_color =="orange":
            now_image =  self.orange_img
        elif now_color =="green":
            now_image = self.green_img
        elif now_color =="yellow":
            now_image = self.yellow_img
        elif now_color =="purple":
            now_image = self.purple_img
        elif now_color =="blue":
            now_image = self.blue_img
        elif now_color =="red":
            now_image = self.red_img
        elif now_color =="pink":
            now_image = self.pink_img
        elif now_color =="brown":
            now_image = self.brown_img
        elif now_color =="black":
            now_image = self.black_img
        elif now_color =="limegreen":
            now_image = self.limegreen_img
        elif now_color =="lightblue":
            now_image = self.lightblue_img
        self.VScanvas.create_image(event.x, event.y, image = now_image)

    def click4(self, event):
        now_color = self.color.get()
        if now_color =="white":
            now_image = self.white_img 
        elif now_color =="orange":
            now_image =  self.orange_img
        elif now_color =="green":
            now_image = self.green_img
        elif now_color =="yellow":
            now_image = self.yellow_img
        elif now_color =="purple":
            now_image = self.purple_img
        elif now_color =="blue":
            now_image = self.blue_img
        elif now_color =="red":
            now_image = self.red_img
        elif now_color =="pink":
            now_image = self.pink_img
        elif now_color =="brown":
            now_image = self.brown_img
        elif now_color =="black":
            now_image = self.black_img
        elif now_color =="limegreen":
            now_image = self.limegreen_img
        elif now_color =="lightblue":
            now_image = self.lightblue_img
        self.CREWcanvas.create_image(event.x, event.y, image = now_image)

    def click5(self, event):
        now_color = self.color.get()
        if now_color =="white":
            now_image = self.white_img 
        elif now_color =="orange":
            now_image =  self.orange_img
        elif now_color =="green":
            now_image = self.green_img
        elif now_color =="yellow":
            now_image = self.yellow_img
        elif now_color =="purple":
            now_image = self.purple_img
        elif now_color =="blue":
            now_image = self.blue_img
        elif now_color =="red":
            now_image = self.red_img
        elif now_color =="pink":
            now_image = self.pink_img
        elif now_color =="brown":
            now_image = self.brown_img
        elif now_color =="black":
            now_image = self.black_img
        elif now_color =="limegreen":
            now_image = self.limegreen_img
        elif now_color =="lightblue":
            now_image = self.lightblue_img
        self.INPcanvas.create_image(event.x, event.y, image = now_image)


    # 一方矢印
    def click6(self, event):    
        self.VScanvas.create_image(event.x, event.y, image = self.arrow_img)
    
    def click7(self, event):    
        self.CREWcanvas.create_image(event.x, event.y, image = self.arrow_img)
    
    def click8(self, event):    
        self.INPcanvas.create_image(event.x, event.y, image = self.arrow_img)
    
    
    #対抗矢印
    def click9(self, event):    
        self.VScanvas.create_image(event.x, event.y, image = self.arrows_img)
    
    def click10(self, event):    
        self.CREWcanvas.create_image(event.x, event.y, image = self.arrows_img)
    
    def click11(self, event):    
        self.INPcanvas.create_image(event.x, event.y, image = self.arrows_img)

    #各種マーク
    def admin(self, event):    
        if event.x == self.sx and event.y == self.sy:
            self.canvas.create_image(self.sx, self.sy - 30, image = self.admin_img)
        else:
            self.canvas.create_image(event.x, event.y, image = self.admin_img)
    
    def security(self, event):    
        if event.x == self.sx and event.y == self.sy:
            self.canvas.create_image(self.sx, self.sy - 30, image = self.security_img)
        else:
            self.canvas.create_image(event.x, event.y, image = self.security_img)
    
    def report(self, event):    
        if event.x == self.sx and event.y == self.sy:
            self.canvas.create_image(self.sx, self.sy - 30, image = self.report_img)
        else:
            self.canvas.create_image(event.x, event.y, image = self.report_img)

    def kill(self, event):    
        if event.x == self.sx and event.y == self.sy:
            self.canvas.create_image(self.sx, self.sy - 30, image = self.kill_img)
        else:
            self.canvas.create_image(event.x, event.y, image = self.kill_img)
    
    def vent(self, event):    
        if event.x == self.sx and event.y == self.sy:
            self.canvas.create_image(self.sx, self.sy - 30, image = self.vent_img)
        else:
            self.canvas.create_image(event.x, event.y, image = self.vent_img)
    
    def sabo(self, event):    
        if event.x == self.sx and event.y == self.sy:
            self.canvas.create_image(self.sx, self.sy - 30, image = self.sabo_img)
        else:
            self.canvas.create_image(event.x, event.y, image = self.sabo_img)
    
    #MAPの切り替え
    def SKELD(self):
        img = Image.open('SKELD_MAP_half.png')
        bg_white = Image.new('RGB', img.size, (255,255,255))
        img = Image.blend(img, bg_white, 0.3)

        self.tkimg = ImageTk.PhotoImage(img)
        self.canvas.create_image(img_width / 2, img_height / 2 + blank, image= self.tkimg)

    def MIRA(self):
        img = Image.open('MIRA_HQ_half.png')
        bg_white = Image.new('RGB', img.size, (255,255,255))
        img = Image.blend(img, bg_white, 0.15)

        self.tkimg = ImageTk.PhotoImage(img)
        self.canvas.create_image(img_width / 2, img_height / 2 + blank, image= self.tkimg)

    def POLUS(self):
        img = Image.open('POLUS_half.png')
        bg_white = Image.new('RGB', img.size, (255,255,255))
        img = Image.blend(img, bg_white, 0.15)

        self.tkimg = ImageTk.PhotoImage(img)
        self.canvas.create_image(img_width / 2, img_height / 2 + blank, image= self.tkimg)
    
    def SKELDe(self):
        img = Image.open('SKELD_easy_half.png')
        bg_white = Image.new('RGB', img.size, (255,255,255))
        img = Image.blend(img, bg_white, 0.3)

        self.tkimg = ImageTk.PhotoImage(img)
        self.canvas.create_image(img_width / 2, img_height / 2 + blank, image= self.tkimg)

    def MIRAe(self):
        img = Image.open('MIRA_HQ_easy_half.png')
        bg_white = Image.new('RGB', img.size, (255,255,255))
        img = Image.blend(img, bg_white, 0.3)

        self.tkimg = ImageTk.PhotoImage(img)
        self.canvas.create_image(img_width / 2, img_height / 2 + blank, image= self.tkimg)

    def POLUSe(self):
        img = Image.open('POLUS_easy_half.png')
        bg_white = Image.new('RGB', img.size, (255,255,255))
        img = Image.blend(img, bg_white, 0.3)

        self.tkimg = ImageTk.PhotoImage(img)
        self.canvas.create_image(img_width / 2, img_height / 2 + blank, image= self.tkimg)


    
    
        

    def create_window(self):
        def set_color():
            def white():
                self.color.set("white")
            def orange():
                self.color.set("orange")    
            def green():
                self.color.set("green")
            def yellow():
                self.color.set("yellow")
            def purple():
                self.color.set("purple")
            def blue():
                self.color.set("blue")
            def red():
                self.color.set("red")
            def pink():
                self.color.set("pink")
            def brown():
                self.color.set("brown")
            def black():
                self.color.set("black")
            def limegreen():
                self.color.set("limegreen")
            def lightblue():
                self.color.set("lightblue")

            # crewのデータセット（死亡時）
            self.dead_white_img = tkinter.PhotoImage(file = "./crew_set/dead_white_half.png")
            self.dead_orange_img = tkinter.PhotoImage(file = "./crew_set/dead_orange_half.png")
            self.dead_green_img = tkinter.PhotoImage(file = "./crew_set/dead_green_half.png")
            self.dead_yellow_img = tkinter.PhotoImage(file = "./crew_set/dead_yellow_half.png")
            self.dead_purple_img = tkinter.PhotoImage(file = "./crew_set/dead_purple_half.png")
            self.dead_blue_img = tkinter.PhotoImage(file = "./crew_set/dead_blue_half.png")
            self.dead_red_img = tkinter.PhotoImage(file = "./crew_set/dead_red_half.png")
            self.dead_pink_img = tkinter.PhotoImage(file = "./crew_set/dead_pink_half.png")
            self.dead_brown_img = tkinter.PhotoImage(file = "./crew_set/dead_brown_half.png")
            self.dead_black_img = tkinter.PhotoImage(file = "./crew_set/dead_black_half.png")
            self.dead_limegreen_img = tkinter.PhotoImage(file = "./crew_set/dead_limegreen_half.png")
            self.dead_lightblue_img = tkinter.PhotoImage(file = "./crew_set/dead_lightblue_half.png")

            
            # crewのデータセット（生存時）
            self.white_img = tkinter.PhotoImage(file = "./crew_set/white_half.png")
            self.orange_img = tkinter.PhotoImage(file = "./crew_set/orange_half.png")
            self.green_img = tkinter.PhotoImage(file = "./crew_set/green_half.png")
            self.yellow_img = tkinter.PhotoImage(file = "./crew_set/yellow_half.png")
            self.purple_img = tkinter.PhotoImage(file = "./crew_set/purple_half.png")
            self.blue_img = tkinter.PhotoImage(file = "./crew_set/blue_half.png")
            self.red_img = tkinter.PhotoImage(file = "./crew_set/red_half.png")
            self.pink_img = tkinter.PhotoImage(file = "./crew_set/pink_half.png")
            self.brown_img = tkinter.PhotoImage(file = "./crew_set/brown_half.png")
            self.black_img = tkinter.PhotoImage(file = "./crew_set/black_half.png")
            self.limegreen_img = tkinter.PhotoImage(file = "./crew_set/limegreen_half.png")
            self.lightblue_img = tkinter.PhotoImage(file = "./crew_set/lightblue_half.png")

            #矢印
            self.arrow_img = tkinter.PhotoImage(file = "./arrow_half.png")
            self.arrows_img = tkinter.PhotoImage(file = "./arrows_half.png")

            # 場所
            self.admin_img = tkinter.PhotoImage(file = "./Admin_half.png")
            self.security_img = tkinter.PhotoImage(file = "./Security_half.png")
            self.report_img = tkinter.PhotoImage(file = "./Report_half.png")
            self.kill_img = tkinter.PhotoImage(file = "./Kill_half.png")
            self.vent_img = tkinter.PhotoImage(file = "./Vent_half.png")
            self.sabo_img = tkinter.PhotoImage(file = "./Sabotage_half.png")
            



            yy = 590

            #CREWのボタン設定
            white_button = tkinter.Button(window, text = "white", command = white, image = self.white_img)
            white_button.place(x = 0, y = yy)
            
            orange_button = tkinter.Button(window, text = "orange", command = orange, image = self.orange_img)
            orange_button.place(x = 5+48, y = yy)
            
            green_button = tkinter.Button(window, text = "green", command = green, image = self.green_img)
            green_button.place(x = 10+48*2, y = yy)

            yellow_button = tkinter.Button(window, text = "yellow", command = yellow, image = self.yellow_img)
            yellow_button.place(x = 15+48*3, y = yy)
            
            purple_button = tkinter.Button(window, text = "purple", command = purple, image = self.purple_img)
            purple_button.place(x = 20+48*4, y = yy)
            
            blue_button = tkinter.Button(window, text = "blue", command = blue, image = self.blue_img)
            blue_button.place(x = 25+48*5, y = yy)
            
            red_button = tkinter.Button(window, text = "red", command = red, image = self.red_img)
            red_button.place(x = 30+48*6, y = yy)
            
            pink_button = tkinter.Button(window, text = "pink", command = pink, image = self.pink_img)
            pink_button.place(x = 35+48*7, y = yy)
            
            brown_button = tkinter.Button(window, text = "brown", command = brown, image = self.brown_img)
            brown_button.place(x = 40+48*8, y = yy)
            
            black_button = tkinter.Button(window, text = "black", command = black, image = self.black_img)
            black_button.place(x = 45+48*9, y = yy)
            
            limegreen_button = tkinter.Button(window, text = "limegreen", command = limegreen, image = self.limegreen_img)
            limegreen_button.place(x = 50+48*10, y = yy)
            
            lightblue_button = tkinter.Button(window, text = "lightblue", command = lightblue, image = self.lightblue_img)
            lightblue_button.place(x = 55+48*11, y = yy)
            
            

          
        yy = 590
        self.now_x = 0
        self.now_y = 0

        window = tkinter.Tk()
        window.title("among us detection tool")
        window.geometry("1224x636")
        window.configure(background = "white")
        self.canvas = tkinter.Canvas(window, bg = "black", 
                                 bd = 5, relief = tkinter.RIDGE,cursor = "dot",
                                 width = img_width, height = img_height + blank)                             
        self.canvas.place(x = 0, y= 0)

        #ボタンセット
        quit_button = tkinter.Button(window, text = "終了  Ctrl+C",
                                 command = window.quit, width = 20)
        quit_button.place(x = 1044, y = 606)
        skeld_button = tkinter.Button(window, text = "SKELD",
                                 command = self.SKELD, width = 20)
        skeld_button.place(x = 1200, y = 0, width = 70)
        mira_button = tkinter.Button(window, text = "MIRA HQ",
                                 command = self.MIRA, width = 20)
        mira_button.place(x = 1200, y = 55, width = 70)
        polus_button = tkinter.Button(window, text = "POLUS",
                                 command = self.POLUS, width = 20)
        polus_button.place(x = 1200, y = 110, width = 70)
        skeld_ea_button = tkinter.Button(window, text = "SKELD2",
                                 command = self.SKELDe, width = 20)
        skeld_ea_button.place(x = 1200, y = 25, width = 70)
        mira_ea_button = tkinter.Button(window, text = "MIRA HQ2",
                                 command = self.MIRAe, width = 20)
        mira_ea_button.place(x = 1200, y = 80, width = 70)
        polus_ea_button = tkinter.Button(window, text = "POLUS2",
                                 command = self.POLUSe, width = 20)
        polus_ea_button.place(x = 1200, y = 135, width = 70)
        
        
        
        self.VSflame = tkinter.LabelFrame(window, text = "グレー", 
                                            labelanchor = "n", font = ("arial",15),
                                            bd = 5, relief=tkinter.RIDGE,bg = "white", cursor= "dot")
        self.VSflame.place(x = 1044, y = 0, width = 150, height = 150)
        self.VScanvas = tkinter.Canvas(self.VSflame, bg = "white", width = 137, height = 115)
        self.VScanvas.place(x = 0, y = 0)
        
        #CREW
        self.CREWflame = tkinter.LabelFrame(window, text = "白置き", 
                                            labelanchor = "n", font = ("arial",15),
                                            bd = 5, relief=tkinter.RIDGE,bg = "white", cursor= "dot")
        self.CREWflame.place(x = 1044, y = 175, width = 150, height = 150)
        self.CREWcanvas = tkinter.Canvas(self.CREWflame, bg = "white", width = 137, height = 115)
        self.CREWcanvas.place(x = 0, y = 0)
        
        #INPOSTA
        self.INPflame = tkinter.LabelFrame(window, text = "黒置き", 
                                            labelanchor = "n", font = ("arial",15),
                                            bd = 5, relief=tkinter.RIDGE,bg = "white", cursor= "dot")
        self.INPflame.place(x = 1044, y = 350, width = 150, height = 150)
        self.INPcanvas = tkinter.Canvas(self.INPflame, bg = "white", width = 137, height = 115)
        self.INPcanvas.place(x = 0, y = 0)

        #注意書き
        self.explain = tkinter.Label(text = " キー入力", font = ("arial", 10))
        self.explain2 = tkinter.Label(text = " A= admin  S= security  R= report", font = ("arial", 10))
        self.explain3 = tkinter.Label(text = " V= vent     X= kill    B= sabotage", font = ("arial", 10))
        self.explain4 = tkinter.Label(text = "Project by @amongus_tsuna (twitter)", font = ("arial", 10))
        self.explain.place(x = 800, y = 590)
        self.explain2.place(x = 800, y = 610)
        self.explain3.place(x = 800, y = 630)
        self.explain4.place(x = 2, y = 630)
        
        
        
        #MAP初期値
        img = Image.open('SKELD_MAP_half.png')
        bg_white = Image.new('RGB', img.size, (255,255,255))
        img = Image.blend(img, bg_white, 0.3)
        
        self.tkimg = ImageTk.PhotoImage(img)
        self.canvas.create_image(img_width / 2, img_height / 2 + blank, image= self.tkimg)

        #各種ボタンの設定
        self.canvas.bind("<ButtonPress-1>", self.on_pressed) 
        self.canvas.bind("<B1-Motion>", self.on_dragged)
        self.canvas.bind("<ButtonPress-2>",self.click1) 
        self.canvas.bind("<ButtonPress-3>",self.click2) 

        self.VScanvas.bind("<ButtonPress-3>",self.click3) 
        self.CREWcanvas.bind("<ButtonPress-3>",self.click4) 
        self.INPcanvas.bind("<ButtonPress-3>",self.click5) 

        self.VScanvas.bind("<ButtonPress-2>",self.click6) 
        self.CREWcanvas.bind("<ButtonPress-2>",self.click7) 
        self.INPcanvas.bind("<ButtonPress-2>",self.click8)

        self.VScanvas.bind("<ButtonPress-1>",self.click9)
        self.CREWcanvas.bind("<ButtonPress-1>",self.click10)
        self.INPcanvas.bind("<ButtonPress-1>",self.click11) 
        
        self.canvas.bind("<KeyPress-a>",self.admin) 
        self.canvas.bind("<KeyPress-s>",self.security)
        self.canvas.bind("<KeyPress-r>",self.report)
        self.canvas.bind("<KeyPress-x>",self.kill) 
        self.canvas.bind("<KeyPress-v>",self.vent)
        self.canvas.bind("<KeyPress-b>",self.sabo) 
        window.bind("<Control-c>", quit)
        self.canvas.focus_set()
        
        #色関連
        COLORS = ["white", "orange", "green", "yellow", 
        "purple", "blue", "red", "pink", "brown", 
        "black", "limegreen", "lightblue"]
        self.color = tkinter.StringVar()                    
        self.color.set(COLORS[0])                        
        
        set_color()

        self.death_flame = tkinter.LabelFrame(window, text = "死亡推定 (秒前)", 
                                            labelanchor = "n", font = ("arial",12),
                                            bd = 5, relief=tkinter.RIDGE,bg = "white")
        self.death_flame.place(x = 1044, y = 510, width = 150, height = 75)
         
        self.death_time = tkinter.Scale(self.death_flame, from_ = 1, to = 50, orient = tkinter.HORIZONTAL)
        self.death_time.set(5)
        self.death_time.place(x = 15, y = 10)

        self.width = tkinter.Scale(window, from_ = 1, to = 10,
                               orient = tkinter.HORIZONTAL) 
        self.width.set(5)                                       
        self.width.place(x = 80+48*12, y = yy)

        return window;

    
    def __init__(self):
        self.window = self.create_window();  
        
    def run(self):
        self.window.mainloop()
Scribble().run()
