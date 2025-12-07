#خالد احمد محمود محمد         سكشن ٤
from tkinter import Tk, Label, Entry, Text, Button, messagebox

# ===== Main Window =====
r = Tk()
r.geometry("430x460")
r.title("REVIEW Form")
r.configure(bg="#0A1A2F")

# ===== Title =====
Label(
    r,
    text="Share Your REVIEW",
    font=("Segoe UI", 20, "bold"),
    bg="#0A1A2F",
    fg="#E0E6ED"
).pack(pady=25)

# ===== Name Field =====
Label(
    r,
    text="Full Name:",
    font=("Segoe UI", 12, "bold"),
    bg="#0A1A2F",
    fg="#AAB7C4"
).pack()
name = Entry(
    r,
    font=("Segoe UI", 12),
    width=32,
    bg="#132742",
    fg="white",
    insertbackground="white",
    bd=1,
    relief="flat"
)
name.pack(pady=6)

# ===== Rating Field =====


# ===== Comment Field =====
Label(
    r,
    text="Your Comments:",
    font=("Segoe UI", 12, "bold"),
    bg="#0A1A2F",
    fg="#AAB7C4"
).pack()
comment = Text(
    r,
    width=32,
    height=5,
    font=("Segoe UI", 12),
    bg="#132742",
    fg="white",
    insertbackground="white",
    bd=1,
    relief="flat"
)
comment.pack(pady=6)

# ===== Button Function =====
def submit_REVIEW():
    n = name.get()
    rt = rating.get()
    c = comment.get("1.0", "end").strip()

    if n == "" or rt == "" or c == "":
        messagebox.showerror("Error", "Please fill all fields!")
        return

    if not rt.isdigit() or not (1 <= int(rt) <= 5):
        messagebox.showerror("Error", "Rating must be between 1 and 5.")
        return

    messagebox.showinfo("Submitted", "Your feedback has been sent. Thank you!")

# ===== Submit Button =====
Button(
    r,
    text="Submit REVIEW",
    command=submit_REVIEW,
    bg="#1A3A5F",
    fg="white",
    activebackground="#244A74",
    activeforeground="white",
    font=("Segoe UI", 13, "bold"),
    width=18,
    height=1,
    bd=0,
    relief="flat"
).pack(pady=25)


r.mainloop()
