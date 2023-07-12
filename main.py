from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageGrab

window = Tk()
window.title("Add Watermark")
window.config(bg="white")
window.geometry('600x700+0+0')


def upload_image():
    filename = filedialog.askopenfilename()
    return filename


def save_image():
    save = ImageGrab.grab(bbox=(0, 50, 600, 650))
    save.show()
    save.save("watermark_image.png")


main_image = Image.open(f"{upload_image()}")
if main_image.height > main_image.width:
    calc = main_image.height / 600
    width = main_image.width / calc
    resize_main_image = main_image.resize((int(width), 600))
elif main_image.height < main_image.width:
    calc = main_image.width / 600
    height = main_image.height / calc
    resize_main_image = main_image.resize((600, int(height)))
else:
    resize_main_image = main_image.resize((600, 600))

canvas = Canvas(height=600, width=600, bg="white", highlightthickness=0)
uploaded_img = ImageTk.PhotoImage(resize_main_image)
canvas.create_image(300, 300, image=uploaded_img)
canvas.grid(row=1, column=1)

watermark_image = Image.open("15.png")
resize_image = watermark_image.resize((100, 100))
uploaded_water_img = ImageTk.PhotoImage(resize_image)

canvas.create_image(450, 500, image=uploaded_water_img)
canvas.grid(row=1, column=1)

save_button = Button(text="Save", command=save_image)
save_button.grid(row=2, column=1)

window.mainloop()
