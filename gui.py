from pathlib import Path
import psutil
import subprocess
from tkinter import Tk, Canvas, PhotoImage, messagebox
from time import time
import os

def relative_to_assets(path):
    return  f'{os.getcwd()}/assets/frame0/{path}'

# Store the application start time
app_start_time = time()

def get_cpu_load():
    try:
        cpu_load = psutil.cpu_percent(interval=1)
        return round(cpu_load, 2)
    except Exception as e:
        print(f"Error getting CPU load: {e}")
        return None

def get_ram_usage():
    try:
        ram = psutil.virtual_memory()
        return ram.percent
    except Exception as e:
        print(f"Error getting RAM usage: {e}")
        return None

def get_system_uptime():
    try:
        uptime = time() - app_start_time
        return round(uptime / 60, 2)  # Convert to minutes
    except Exception as e:
        print(f"Error getting system uptime: {e}")
        return None

def shutdown():
    try:
        subprocess.run(["shutdown", "/s", "/t", "1"])
    except Exception as e:
        print(f"Error shutting down: {e}")

def restart():
    try:
        subprocess.run(["shutdown", "/r", "/t", "1"])
    except Exception as e:
        print(f"Error restarting: {e}")

def on_close():
    # Display a confirmation dialog before closing the application
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        window.destroy()

def update_information():
    cpu_load = get_cpu_load()
    ram_usage = get_ram_usage()
    system_uptime = get_system_uptime()

    if cpu_load is not None:
        canvas.itemconfig(cpu_text, text=f"CPU: {cpu_load}%")

    if ram_usage is not None:
        canvas.itemconfig(ram_text, text=f"Dung lượng RAM: {ram_usage}%")

    if system_uptime is not None:
        canvas.itemconfig(uptime_text, text=f"Thời gian: {system_uptime} phút")

    window.after(1000, update_information)  # Update every 1000 milliseconds (1 second)

window = Tk()

window.geometry("366x218+{}+{}".format(window.winfo_screenwidth() - 366, 0))
window.configure(bg="#FFFFFF")
window.title("Trạng thái máy tính")  # Set your desired window title
window.overrideredirect(True)  # Hide the title bar
window.wm_attributes("-topmost", 0)  # Keep the window on top

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=218,
    width=366,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_AnhNen = PhotoImage(
    file=relative_to_assets("AnhNen.png"))
AnhNen = canvas.create_image(
    183.0,
    109.0,
    image=image_AnhNen
)

cpu_text = canvas.create_text(
    44.0,
    28.0,
    anchor="nw",
    text="CPU:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

ram_text = canvas.create_text(
    44.0,
    67.0,
    anchor="nw",
    text="Dung lượng RAM:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

uptime_text = canvas.create_text(
    44.0,
    114.0,
    anchor="nw",
    text="Thời gian:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    267.0,
    191.0,
    anchor="nw",
    text="duyvo26.xyz",
    fill="#000000",
    font=("Inter", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    54.0,
    175.0,
    image=image_image_1,
    tags="shutdown_img"
    
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    112.0,
    175.0,
    image=image_image_2,
    tags="restart_img"
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    20.0,
    78.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    22.0,
    34.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    22.0,
    121.0,
    image=image_image_5
)

canvas.create_text(
    42.0,
    200.0,
    anchor="nw",
    text="Tắt máy",
    fill="#000000",
    font=("Inter", 8 * -1),
    tags="shutdown_button"
)

canvas.create_text(
    93.0,
    202.0,
    anchor="nw",
    text="Khởi động lại",
    fill="#000000",
    font=("Inter", 8 * -1),
    tags="restart_button"
)

# Event bindings for the shutdown and restart buttons
canvas.tag_bind("shutdown_button", "<Button-1>", lambda event: shutdown())
canvas.tag_bind("shutdown_img", "<Button-1>", lambda event: shutdown())
canvas.tag_bind("restart_button", "<Button-1>", lambda event: restart())
canvas.tag_bind("restart_img", "<Button-1>", lambda event: restart())

window.resizable(False, False)
window.after(1000, update_information)  # Start the update loop
window.mainloop()
