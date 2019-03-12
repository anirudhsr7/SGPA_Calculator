from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time


def raise_frame(frame):
    frame.tkraise()
    if frame == f2:
        cal()

thr_list = []
crd_thr_list = []
prac_list = []
crd_prac_list = []

def sgpa():
    thr_list_int = []
    crd_thr_list_int = []
    prac_list_int = []
    crd_prac_list_int= []
    grade_thr = []
    grade_prac = []
    grade_points_thr = []
    grade_points_prac = []
    mul_thr = 0
    mul_prac = 0
    mul = 0
    crd_thr =0
    crd_prac = 0
    tc = 0



    for entry in thr_list:
        val = entry.get()
        val = int(val)
        thr_list_int.append(val)
        print(val)
    for entry in crd_thr_list:
        val = entry.get()
        val = int(val)
        crd_thr_list_int.append(val)
        print(val)
    for entry in prac_list:
        val = entry.get()
        val = int(val)
        prac_list_int.append(val)
        print(val)
    for entry in crd_prac_list:
        val = entry.get()
        val = int(val)
        crd_prac_list_int.append(val)
        print(val)

    def thr_marks_grd(marks):
        if (marks>=90 and marks<=100):
            grd = 'O'
        elif (marks>=80 and marks<90):
            grd = 'A+'
        elif (marks>=70 and marks<80):
            grd = 'A'
        elif (marks>=60 and marks<70):
            grd = 'B+'
        elif (marks>=50 and marks<60):
            grd = 'B'
        elif (marks>=45 and marks<50):
            grd = 'C'
        elif (marks>=40 and marks<45):
            grd = 'P'
        elif (marks<40):
            grd = 'F'

        return grd

    def prac_marks_grd(marks):

        if (marks>=45 and marks<=50):
            grd = 'O'
        elif (marks>=40 and marks<45):
            grd = 'A+'
        elif (marks>=35 and marks<40):
            grd = 'A'
        elif (marks>=30 and marks<35):
            grd = 'B+'
        elif (marks>=25 and marks<30):
            grd = 'B'
        elif (marks>=22.5 and marks<25):
            grd = 'C'
        elif (marks>=20 and marks<22.5):
            grd = 'P'
        elif (marks<20):
            grd = 'F'

        return grd

    grd_dict = {
        'O': 10,
        'A+': 9,
        'A': 8,
        'B+': 7,
        'B': 6,
        'C': 5,
        'P': 4,
        'F': 0
    }

    for i in thr_list_int:
        g = thr_marks_grd(i)
        grade_thr.append(g)

    for i in prac_list_int:
        g = prac_marks_grd(i)
        grade_prac.append(g)

    for g in grade_thr:
        for k, v in grd_dict.items():
            if g == k:
                point = v
                grade_points_thr.append(point)

    for g in grade_prac:
        for k, v in grd_dict.items():
            if g == k:
                point = v
                grade_points_prac.append(point)

    for i in range(0, len(grade_points_thr)):
        m = grade_points_thr[i] * crd_thr_list_int[i]
        mul_thr += m

    for i in range(0, len(grade_points_prac)):
        m = grade_points_prac[i] * crd_prac_list_int[i]
        mul_prac += m

    for i in range(0, len(crd_thr_list_int)):
        crd_thr += crd_thr_list_int[i]

    for i in range(0, len(crd_prac_list_int)):
        crd_prac += crd_prac_list_int[i]

    mul = mul_thr + mul_prac
    tc = crd_thr + crd_prac

    sgpa = (mul / tc)
    g = float("{0:.2f}".format(sgpa))
    print(g)

    time.sleep(0.5)
    messagebox.showinfo("RESULT", "SGPA : {}".format(g))

    raise_frame(f1)


def cal():
    thr_no = thr.get()
    thr_no = int(thr_no)
    prac_no = prac.get()
    prac_no = int(prac_no)
    tr_sem = var1.get()
    tr_sem = int(tr_sem)
    gf_sem = var2.get()
    print(thr_no, prac_no, tr_sem, gf_sem)
    # Label(f2, text="hi").grid()
    count = 0

    Label(f2, text="MARKS").grid(row=0, column=3)
    Label(f2, text="CREDITS").grid(row=0, column=5)
    for i in range(1, thr_no + 1):
        Label(f2, text="Subject {}".format(i)).grid(row=i+1, sticky='w')
        th = Entry(f2)
        th.grid(row=i+1, column=3)
        thr_list.append(th)
        crd = Entry(f2)
        crd.grid(row=i+1, column=5)
        crd_thr_list.append(crd)
        # crd_thr_list.append(int(crd_thr[i]))
        count += 1

    for j in range(1, prac_no+1):
        Label(f2, text="Practical {}".format(j)).grid(row=thr_no+j+1, sticky='w')
        pr = Entry(f2)
        pr.grid(row=thr_no+j+1, column=3)
        prac_list.append(pr)
        crd_prac= Entry(f2)
        crd_prac.grid(row=thr_no + j + 1, column=5)
        crd_prac_list.append(crd_prac)

        count += 1

    time.sleep(0.5)

    if tr_sem == 1:
        Label(f2, text="Training SEM").grid(row=count+2)
        trs = Entry(f2)
        trs.grid(row=count+2, column=3)
        thr_list.append(trs)
        trs_crd = Entry(f2)
        trs_crd.grid(row=count+2, column=5)
        crd_thr_list.append(trs_crd)
    else:
        Label(f2, text="General Fitness").grid(row=count+2)
        gfs = Entry(f2)
        gfs.grid(row=count+2, column=3)
        thr_list.append(gfs)
        gfs_crd = Entry(f2)
        gfs_crd.grid(row=count+2, column=5)
        crd_thr_list.append(gfs_crd)


    ttk.Button(f2, text='Submit', command=sgpa).grid(row=count+4, column=4)
    # for entry in thr_list:
    #     print(entry.get())

root = Tk()
root.wm_title("SGPA CALCULATOR")
root.iconbitmap(r'E:\btech\sem 6\Minor_Project\gne.ico')
#root.geometry("415x300")

f1 = Frame(root, padx=20, pady=20)
f2 = Frame(root, padx=20, pady=20)


for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')

thr_label = tk.Label(f1, text="No. Of Theory Subjects")
thr_label.grid(row= 2, column=1, sticky='w')
thr = tk.Entry(f1)
thr.grid(row=2, column=3)

prac_label = tk.Label(f1, text="No. Of Practical Subjects")
prac_label.grid(row= 4, column=1, sticky='w')
prac = tk.Entry(f1)
prac.grid(row=4, column=3)

gf_tr = tk.Label(f1, text="Training SEM or General Fitness")
gf_tr.grid(row=6, column=1, sticky='w')
var1 = IntVar()
tr = tk.Checkbutton(f1, text="TRAINING SEM", variable=var1)
tr.grid(row=6, column=3, sticky='w')
var2 = IntVar()
gf = tk.Checkbutton(f1, text="GENERAL FITNESS", variable=var2)
gf.grid(row=7, column=3, sticky='w')

ttk.Button(f1, text='Submit', command=lambda:raise_frame(f2)).grid(row=8, column=3)
#Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
#Label(f1, text='FRAME 1').pack()


raise_frame(f1)
root.mainloop()
