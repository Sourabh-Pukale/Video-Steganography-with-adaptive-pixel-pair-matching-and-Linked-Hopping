import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
from tkinter import *
from tkinter import *
from tkinter import filedialog
import cv2
from tkinter import ttk
import os
from PIL import Image
import subprocess
import cv2
import os
from PIL import Image
import subprocess
import shutil


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        self.grid()
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        self.title("Steganography")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self,bg="black")
        container.pack(fill=BOTH, expand=YES)

        # # container.pack(side=",top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        parent.grid_columnconfigure(0,weight=1)
        parent.grid_rowconfigure(0, weight=1)
        self.configure(bg="black")

        B1 = Button(self, text="Encode", command=lambda: controller.show_frame("PageOne"))
        B1.place(relx=0.262, rely=0.405, height=43, width=136)
        B1.configure(bg="black")
        B1.configure(font=("Courier", 20,'bold'))
        B1.configure(fg="white")

        B2 = Button(self, text="Decode", command=lambda: controller.show_frame("PageTwo"))
        B2.configure(bg="black")
        B2.configure(foreground="white")
        B2.configure(font=("Courier", 20,'bold'))
        B2.place(relx=0.54, rely=0.405, height=43, width=136)



class PageOne(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        # self.pack(fill=BOTH, expand=YES)
        self.configure(bg="black")

        self.label1 = Label(self, text="Choose Video")
        self.label1.place(relx=0.180, rely=0.350, height=34, width=142)
        self.label1.configure(bg="black")
        self.label1.configure(font=("Courier", 15,'bold'))
        self.label1.configure(foreground="white")

        self.label2 = Label(self, text="Input Text")
        self.label2.place(relx=0.183, rely=0.489, height=34, width=138)
        self.label2.configure(bg="black")
        self.label2.configure(font=("Courier", 15,'bold','italic'))
        self.label2.configure(fg="green2")

        self.entry1 = Entry(self)
        self.entry1.place(relx=0.383, rely=0.356, height=24, relwidth=0.34)
        self.entry1.configure(background="white")
        self.entry1.configure(foreground="black")

        self.entry2 = Entry(self)
        self.entry2.place(relx=0.383, rely=0.489, height=24, relwidth=0.34)
        self.entry2.configure(background="white")
        self.entry2.configure(foreground="black")

        self.button1 = Button(self, text="Browse", command=self.callback)
        self.button1.place(relx=0.75, rely=0.356, height=33, width=69)
        self.button1.configure(font=("Courier", 10))
        self.button1.configure(bg="black")
        self.button1.configure(foreground="white")

        self.button2 = Button(self, text="Encode", command=self.encode)
        self.button2.place(relx=0.500, rely=0.689, height=37, width=78)
        self.button2.configure(background="black")
        self.button2.configure(font=("Courier", 10))
        self.button2.configure(foreground="white")

        self.button3 = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        self.button3.place(relx=0.0, rely=0.0, height=33, width=69)
        self.button3.configure(bg="black")
        self.button3.configure(font=("Courier", 10))
        self.button3.configure(fg="white")

        #################################################################

    def frame_to_images(self,video):
        folder = 'VSJH_IMAGES'

        os.makedirs(folder, exist_ok=True)

        vidcap = cv2.VideoCapture(video)
        cnt = 0

        while True:
            success, arrayframe = vidcap.read()
            if not success:
                break
            cv2.imwrite(os.path.join(folder, "{:d}.png".format(cnt)), arrayframe)
            cnt += 1

    def fti(self,video):
        folder = 'VSJH_ORI'

        os.makedirs(folder, exist_ok=True)

        vidcap = cv2.VideoCapture(video)
        cnt = 0

        while True:
            success, arrayframe = vidcap.read()
            if not success:
                break
            cv2.imwrite(os.path.join(folder, "{:d}.png".format(cnt)), arrayframe)
            cnt += 1


    def popupmsg(self):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text="Invalid Input", font=("Courier", 10))
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()


    def encode(self):

        send_lis = []

        input_string = self.entry2.get()
        video_path = self.entry1.get()

        self.fti(video_path)

        print("INput : Sytring  -------------------> "+input_string)

        if len(input_string)==0:
            self.popupmsg()

        if len(video_path)==0:
            self.popupmsg()

        input_video_path = ""
        for i in video_path:
             if i is '/':
                 #print("q")
                 input_video_path +='\\\\'
             else:
                 input_video_path += i

        print(input_video_path)

        self.frame_to_images(input_video_path)

        # print("FRAMES TO IMAGES COMPLETED.")

        vidObj = cv2.VideoCapture(input_video_path)
        length = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))

        # print("Number of Frames : "+" "+str(length))
        # print(s)

        s = []

        s.append(len(input_string))

        for i in range(0, len(input_string)):
            s.append(ord(input_string[i]))

        slis = set()
        lis = []

        seed = int(0)

        # /////////////////////////////////////////////////////////////////////

        # FINDING INITIAL SEED BY ADDING ALL R,G,B VALUES FROM FIRST FRAME.

        psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(0) + ".png")
        width, height = psframe.size

        # print("width : "+str(width)+" height : "+str(height))

        for row in range(0, width - 1):
            for column in range(0, height - 1):
                x, y, z = psframe.getpixel((row, column))
                seed += int(int(x) + int(y) + int(z))
        seed = seed % 179

        print("SEED : "+str(seed))

        # /////////////////////////////////////////////////////////////////////

        seed_saved = int(seed)  # SEED SAVED WHICH CAN GIVE THE SEQUENCE.

        m = int(length)  # M IS THE NUMBER OF FRAMES OF THE VIDEO.

        seed, slis, lis = self.next_seed(seed, m, slis, lis)  # FIRST SEED IS GENERATED FOR

        # print("First frame" + "  " + str(seed))
        #seed_saved=int(seed)
        psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(seed) + ".png")
        width, height = psframe.size

        n1 = int((width - 1) / 2)  # GOTO MIDDLE POSITION OF FIRST FRAME FROM THE SEQUENCE TO FIND NUMBER OF HOPS.
        n2 = int((height - 1) / 2)

        r, g, b = psframe.getpixel((n1, n2))
        next_hop = (r + g + b) % 9 + 1

        lis.clear()  # NOW WE GOT FIRST HOP AS WELL AS THE SEED SO EMPTY THE LIST AND SET.
        slis.clear()

        seed = seed_saved  # INITIALIZE SEED TO ACTUAL SEED VALUE.

        xcor = int(width / 2)  # INITIALLY POSITION OF XCOR AND YCOR IS MIDDLE.
        ycor = int(height / 2)
        prevxcor = int(xcor)
        prevycor = int(ycor)

        # print("XCOR :: " + str(xcor) + "  YCOR :: " + str(ycor))

        # print("INITIAL XCOR AND YCOR : " + "  " + str(xcor) + " " + str(ycor))

        for idx in range(0, len(s)):  # ITERATE LOOP FOR PUTTING IDX NUMBER OF CHARACTERS

            for __ in range(0, next_hop):  # SKIP X = NUMBER OF HOPS, FRAMES BY TAKING VALUE OF NEXT XCOR

                seed, slis, lis = self.next_seed(seed, m, slis, lis)

                psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(seed) + ".png")
                width, height = psframe.size

                xtrav = xcor
                ytrav = ycor
                next_xcor = ""
                next_ycor = ""

                for i in range(1, 16):  # FINDING NEXT X COORDINATE
                    xtrav += 1
                    xtrav = xtrav % width
                    r, g, b = psframe.getpixel((xtrav, ytrav))
                    if r % 2 == 0:
                        next_xcor += '0'
                    else:
                        next_xcor += '1'

                for i in range(1, 16):  # FINDING NEXT Y COORDINATE
                    ytrav -= 1
                    ytrav = ytrav % height
                    r, g, b = psframe.getpixel((xtrav, ytrav))
                    if r % 2 == 0:
                        next_ycor += '0'
                    else:
                        next_ycor += '1'

                prevxcor = xcor
                prevycor = ycor
                xcor = int(next_xcor, 2) % width
                ycor = int(next_ycor, 2) % height
                print("XCOR :: " + str(xcor) + "  YCOR :: " + str(ycor))

            seed, slis, lis = self.next_seed(seed, m, slis, lis)  # FRAME TO INSERT THE DATA.
            psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(seed) + ".png")
            width, height = psframe.size

            val = s[idx]
            val_str = self.binary(val)

            xflg = int(0)
            yflg = int(0)
            diff = int(1000000007)

            for i in range(0, width - 1):  # FINDING XFLG AND YFLG TO INSERT DATA INTO FRAME IN 3,3,2 FORMAT.
                for j in range(0, height - 1):
                    rr, gg, bb = psframe.getpixel((i, j))

                    rstr = self.binary(rr)
                    gstr = self.binary(gg)
                    bstr = self.binary(bb)

                    if rstr[5:] == val_str[0:3] and gstr[5:] == val_str[3:6] and bstr[6:] == val_str[6:]:
                        xflg = i
                        yflg = j
                        break
                    else:
                        string = rstr[5:] + gstr[5:] + bstr[6:]
                        val_string = int(string, 2)
                        if (int(abs(val_string - val)) < int(diff)):
                            diff = abs(val_string - val)
                            xflg = i
                            yflg = j

            xcor = xflg
            ycor = yflg

            r, g, b = psframe.getpixel((xflg, yflg))  # GET VAL OF THE COORDINATE TO CHANGE IT.
            rchstr = self.binary(r)
            gchstr = self.binary(g)
            bchstr = self.binary(b)

            rchstr = rchstr[5:] + val_str[0:3]  # CHANGING VALUE OF THE PIXEL BY OUR DATA.
            gchstr = gchstr[5:] + val_str[3:6]
            bchstr = bchstr[6:] + val_str[6:]

            r = int(rchstr, 2)  # NEW PIXEL VALUES AS OUR DATA.
            g = int(gchstr, 2)
            b = int(bchstr, 2)

            encoded = psframe.copy()  # TIME TO PUT THIS INTO FRAME

            print("FRAME : " + str(seed) + "  Co ordinates : " + str(xflg) + "  "
                 + str(yflg) + "  DATA : " + str(s[idx]) )

            encoded.putpixel((xflg, yflg), (r, g, b))  # CHANGE SUCCESSFUL

            # send_lis.append(seed)

            encoded.save(str("VSJH_IMAGES") + "\\" + str(seed) + ".png", compress_level=0)  # SAVING THE FRAME.

            r, g, b = encoded.getpixel((xflg, yflg))
            next_hop = (r + g + b) % 9 + 1  # FINDING NEXT NUMBER OF HOPS.
            print("Next number of hops : " + str(next_hop))

            frame_num = lis[-2]  # OPENING PREVIOUS FRAME
            psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(frame_num) + ".png")
            encoded = psframe.copy()

            xtrav = prevxcor
            ytrav = prevycor

            xcorstr = self.Binary(xflg)
            ycorstr = self.Binary(yflg)

            while len(xcorstr) < 15:  # CREATING BINARY STRING OF X AND Y CORDINATES
                xcorstr = '0' + xcorstr
            while len(ycorstr) < 15:
                ycorstr = '0' + ycorstr

            for i in range(1, 16):
                xtrav += 1
                xtrav = xtrav % width
                r, g, b = psframe.getpixel((xtrav, ytrav))
                r = self.binary(r)
                r = r[:7] + xcorstr[i - 1]
                r = int(r, 2)
                encoded.putpixel((xtrav, ytrav), (r, g, b))

            for i in range(1, 16):
                ytrav -= 1
                ytrav = ytrav % height
                r, g, b = psframe.getpixel((xtrav, ytrav))
                r = self.binary(r)
                r = r[:7] + ycorstr[i - 1]
                r = int(r, 2)
                encoded.putpixel((xtrav, ytrav), (r, g, b))
            prevxcor = int(xcorstr, 2) % width
            prevycor = int(ycorstr, 2) % height
            print("------>>>>>>>>"+str(frame_num))

            send_lis.append(frame_num)

            encoded.save(str("VSJH_IMAGES") + "\\" + str(frame_num) + ".png", compress_level=0)
        vidObj.release()
        cv2.destroyAllWindows()
        #self.merge(input_video_path)
        print("----------------------------------------------------------------------------------")

        print("SEND_LIS IS HERE GRAB IT !!!")

        print(send_lis)
        print("WIDTH IS HERE : ")
        print(width)
        print("HEIGHT IS HERE : ")
        print(height)
        print("----------------------------------------------------------------------------------")


    def merge(self,input_video_path):  # CHECK PATH AND DIRECTORIES OF COMMANDS.

        command4 = "ffmpeg -framerate 30 -i VSJH_IMAGES\\%d.png -c:v huffyuv -pix_fmt rgb24 VSJH_IMAGES\\mute_video.mkv "
        subprocess.call(command4, shell=True)
        command1 = "ffmpeg -i " + input_video_path + " -ab 160k -ac 2 -ar 44100 -vn VSJH_IMAGES\\MiniAudio.wav"
        subprocess.call(command1, shell=True)
        os.makedirs("Stego_Video", exist_ok=True)
        command3 = "ffmpeg -i VSJH_IMAGES\\mute_video.mkv -i VSJH_IMAGES\\MiniAudio.wav -c copy -map 0:v -map 1:a Stego_Video\\StegoVideo.mkv"
        subprocess.call(command3, shell=True)
        dirpath = os.getcwd()
        shutil.rmtree(dirpath + "\\VSJH_IMAGES")

    def callback(self):
        path = filedialog.askopenfilename()
        #self.entry1.delete(0, END)  # Remove current text in entry
        self.entry1.insert(0, path)  # Insert the 'path'

    def Binary(self,n):  # FUNCTION TO RETURN BINARY FORMAT OF ANY NUMBER.
        s = bin(n)
        return s[2:]

    def binary(self,n):  # FUNCTION TO RETURN BINARY FORMAT OF NUMBER LESS THAN 256 IN 8 BITS FORMAT.
        s = bin(n)
        s = s[2:]
        while len(s) < 8:
            s = '0' + s
        return s  # BOTH FUNCTIONS ARE NECESSARY.


    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def next_seed(self,seed, m, slis, lis):
        a = int(1237403)
        b = int(3220093)
        seed = (a * seed + b) % (m - 1)
        seed += 1
        lprev = int(len(slis))
        slis.add(seed)
        if lprev == len(slis):
            for j in range(1,m):
                lprev = (len(slis))
                seed = j
                slis.add(seed)
                if (lprev != len(slis)):
                    lis.append(seed)
                    break
        else:
            lis.append(seed)
        return seed, slis, lis




