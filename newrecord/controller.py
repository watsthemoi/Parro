from newrecord.views import NewRecordView
# Function to switch to the newrecord view
def openNewRecordView(root):
    # Remove the current widgets (from the homepage view)
    for widget in root.winfo_children():
        widget.destroy()  # Clear the current content of the window

    # Create and display the NewRecordView within the same window
    app = NewRecordView(root)  # Pass the existing window to the new view
    app.pack(fill="both", expand=True)  # Ensure it fills the window space