from tkinter import *
from tkinter import messagebox
import pandas as pd

def formatTable():
   
   pathFile = str(path_tf.get())
   data = pd.read_excel (pathFile,skiprows=6)
   data['Код проекта'].bfill()
   with pd.ExcelWriter('table.xlsx') as wb:
    data.to_excel(wb,sheet_name='Итог',index = False)
   #print(data)

   messagebox.showinfo('Результаты', 'Плоский файл создан') 
  
window = Tk()
window.title('Программа преобразования в плоский файл')
window.geometry('400x300')
  
frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)
  
path_lb = Label(
   frame,
   text="Введите полный путь к файлу "
)
path_lb.grid(row=1, column=2)
 
path_tf = Entry(
   frame
)
path_tf.grid(row=3, column=2, pady=10)

cal_btn = Button(
   frame,
   text='Преобразовать в плоский файл',
   command=formatTable
)
cal_btn.grid(row=5, column=2,pady = 30)
 
window.mainloop()