class PageTwo(tk.Frame):

    def callback(self):
        path = filedialog.askopenfilename()
        #self.entry1.delete(0, END)  # Remove current text in entry
        self.entry1.insert(0, path)  # Insert the 'path'

    def Binary(self,n):  # FUNCTION TO RETURN BINARY FORMAT OF ANY NUMBER.
        s = bin(n)
        return s[2:]

    def binary(self,n):  # FUNCTION TO RETURN BINARY FORMAT OF NUMBER LESS THAN 256 IN 8 BITS FORMAT.
        s = bin(n)
        s = s[2:]
        while len(s) < 8:
            s = '0' + s
        return s  # BOTH FUNCTIONS ARE NECESSARY.

    def frame_to_images(self,video):
        folder = 'VSJH_IMAGES'

        os.makedirs(folder, exist_ok=True)

        vidcap = cv2.VideoCapture(video)
        cnt = 0

        while True:
            success, arrayframe = vidcap.read()
            if not success:
                break
            cv2.imwrite(os.path.join(folder, "{:d}.png".format(cnt)), arrayframe)
            cnt += 1

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def next_seed(self,seed, m, slis, lis):
        a = int(1237403)
        b = int(3220093)
        seed = (a * seed + b) % (m - 1)
        seed += 1
        lprev = int(len(slis))
        slis.add(seed)
        if lprev == len(slis):
            for j in range(1,m):
                lprev = (len(slis))
                seed = j
                slis.add(seed)
                if (lprev != len(slis)):
                    lis.append(seed)
                    break
        else:
            lis.append(seed)
        return seed, slis, lis

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def decode(self):  # def decode(length):
        video_path = self.entry1.get()

        if len(video_path) == 0:
            self.popupmsg()

        path = ""
        for i in video_path:
            if i == "/":
                path += "\\\\"
            else:
                path += i

        print(path)

        self.frame_to_images(path)  # CONVERT THE STEGO VIDEO TO FRAMES

        # print("FRAMES TO IMAGES COMPLETED.")

        vidObj = cv2.VideoCapture(path)
        length = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))  # CALCULATE THE NUMBER OF FRAMES IN STEGO VIDEO

        # print("Number of Frames : "+" "+str(length))

        dslis = set()
        dlis = []

        seed = int(0)

        # /////////////////////////////////////////////////////////////////////

        # FINDING INITIAL SEED BY ADDING ALL R,G,B VALUES FROM FIRST FRAME.

        psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(0) + ".png")
        width, height = psframe.size

        # print("width : "+str(width)+" height : "+str(height))

        for row in range(0, width - 1):
            for column in range(0, height - 1):
                x, y, z = psframe.getpixel((row, column))
                seed += int(int(x) + int(y) + int(z))
        seed = seed % 179

        print("DECODE : SEED : "+str(seed))

        # /////////////////////////////////////////////////////////////////////

        seed_saved = int(seed)  # SEED SAVED WHICH CAN GIVE THE SEQUENCE.

        m = int(length)  # M IS THE NUMBER OF FRAMES OF THE VIDEO.

        seed, dslis, dlis = self.next_seed(seed, m, dslis, dlis)  # FIRST SEED IS GENERATED FOR

        print("First frame" + "  " + str(seed))

        psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(seed) + ".png")
        width, height = psframe.size

        n1 = int((width - 1) / 2)  # GOTO MIDDLE POSITION OF FIRST FRAME FROM THE SEQUENCE TO FIND NUMBER OF HOPS.
        n2 = int((height - 1) / 2)

        r, g, b = psframe.getpixel((n1, n2))
        next_hop = (r + g + b) % 9 + 1

        dlis.clear()  # NOW WE GOT FIRST HOP AS WELL AS THE SEED SO EMPTY THE LIST AND SET.
        dslis.clear()

        seed = seed_saved  # INITIALIZE SEED TO ACTUAL SEED VALUE.

        xcor = int(width / 2)  # INITIALLY POSITION OF XCOR AND YCOR IS MIDDLE.
        ycor = int(height / 2)

        print("INITIAL XCOR AND YCOR : " + "  " + str(xcor) + " " + str(ycor))

        num_of_chars = int(0)

        print("Number of chars : " + str(num_of_chars))

        for idx in range(0, 1):  # ITERATE LOOP FOR PUTTING IDX NUMBER OF CHARACTERS

            for __ in range(0, next_hop):  # SKIP X = NUMBER OF HOPS, FRAMES BY TAKING VALUE OF NEXT XCOR

                seed, dslis, dlis = self.next_seed(seed, m, dslis, dlis)

                psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(seed) + ".png")
                width, height = psframe.size

                xtrav = xcor
                ytrav = ycor
                next_xcor = ""
                next_ycor = ""

                for i in range(1, 16):  # FINDING NEXT X COORDINATE
                    xtrav += 1
                    xtrav = xtrav % width
                    r, g, b = psframe.getpixel((xtrav, ytrav))
                    if r % 2 == 0:
                        next_xcor += '0'
                    else:
                        next_xcor += '1'

                for i in range(1, 16):  # FINDING NEXT Y COORDINATE
                    ytrav -= 1
                    ytrav = ytrav % height
                    r, g, b = psframe.getpixel((xtrav, ytrav))
                    if r % 2 == 0:
                        next_ycor += '0'
                    else:
                        next_ycor += '1'

                xcor = int(next_xcor, 2) % width
                ycor = int(next_ycor, 2) % height

            seed, dslis, dlis = self.next_seed(seed, m, dslis, dlis)  # FRAME TO EXTRACT THE DATA.
            psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(seed) + ".png")
            width, height = psframe.size

            val_str = ""

            r, g, b = psframe.getpixel((xcor, ycor))  # GET VAL OF THE COORDINATE TO CHANGE IT.

            next_hop = (r + g + b) % 9 + 1

            rchstr = self.binary(r)
            gchstr = self.binary(g)
            bchstr = self.binary(b)

            val_str = val_str + rchstr[5:]  # CHANGING VALUE OF THE PIXEL BY OUR DATA.
            val_str = val_str + gchstr[5:]
            val_str = val_str + bchstr[6:]

            asciival = int(val_str, 2)

            print("FRAME : " + str(seed) + "  Co ordinates : " + str(xcor) + "  "
                 + str(ycor) + "  DATA : " + chr(asciival) + str(asciival))

            num_of_chars = int(asciival)

        print("Number of chars :........................................................ " + str( num_of_chars ))

        ans = []

        for idx in range(0, num_of_chars):  # ITERATE LOOP FOR PUTTING IDX NUMBER OF CHARACTERS

            for __ in range(0, next_hop):  # SKIP X = NUMBER OF HOPS, FRAMES BY TAKING VALUE OF NEXT XCOR

                seed, dslis, dlis = self.next_seed(seed, m, dslis, dlis)

                psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(seed) + ".png")
                width, height = psframe.size

                xtrav = xcor
                ytrav = ycor
                next_xcor = ""
                next_ycor = ""

                for i in range(1, 16):  # FINDING NEXT X COORDINATE
                    xtrav += 1
                    xtrav = xtrav % width
                    r, g, b = psframe.getpixel((xtrav, ytrav))
                    if r % 2 == 0:
                        next_xcor += '0'
                    else:
                        next_xcor += '1'

                for i in range(1, 16):  # FINDING NEXT Y COORDINATE
                    ytrav -= 1
                    ytrav = ytrav % height
                    r, g, b = psframe.getpixel((xtrav, ytrav))
                    if r % 2 == 0:
                        next_ycor += '0'
                    else:
                        next_ycor += '1'

                xcor = int(next_xcor, 2) % width
                ycor = int(next_ycor, 2) % height

            seed, dslis, dlis = self.next_seed(seed, m, dslis, dlis)  # FRAME TO EXTRACT THE DATA.
            psframe = Image.open(str("VSJH_IMAGES") + "\\" + str(seed) + ".png")
            width, height = psframe.size

            val_str = ""

            r, g, b = psframe.getpixel((xcor, ycor))  # GET VAL OF THE COORDINATE TO CHANGE IT.

            next_hop = (r + g + b) % 9 + 1

            rchstr = self.binary(r)
            gchstr = self.binary(g)
            bchstr = self.binary(b)

            val_str = val_str + rchstr[5:]  # CHANGING VALUE OF THE PIXEL BY OUR DATA.
            val_str = val_str + gchstr[5:]
            val_str = val_str + bchstr[6:]

            asciival = int(val_str, 2)

            print("FRAME : " + str(seed) + "  Co ordinates : " + str(xcor) + "  "
                 + str(ycor) + "  DATA : " + chr(asciival))

            ans.append(asciival)
            print("====================================================>>             "+chr(asciival))

        final_string = ""

        for i in ans:
            final_string += chr(i)
            print(chr(i))

        self.entry2.insert(0,final_string)
        shutil.rmtree(os.getcwd()+"\\VSJH_IMAGES")

        print("000000000000000000000000000000000000000000000000000000000000000000000000000")

    def popupmsg(self):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text="Invalid Input", font=("Courier", 10))
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller = controller
        self.parent = parent
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()