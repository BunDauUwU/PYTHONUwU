from tkinter import *
from PIL import Image, ImageTk

root = Tk()
photo =PhotoImage(file = 'hutao.png')
root.wm_iconphoto(False, photo)
root.title("Tiền điện hoặc gì đó tương tự")
root.minsize(height=500, width=750)
res = [0,0]
val = [1.728, 1786, 2.074, 2.612, 2.919, 3.015]
level = [50, 100, 200, 300, 400, 0]
money = dict()
def calc(price):
   lst = 0
   for i in range(0, len(val)):
      lst += min(val[i], price)*level[i]
      price -= val[i]
      if price < 0:
         break
   return lst*108/100
##
def sua():
   listbox.delete(0,END)
   money[pos.get()] = Value.get()
   out()
   tinh()
##
def tinh():
   listBox.delete(0,END)
   res[0] = 0
   for i in money.keys():
      res[0] += money.get(i)
   res[1] = res[0] / len(money)
   # for i in range(0, len(money)):
      # listbox.insert(i,f"Tháng {i + 1}: {money[i]/1*1} đồng")
   listBox.insert(len(money)+1,f"Tổng tiền điện: {calc(res[0])} đồng")
   listBox.insert(len(money)+1,f"Tiền điện trung bình: {calc(res[1])} đồng")
##
def xoa():
   money.clear()      
   listbox.delete(0,END)
   tinh()
##
def out():
   cur = 0
   for i in money.keys():
      cur += 1
      listbox.insert(cur,f"Hộ {i}: {calc(money[i])} đồng")
## Variable ##
pos = StringVar()
Value = DoubleVar()
##
image = Image.open("./hutao.png")
 
# Resize the image using resize() method
resize_image = image.resize((500, 500))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.place(x = 300,y = 0) 
##
Label(root, text = "UwU nhập dữ liệu vô đây", fg = "red", width = 20, font = ('cambria', 16)).grid(row = 0, column = 0)
listbox = Listbox(root, width='66', height='13')
listbox.grid(row = 1, columnspan = 3)
listBox = Listbox(root, width='66', height='2')
listBox.grid(row = 2, columnspan = 3)
##
Label(root, text = "Hộ gia đình:").grid(row = 3, column = 0)
Entry(root, width = 20, textvariable=pos).grid(row = 3, column = 1)
##
Label(root, text = "Số điện tiêu thụ:").grid(row = 4, column = 0)
Entry(root, width = 20, textvariable=Value).grid(row = 4, column = 1)
Label(root, text = "kW").grid(row = 4, column = 2)
##
btn = Frame(root)
Button(btn, text = "Thêm hoặc sửa", command=sua).pack(side = LEFT)
Button(btn, text = "Xoá hết", command=xoa).pack(side=LEFT)
Button(btn, text = "Thoát", command = root.quit).pack(side = LEFT)
btn.grid(row = 5, column= 1)

root.mainloop()