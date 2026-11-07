#!/usr/bin/env python3

import subprocess
import tkinter as tk
from tkinter import ttk


def show_keyboard():
    subprocess.run(
        [
            "busctl",
            "--user",
            "call",
            "sm.puri.OSK0",
            "/sm/puri/OSK0",
            "sm.puri.OSK0",
            "SetVisible",
            "b",
            "true",
        ],
        check=False,
    )


def entry_touched(event):
    selected_entry = event.widget

    # Allow Tk's normal button-release processing to finish.
    root.after(
        50,
        lambda: activate_entry(selected_entry)
    )


def activate_entry(selected_entry):
    # Initially select the entry.
    selected_entry.focus_set()
    selected_entry.icursor(tk.END)

    # Bring up Squeekboard.
    show_keyboard()

    # Squeekboard appearing may disturb the XWayland focus.
    # Restore it once the keyboard is visible.
    root.after(
        400,
        lambda: restore_focus(selected_entry)
    )


def restore_focus(selected_entry):
    root.lift()
    selected_entry.focus_force()
    selected_entry.icursor(tk.END)

    print("Restored focus to:", root.focus_get())


root = tk.Tk()
root.title("Tkinter Keyboard Focus Test")
root.geometry("600x300")

label = ttk.Label(
    root,
    text="Tap the entry and type using the on-screen keyboard",
    font=("Helvetica", 16),
)
label.pack(pady=30)

entry = ttk.Entry(
    root,
    font=("Helvetica", 24),
    width=25,
)
entry.pack(padx=30, pady=20)

entry.bind(
    "<ButtonRelease-1>",
    entry_touched,
    add="+",
)

exit_button = ttk.Button(
    root,
    text="Exit",
    command=root.destroy,
)
exit_button.pack(pady=20)

root.mainloop()