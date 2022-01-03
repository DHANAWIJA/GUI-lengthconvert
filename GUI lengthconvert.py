#LENGTH CONVERTOR

import tkinter as tk

def inchtocenti():
    inch=ent_inch.get()
    centi=2.54 *float(inch)
    lbl_result["text"]=f'{(centi)}cm'

window=tk.Tk()
window.title("Length convertor")

frm_entry=tk.Frame(master=window)
ent_inch=tk.Entry(master=frm_entry,width=10)
lbl_temp=tk.Label(master=frm_entry,text="inch")

ent_inch.grid(row=0,column=0,sticky="e")
lbl_temp.grid(row=0,column=1,sticky="w")

btn_convert=tk.Button(
    master=window,
    text="--->",
    command=inchtocenti
)
lbl_result=tk.Label(master=window,text="cm")

frm_entry.grid(row=0,column=0,padx=10)
btn_convert.grid(row=0,column=1,pady=20)
lbl_result.grid(row=0,column=2,padx=30)

window.mainloop()