import tkinter as tk
# from [folder].[page] import [def to display page]
# from [folder].[page] import [def to display page]

def main():
    root = tk.Tk()
    root.title("Gray Rectangular Box Frame")

    # Configure root to resize frame
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Create frame
    frame = tk.Frame(root, bg="#606060", width=200, height=150) # Minimized page will start off as this size
    frame.pack(fill="both", expand=True) # Frame expands with page

    ## When you want to put the logo above the title
    # image = Image.open("[image_name].[file_type]")
    # image = image.resize(100, 100), Image.ANTIALIAS)
    # image = ImageTk.PhotoImage(image)
    ##

    ## Add image to box
    # i_label = tk.Label(frame, image=image, bg="#606060")
    # i_label.grid(row=0, column=0, sticky="w", padx=20, pady=(80,0)) # Adjusted to be placed above title
    ## 

    # Add title to box from right side
    title_label = tk.Label(frame, text="Title", font=("Arial", 50), fg="white", bg="#606060")
    title_label.grid(row=4, column=0, sticky="w", padx=20, pady=(80,10)) # Sticky w means stick to the west
                                       # Adjust pady to lower or raise title: n from top, and m from bottom



    root.mainloop()

if __name__ == "__main__":
    main()    