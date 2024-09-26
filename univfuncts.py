"""Universal Functions for Pages"""

import customtkinter as ctk

class UniversalPageFunctions:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def slide(self, frame_in, frame_out, direction="left", duration=300):
        """Sliding Animation Parameters"""
        frame_out.place_forget()
        
        if direction == "left":
            frame_in.place(x=-frame_in.winfo_width(), y=frame_in.winfo_y())
            target_x = 0
            target_y = frame_in.winfo_y()
        elif direction == "right":
            frame_in.place(x=self.parent.winfo_width(), y=frame_in.winfo_y())
            target_x = self.parent.winfo_width() - frame_in.winfo_width()
            target_y = frame_in.winfo_y()
        elif direction == "up":
            frame_in.place(x=frame_in.winfo_x(), y=-frame_in.winfo_height())
            target_x = frame_in.winfo_x()
            target_y = 0
        elif direction == "down":
            frame_in.place(x=-frame_in.winfo_width(), y=frame_in.winfo_y())
            target_x = frame_in.winfo_x()
            target_y = self.parent.winfo_height() - frame_in.winfo_height()
        else:
            raise ValueError("Invalid direction")      

        self.animate_slide(frame_in, target_x, target_y, duration)

    def animate_slide(self, frame, target_x, target_y, duration=300):
        """Handles sliding animation using update method"""
        change_x = (target_x - frame.winfo_x()) / (duration / 10)
        change_y = (target_y - frame.winfo_y()) / (duration / 10) if target_y is not None else 0

        def update():
            new_x = frame.winfo_x() + change_x
            new_y = frame.winfo_y() + change_y 

            frame.place(x=new_x, y=new_y)
            if((change_x > 0 and new_x < target_x) or (change_x < 0 and new_x > target_x) 
                or (change_y > 0 and new_y < target_y) or (change_y < 0 and new_y > target_y)): 
                self.parent.after(10, update)

        update()                   
            
            
