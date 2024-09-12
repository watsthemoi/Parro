import json
import customtkinter as ctk
from PIL import Image, ImageTk

# Function to load JSON data from a file
def load_json_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

class Main(ctk.CTk):
    def __init__(self, json_data):
        super().__init__()
        
        # Extract the main window parameters
        main_data = json_data.get("MAIN-1", {})
        main_params = main_data.get("parameters", {})
        self.title(main_params.get("title", "Parro"))
        self.geometry(f"{main_params.get('width', 800)}x{main_params.get('height', 500)}")
        
        # Set the theme
        ctk.set_appearance_mode("dark")  # You can choose 'light' or 'dark'
        ctk.set_default_color_theme(main_data.get("theme", "dark-blue"))

        # Create the options frame
        options_frame_data = main_data.get("OPTIONSFRAME", {})
        options_frame = ctk.CTkFrame(self)
        options_frame.pack(**options_frame_data.get("pack_options", {}))

        # Add components to the frame
        self.create_textbox(options_frame, options_frame_data.get("TB_TITLE"))
        self.create_button(options_frame, options_frame_data.get("BTN_HOME"))
        self.create_button(options_frame, options_frame_data.get("BTN_NEWCOMP"))
        self.create_button(options_frame, options_frame_data.get("BTN_NEWRECORDING"))
        self.create_textbox(options_frame, options_frame_data.get("TB_RECORDINGS"))
        self.create_button(options_frame, options_frame_data.get("BTN_RESUMERECORDING"))
        self.create_textbox(options_frame, options_frame_data.get("TB_COMPOSITIONS"))
        self.create_button(options_frame, options_frame_data.get("BTN_RESUMECOMPOSITION"))

    def create_textbox(self, parent, textbox_data):
        if not textbox_data:
            return

        textbox = ctk.CTkLabel(
            parent,
            text=textbox_data.get("parameters", {}).get("text", ""),
            text_color=textbox_data.get("parameters", {}).get("text_color", ["#ffffff", "#ffffff"])[0],
            height=textbox_data.get("parameters", {}).get("height", 25),
            anchor=textbox_data.get("parameters", {}).get("anchor", "w"),
            font=(textbox_data.get("parameters", {}).get("font_family", "Fixedsys"),
                  textbox_data.get("parameters", {}).get("font_size", 15))
        )
        # Ensure left alignment using anchor="w"
        textbox.pack(
            **textbox_data.get("pack_options", {})
        )

    def create_button(self, parent, button_data):
        if not button_data:
            return

        button_params = button_data.get("parameters", {})
        image_data = button_params.get("image", {})
        
        # Load the image
        if image_data:
            img = Image.open(image_data.get("image"))
            img = img.resize(image_data.get("size", [18, 18]))
            button_image = ImageTk.PhotoImage(img)
        else:
            button_image = None

        button = ctk.CTkButton(
            parent,
            text=button_params.get("text", ""),
            fg_color=button_params.get("fg_color", ["#212121", "#212121"])[0],
            text_color=button_params.get("text_color", ["#ffffff", "#ffffff"])[0],
            hover_color=button_params.get("hover_color", ["#ff8080", "#ff5e5e"])[0],
            image=button_image,
            font=(button_params.get("font_family", "Fixedsys"), button_params.get("font_size", 15)),
            width=button_params.get("width", 180),
            anchor=button_params.get("anchor", "w"),
        )
        # Ensure left alignment using anchor="w"
        button.pack(
            **button_data.get("pack_options", {})
        )

if __name__ == "__main__":
    # Load the JSON configuration from an external file
    json_file_path = "assets/Parro.json" # Path to your JSON file
    json_data = load_json_from_file(json_file_path)
    
    app = Main(json_data)
    app.mainloop()