from tkinter import *
import os
import random

os.chdir(os.path.dirname(__file__))


global sampling_list
sampling_list = []

global whole_list
whole_list = []


def add_name(new_name):
    global sampling_list
    global whole_list
    if new_name not in whole_list:
        whole_list.append(new_name)
        sampling_list.append(new_name)


def sample_name():
    global sampling_list

    if len(sampling_list) > 0:
        name = random.sample(sampling_list, 1)[0]
        lb_sample_name["text"] = name
        sampling_list.remove(name)
    else:
        lb_sample_name["text"] = "Kein Nutzer mehr übrig"


def reset_sample_list():
    global sampling_list
    global whole_list
    sampling_list = whole_list.copy()

window = Tk()
window.title("SST - Simons Sampling Tool")



lb_new_name = Label(window, text="Entry Sample Name:")
lb_new_name.pack()

e_new_name = Entry(window)
e_new_name.pack()


btn_add_name = Button(window, text="Add Name", command = lambda: add_name(str(e_new_name.get())))
btn_add_name.pack()

btn_sample_name = Button(window, text="Sample Name", command = sample_name)
btn_sample_name.pack()


lb_sample_name = Label(window, text="Entry Sample Name:")
lb_sample_name.pack()

btn_reset = Button(window, text="Reset List", command = reset_sample_list)
btn_reset.pack()

window.mainloop()
