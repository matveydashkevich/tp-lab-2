import tkinter as tk
import controller


# constants

BACKGROUND_COLOR = "#f0f0f0"


# window

window = tk.Tk()
window.title("Система обработки заказов")
width=1006
height=542
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)
window.resizable(width=False, height=False)
window.configure(bg=BACKGROUND_COLOR)


# output label

label_output=tk.Label(window)
label_output["bg"] = "white"
label_output["anchor"] = "nw"
label_output["justify"] = "left"
label_output["relief"] = "sunken"
label_output.place(x=110,y=100,width=279,height=359)


# textboxes

textbox_address=tk.Entry(window)
textbox_address.place(x=670,y=150,width=158,height=30)

textbox_order_number_first=tk.Entry(window)
textbox_order_number_first.place(x=670,y=290,width=70,height=25)

textbox_product_number=tk.Entry(window)
textbox_product_number.place(x=780,y=290,width=70,height=25)

textbox_number=tk.Entry(window)
textbox_number.place(x=890,y=290,width=70,height=25)

textbox_order_number_second=tk.Entry(window)
textbox_order_number_second.place(x=670,y=400,width=87,height=30)


# buttons' commands

def button_get_catalog_command():
    try:
        label_output["text"] = controller.get_catalog()
    except:
        label_output["text"] = "Ошибка"

def button_add_order_command():
    try:
        label_output["text"] = controller.add_order(textbox_address.get())
    except:
        label_output["text"] = "Ошибка"

def button_add_product_command():
    try:
        order_number = int(textbox_order_number_first.get())
        product_number = int(textbox_product_number.get())
        number = int(textbox_number.get())
        label_output["text"] = controller.add_product(order_number, product_number, number)
    except:
        label_output["text"] = "Ошибка"

def button_remove_product_command():
    try:
        order_number = int(textbox_order_number_first.get())
        product_number = int(textbox_product_number.get())
        number = int(textbox_number.get())
        label_output["text"] = controller.remove_product(order_number, product_number, number)
    except:
        label_output["text"] = "Ошибка"

def button_form_order_command():
    try:
        label_output["text"] = controller.form_order(int(textbox_order_number_second.get()))
    except:
        label_output["text"] = "Ошибка"

def button_cancel_order_command():
    try:
        label_output["text"] = controller.cancel_order(int(textbox_order_number_second.get()))
    except:
        label_output["text"] = "Ошибка"

def button_get_order_command():
    try:
        label_output["text"] = controller.get_order(int(textbox_order_number_second.get()))
    except:
        label_output["text"] = "Ошибка"


# buttons

button_get_catalog=tk.Button(window)
button_get_catalog["text"] = "Получить \nкаталог"
button_get_catalog.place(x=550,y=70,width=100,height=35)
button_get_catalog["command"] = button_get_catalog_command

button_add_order=tk.Button(window)
button_add_order["text"] = "Добавить \nзаказ"
button_add_order.place(x=550,y=150,width=100,height=35)
button_add_order["command"] = button_add_order_command

button_get_order=tk.Button(window)
button_get_order["text"] = "Получить \nзаказ"
button_get_order.place(x=550,y=440,width=100,height=35)
button_get_order["command"] = button_get_order_command

button_add_product=tk.Button(window)
button_add_product["text"] = "Добавить \nпродукт"
button_add_product.place(x=550,y=250,width=100,height=35)
button_add_product["command"] = button_add_product_command

button_remove_product=tk.Button(window)
button_remove_product["text"] = "Удалить \nпродукт"
button_remove_product.place(x=550,y=290,width=100,height=35)
button_remove_product["command"] = button_remove_product_command

button_form_order=tk.Button(window)
button_form_order["text"] = "Сформировать \nзаказ"
button_form_order.place(x=550,y=360,width=100,height=35)
button_form_order["command"] = button_form_order_command

button_cancel_order=tk.Button(window)
button_cancel_order["text"] = "Отменить \nзаказ"
button_cancel_order.place(x=550,y=400,width=100,height=35)
button_cancel_order["command"] = button_cancel_order_command


# labels

label_address=tk.Label(window)
label_address["bg"] = BACKGROUND_COLOR
label_address["text"] = "Адрес"
label_address.place(x=830,y=150,width=118,height=30)

label_order_number_first=tk.Label(window)
label_order_number_first["bg"] = BACKGROUND_COLOR
label_order_number_first["text"] = "Номер заказа"
label_order_number_first.place(x=670,y=250,width=78,height=30)

label_product_number=tk.Label(window)
label_product_number["bg"] = BACKGROUND_COLOR
label_product_number["text"] = "Номер продукта"
label_product_number.place(x=770,y=250,width=96,height=32)

label_number=tk.Label(window)
label_number["bg"] = BACKGROUND_COLOR
label_number["text"] = "Количество"
label_number.place(x=890,y=253,width=70,height=25)

label_order_number_second=tk.Label(window)
label_order_number_second["bg"] = BACKGROUND_COLOR
label_order_number_second["text"] = "Номер заказа"
label_order_number_second.place(x=670,y=360,width=86,height=30)

label_output_name=tk.Label(window)
label_output_name["bg"] = BACKGROUND_COLOR
label_output_name["text"] = "Вывод"
label_output_name.place(x=210,y=60,width=70,height=25)


if __name__ == "__main__":
    window.mainloop()
