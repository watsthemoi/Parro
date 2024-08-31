import tkinter as tk
# from [folder].[page] import [def to display page]
# from [folder].[page] import [def to display page]

# Variable Naming Convention
# Frame = frm_name
# Label = lbl_name
# Button = btn_name
# Entry = ent_name
# Text = txt_name

def main():
    root = tk.Tk()
    root.title("Parro")

    # Configure root to resize frame
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Create window frame
    frm_window = tk.Frame(root, bg="#606060", width=200, height=150) # Minimized page will start off as this size
    frm_window.pack(fill="both", expand=True) # Frame expands with page

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
    lbl_title = tk.Label(frm_window, text="Parro", font=("Arial", 50), fg="white", bg="#606060")
    lbl_title.grid(row=0, column=0, sticky="w", padx=20, pady=(80,10)) # Sticky w means stick to the west
                                       # Adjust pady to lower or raise title: n from top, and m from bottom

    # Create a sub-frame for the buttons to manage them together
    btn_frame = tk.Frame(frm_window, bg="#606060")
    btn_frame.grid(row=1, column=1, sticky="e", padx=20, pady=(80, 10))  # Sticky e means stick to the east

    # Add Buttons to the right side of the frame
    btn_new_composition = tk.Button(btn_frame, text='New Composition', width=25)
    btn_new_composition.pack(side=tk.TOP) 

    btn_new_recording = tk.Button(btn_frame, text='New Recording', width=25)
    btn_new_recording.pack(side=tk.TOP)

    btn_resume_composition = tk.Button(btn_frame, text='Resume Composition', width=25)
    btn_resume_composition.pack(side=tk.TOP) 



    root.mainloop()

if __name__ == "__main__":
    main()