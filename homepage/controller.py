from homepage.views import HomePageView

def run_homepage():
    app = HomePageView()
    app.geometry("800x500")
    app.iconbitmap("icon.ico")
    app.title("Parro")
    app.configure(fg_color=['gray92', 'gray14'])
    app.mainloop()