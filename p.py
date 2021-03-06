from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
try:
  import googletrans
except Exception as e:
    print(f"not to import googletrans err ==[{e}]")
#import googletrans
try:
  tpp = googletrans.Translator()
  tpp.translate(text='yoyo')
except Exception as ex:
    print(f"not to do work that err=[{ex}]")
# import fileps
#
# ty = (('.py files', '*.py files'), ('.op files', '*.py files'))
#
# fileps.openf(ty, 'open')
# print(fileps.rootf)

root = Tk()
root.attributes('-alpha', 0.50)
# root.overrideredirect(1)
root.attributes('-fullscreen', True)
# messagebox.askyesno('info', 'app starting')
# if FALSE:
#     root.destroy()
img_bg = PhotoImage(file='im.png')
# img_bgs = img_bg.configure(2,2)
root.config(bg='gray')
root.geometry('1780x960')
root.title("main")
root.iconbitmap("im.png")
# root.winfo_screen()
root.wm_iconposition(0, 0)

e = Entry(root)
lbs = Label(root, image=img_bg).place(x=0, y=0)


def op(eo=None):
    import webbrowser
    root.filename = filedialog.askopenfilename(initialdir="", title='open pdf', filetypes=(
        ('.pdf files', '*.pdf files'), ('.not_pdf files', '*.pdf files')))
    Topc=Toplevel()
    Topc.resizable(0,0)
    l = Label(Topc,fg='blue', bg="gray", padx=0, text='path:' + root.filename).grid(row=1, column=0)
    root.iconbitmap(root.filename)
    webbrowser.open(root.filename)
    # import subprocess
    # subprocess.run('python im.py')


def opsd(e=""):
    import speak
    speak.speak(f'start reading:\n{root.filename}')


def hl(e=""):
    import speak
    def el():
        import speak

    speak.speak('hindi')
    dreaded = PyPDF2.PdfFileReader(root.filename)
    pages = dreaded.numPages
    print(pages)

    for num in range(0, pages):
        page = dreaded.getPage(num)
        print(page)
        texts = page.extractText()
        print(texts)
        speak.speak(texts)
        if num == pages:
            Tops = Toplevel()
            l = Label(Tops,text="done to make hindi convert:" + e.get()).grid(row=200, column=0)
    # book = open(root.filename)
    # pr = PyPDF2.PdfFileReader(book)
    # page = pr.numPages
    # print(page)
    speak.speak('processing over . you can read')


def el(e=""):
    import pcl

    pcl.p_c_e(root.filename)


def ml(e=""):
    import pcl
    pcl.p_c_m(root.filename)


def tl(e=""):
    import speak
    speak.speak("tamil")


def zo(e=""):
    import subprocess
    subprocess.run('python test.py')
    # import speak
    # eps = e.get()
    # print(eps)
    # if eps == '':
    #     speak.speak(eps + '\tnot text found. to speak.')
    # else:
    #     print('procesing')
    #     print('text\t' + eps)
    #     speak.speak(e.get())
    # l = Label(text="hello:" + e.get()).grid(row=200, column=0)
    # return None


def opst(e=""):
    import speak
    rootss = Toplevel()

    # e = Entry(root, fg="blue", bg='yellow', width=52, borderwidth=4).grid(row=9, column=0)
    # b_sml_s = Button(fg='blue', bg="gray", padx=140, text='speak now', command=zo).grid(row=10, column=0)
    def g(e):
        io['bg'] = 'green'

    def ga(e):
        io['bg'] = 'red'

    def v(e):
        io['bg'] = 'green'

    def va(e):
        io['bg'] = 'red'

    io = Entry(rootss, fg='blue', bg="red", width=50, borderwidth=5)
    io.pack()
    io.bind('<Enter>', g)
    io.bind('<Leave>', ga)

    # print(io.replace('o', '\tduck\t'), io.replace('out', '\tfan\t'))

    def sp_click():
        ios = io.get()
        speak.speak(ios)

    bks = Button(rootss, fg='blue', bg="black", borderwidth=5, width=50, text='speak', command=sp_click).pack()


# ep = e.get()
# speak.speak(ep)


