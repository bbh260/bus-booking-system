import tkinter as tk
from admin_screens import admin
from database import database_manager
from user_screens import booking_screen
from user_screens import check_screen


class Application:
    def __init__(self):
        self.root = None
        self.admin_screen = admin.ApplicationAdmin()
        self.booking_screen = booking_screen.BookingScreen()
        self.check_screen = check_screen.BookingCheckScreen()
        self.database_manager = database_manager.DatabaseManager("221b124_db.db")

    def splash_screen(self):
        self.root = tk.Tk()
        self.root.title("Bus Booking System")
        self.root.geometry("860x650")
        
        self.root.config(bg="coral1")
        logo = tk.PhotoImage(file="bus_logo.png")
        label = tk.Label(self.root, image=logo, bg="coral1")
        label.grid(row=0, column=0, padx=250, pady=10)
        title = tk.Label(
            self.root,
            text="Bus Booking System",
            font=("Consolas", 30, "bold"),
            bg="coral4",
        )
        title.grid(row=1, column=0)
        name = tk.Label(
            self.root, text="Name: Bhavya Sharma", font=("Consolas", 15), bg="coral1"
        )
        name.grid(row=2, column=0, pady=5)
        eno = tk.Label(
            self.root,
            text="Enrollment No: 221B124",
            font=("Consolas", 15),
            bg="coral1",
        )
        eno.grid(row=3, column=0)
        mobile = tk.Label(
            self.root, text="Mobile: mobile", font=("Consolas", 15), bg="coral1"
        )
        mobile.grid(row=4, column=0)
        footer = tk.Label(
            self.root,
            text="Submitted To: Dr. Mahesh Kumar",
            font=("Consolas", 20, "bold"),
            bg="coral4",
        )
        footer.grid(row=5, column=0, pady=70)
        name = tk.Label(
            self.root,
            text="Project Based Learning (AP Lab 1)",
            font=("Consolas", 18),
            bg="coral1",
        )
        name.grid(row=6, column=0, pady=5)
        self.root.after(3000, self.home_screen)
        self.root.mainloop()

    def home_screen(self, caller_root: tk.Tk = None):
        if caller_root:
            caller_root.destroy()
        else:
            self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Bus Booking System | Home")
        self.root.geometry("860x650")
        
        self.root.config(bg="coral1")
        frame = tk.Frame(self.root, bg="coral1")
        logo = tk.PhotoImage(file="bus_logo.png")
        label = tk.Label(self.root, image=logo, bg="coral1")
        label.grid(row=0, column=0, padx=250, pady=10)
        title = tk.Label(
            self.root,
            text="Bus Booking System",
            font=("Consolas", 30, "bold"),
            bg="coral4",
        )
        title.grid(row=1, column=0)
        book_but = tk.Button(
            frame,
            text="Book Ticket",
            font=("Consolas", 12, "bold"),
            bg="coral4",
            fg="white",
            command=lambda: self.booking_screen.create_screen(
                self.root, self.home_screen, self.database_manager
            ),
        )
        book_but.grid(row=0, column=0, padx=5)
        check_but = tk.Button(
            frame,
            text="Check Ticket",
            font=("Consolas", 12, "bold"),
            bg="coral4",
            fg="white",
            command=lambda: self.check_screen.create_screen(
                self.root, self.home_screen, self.database_manager
            ),
        )
        check_but.grid(row=0, column=1, padx=5)
        add_but = tk.Button(
            frame,
            text="Add Bus",
            font=("Consolas", 12, "bold"),
            bg="coral4",
            fg="white",
            command=lambda: self.admin_screen.create_admin_screen(
                self.root, self.home_screen, self.database_manager
            ),
        )
        add_but.grid(row=0, column=2, padx=5)
        info_label = tk.Label(
            frame,
            text="For Admin Only",
            font=("Consolas", 10, "bold"),
            bg="coral3",
        )
        info_label.grid(row=1, column=2, pady=5)
        frame.grid(row=2, column=0, pady=100)
        self.root.mainloop()


app = Application()
app.splash_screen()