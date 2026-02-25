import tkinter as tk
import tkinter.font as tkFont
import socket
import platform
import uuid

dark_mode = True

def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    result_label.config(text=f"IP Address: {ip}")

def get_computer_name():
    name = platform.node()
    result_label.config(text=f"Computer Name is: {name}")

def get_mac():
    mac= ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                   for elements in range(0,48,8)][::-1])
    result_label.config(text=f"MAC Address: {mac}")

def get_all():
    ip = socket.gethostbyname(socket.gethostname())
    name = platform.node()
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                   for elements in range(0,48,8)][::-1])
    result_label.config(text=
        f"IP Address: {ip}\n\n"
        f"Computer Name is: {name}\n\n"
        f"MAC Address: {mac}"
    )

def toggle_theme():
    global dark_mode

    if dark_mode:
        root.config(bg="lightgrey")
        top_frame.config(bg="lightgrey")
        title_label.config(bg="lightgrey", fg="black")
        result_label.config(bg="lightgrey", fg="black")
        dark_mode = False
    else:
        root.config(bg="black")
        top_frame.config(bg="black")
        title_label.config(bg="black", fg="lime")
        result_label.config(bg="black", fg="lime")
        dark_mode = True

root = tk.Tk()
root.title("WIM Utility")
root.geometry("450x400")
root.config(bg="black")

# Top frame for button
top_frame = tk.Frame(root, bg=root["bg"], height=40)
top_frame.pack(side="top", fill="x")
top_frame.pack_propagate(False)  # prevent shrinking

# Place the button in this frame
btn_theme = tk.Button(top_frame, text="🌙", font=("Arial", 10), width=3, command=toggle_theme)
btn_theme.place(relx=1.0, x=-10, rely=0.5, anchor="e")

title_label = tk.Label(root, text="WIM Utility", font=("Sitka Heading Semibold", 20), bg="black", fg="lime")
title_label.pack(pady=10)

btn_ip = tk.Button(root, text="IP Address", width=20, command=get_ip)
btn_ip.pack(pady=5)

btn_name = tk.Button(root, text="Computer Name", width=20, command=get_computer_name)
btn_name.pack(pady=5)

btn_mac = tk.Button(root, text="MAC Address", width=20, command=get_mac)
btn_mac.pack(pady=5)

btn_all = tk.Button(root, text="All", width=20, command=get_all)
btn_all.pack(pady=5)

result_label = tk.Label(root, text="", fg="lime", bg="black", wraplength=350)
result_label.pack(pady=20)

btn_theme = tk.Button(
    root,
    text="🌙",
    font=("Arial", 10),
    width=3,
    command=toggle_theme
)





root.mainloop()