def speak_text(e=""):
    rootff = Toplevel()
    ej = Entry(rootff, fg='blue', bg='red', border=0, width=25)
    sliders = Scale(rootff, from_=0, to=500, orient=HORIZONTAL, width=35)
    sliders.pack()
    ej.pack()

    def cl():
        import speak
        texts = ej.get()
        speak.set_spead(sliders.get())
        speak.speak(texts)

    b = Button(rootff, command=cl, text='speak text', fg='blue', bg='black', borderwidth=5, padx=50).pack()


def ops(e=""):
    import speak
    speak.speak("opening pdf translate\n \nchuse lang to read pdf")
    framesd = Toplevel(bg = 'gray')
    framesd.resizable(0,0)
    ca = Checkbutton(framesd,fg="blue", bg='yellow', padx=140, text="hindi", command=hl).grid(row=4, column=0)
    cb = Checkbutton(framesd,fg="blue", bg='black', padx=140, text="english", command=el).grid(row=4, column=1)
    cc = Checkbutton(framesd,fg="blue", bg='pink', padx=140, text="marathi", command=ml).grid(row=5, column=0)
    cd = Checkbutton(framesd,fg="blue", bg='red', padx=140, text="tamil", command=tl).grid(row=5, column=1)
    #bd = Button(framesd,fg='blue', bg="gray", padx=140, text='speak start', command=opsd).grid(row=6, column=0)


def pch():
    import speak


def pcm():
    import speak


def pce():
    import speak


def pct():
    import speak
    print('tim')


def sb():
    import PyPDF2
    import subprocess
    subprocess.run('python ooo.py')


def bsof():
    # import subprocess
    # subprocess.run('python ooo.py')
    import pcl
    ios = int(eeee.get())
    print(ios)
    pcl.p_c_e_r(root.filename, ios)


def speak_pdf_no(e=''):
    # fdsk = Entry(root, fg='blue', bg='black')
    # fdsk.grid(row=16, column=0)
    # eeee.place(x = 420,y = 50)
    oooooooooooooo = str(eeee.get())
    if oooooooooooooo == 'page no':
        eeee['bg'] = 'red'
        eeee.delete(0, END)
        eeee.insert(0, 'write page num to red')

    if oooooooooooooo == '':
        eeee['bg'] = 'red'
        eeee.insert(0, 'write page num to red')
        eeee['bg'] = 'red'
    if oooooooooooooo == str:
        eeee['bg'] = 'red'
    else:
        eeee['bg'] = 'blue'
    fos = Button(fg='blue', bg="gray", width=30, text='speak page', command=bsof).grid(row=2, column=2)


def googles(e=""):
    import webbrowser
    webbrowser.open('google translate')


def vo(e=""):
    def mls():
        import speak
        speak.set_voice(0)
        speak.speak('voice has ben set')
        b345 = None
        b3454 = None

    def mlsd():
        import speak
        speak.set_voice(1)
        speak.speak('voice set')
        b345 = ''
        b3454 = ''

    # jees().grid(row = 13, column=1)
    b345 = Checkbutton(fg="blue", bg='yellow', padx=140, text="male", command=mls).grid(row=11, column=2)
    b3454 = Checkbutton(fg="blue", bg='yellow', padx=140, text="female", command=mlsd).grid(row=12, column=2)
    # import time
    # time.sleep(5)
    # b345 = 'h'
    # b3454 = 'ho'


def mobile(e=""):
    import subprocess
    root.winfo_toplevel()
    from tkinter import messagebox
    messagebox.showinfo('app saying to you', 'one window is opening')
    subprocess.run('python p.py')

def exit_button_click():
    exit(1)
def ooooo(e):
    eeee['bg'] = 'green'
    eeee.delete(0, END)


def ooooo1(e):
    eeee['bg'] = 'white'


