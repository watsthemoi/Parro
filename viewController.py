import customtkinter as ctk
from homepage.views import HomePageView
from newrecord.views import NewRecordView

class ViewManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("Parro")
        self.iconbitmap("icon.ico")

        # Initially set the home page
        self.show_homepage()

    def show_homepage(self):
        # Clear current frame
        self.clear_frame()

        # Load and display the HomePageView
        homepage = HomePageView(self)
        homepage.configure(fg_color=['gray92', 'gray14'])
        homepage.pack(fill="both", expand=True)

    def show_newrecord(self):
        # Clear current frame
        self.clear_frame()

        # Load and display the NewRecordView
        new_record = NewRecordView(self)
        new_record.configure(fg_color=['gray92', 'gray14'])
        new_record.pack(fill="both", expand=True)

    def clear_frame(self):
        # Remove all widgets in the current frame
        for widget in self.winfo_children():
            widget.destroy()