def gog(e=""):
    rt = Toplevel()

    def oooood(e):
        t1s['bg'] = 'gray'
        # eeee.delete(0, END)

    def oooood1(e):
        t1s['bg'] = 'white'

    def ooooods(e):
        t2s['bg'] = 'gray'
        # eeee.delete(0, END)

    def ooooods1(e):
        t2s['bg'] = 'white'

    def vcls():
        # from googletrans.translate import googletranstest
        print('none')
        t1stext = t1s.get(0.1, END)
        # t2stext = t2s.get(0.1, END)
        import trans
        trans.trans_text(text='hello')
        t1s.delete(0.0, END)
        t1s.insert(INSERT, t1stext)

    rt.resizable(False, False)
    rt.geometry('540x460')
    immmm = PhotoImage(file='immmm.png')
    # immmm.subsample(5, 2)
    # immmm.width()
    t1s = Text(rt, width=30, pady=30, borderwidth=5, fg='blue')
    t1s.place(x=10, y=0)
    t2s = Text(rt, width=30, pady=30, borderwidth=5, fg='red')
    t2s.place(x=290, y=0)
    tbutton = Button(rt, image=immmm, command=vcls).place(x=260, y=0)
    # tcombobox = Button(rt).place(x=260, y=30)
    t1s.bind('<Enter>', oooood)
    t1s.bind('<Leave>', oooood1)
    t2s.bind('<Leave>', ooooods)
    t2s.bind('<Enter>', ooooods1)
    rt.mainloop()


aa_i_i = PhotoImage(file='aa_i.png')
s_i = PhotoImage(file='ip.png')
o_i = PhotoImage(file='opdf.png')
o_is = o_i.subsample(200,15)
spt_i = PhotoImage(file='spt.png')
sch_i = PhotoImage(file='sch.png')
scm_i = PhotoImage(file='scm.png')
sce_i = PhotoImage(file='sce.png')
sct_i = PhotoImage(file='sct.png')
spts_i = PhotoImage(file='spts.png')
sppn_i = PhotoImage(file='sppn.png')
op_i = PhotoImage(file='op.png')
cv_i = PhotoImage(file='cv.png')
a_f_i = PhotoImage(file='afi.png')
# op_i_r = PhotoImage(file = root.filename)
eeee = Entry(root, fg='yellow', bg="blue", width=50, border=0, font=(20))
eeee.grid(row=2, column=1)
eeee.bind('<Enter>', ooooo)
eeee.bind('<Leave>', ooooo1)
root.bind('<Return>', speak_pdf_no)
b = Button(image=o_i, command=op).grid(row=0, column=0)
bs = Button(image=s_i, command=ops).grid(row=2, column=0)
bcc = Button(image=spt_i, command=opst).grid(row=8, column=0)
bdd = Button(image=sch_i, command=pch).grid(row=11, column=0)
bddsf = Button(image=cv_i, command=vo).grid(row=11, column=1)
bee = Button(image=scm_i, command=pcm).grid(row=12, column=0)
jees = Button(image=a_f_i, command=mobile).grid(row=12, column=1)
bff = Button(image=sce_i, command=pce).grid(row=13, column=0)
bgg = Button(image=sct_i, command=pct).grid(row=8, column=1)
eeee.insert(0, 'page no')
bddc = Button(image=spts_i, command=speak_text).grid(row=3, column=0)
bddcfff = Button(image=sppn_i, command=speak_pdf_no).grid(row=0, column=1)
bddcfffgs = Button(image=op_i, command=googles).grid(row=3, column=1)
bddcfffgss = Button(image=aa_i_i, command=gog).grid(row=13, column=1)
bexit = Button(fg = 'red', bg = 'black',text = 'X', command = exit_button_click, padx = 20).place(x = 1600, y = 0)
root.bind('<o>', op)
def hhh(e):
 mek = messagebox.askyesno('info', 'do you want to change sine up')
 if mek == True:
    import webbrowser
    import  subprocess
    webbrowser.open('hhhhhhhhhhhsssss.jar')
    subprocess.run(['python', 'logn.py'])
    exit(1)


def helps(e=None):
    messagebox.askokcancel('help', 'a to add window\npress o to open pdf \npress h to help\npress s to speak pdf\nl to sine up page')


root.bind('<h>', helps)
root.bind('<l>', hhh)
root.bind('<s>', ops)
root.bind('<a>', mobile)
# bddcfffgss = Button(image = op_i_r, command=googles).grid(row=14, column=1)
# fdsk.grid(row=16, column=0)

root.mainloop()
