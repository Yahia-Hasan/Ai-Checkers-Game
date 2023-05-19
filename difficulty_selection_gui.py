import tkinter as tk

class DifficultySelectionGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Select Difficulty Level")

        # Set up the buttons
        button_font = ("Helvetica", 20)
        easy_button = tk.Button(self.root, text="Easy", font=button_font, command=lambda: self.select_difficulty("easy"))
        medium_button = tk.Button(self.root, text="Medium", font=button_font, command=lambda: self.select_difficulty("medium"))
        hard_button = tk.Button(self.root, text="Hard", font=button_font, command=lambda: self.select_difficulty("hard"))

        # Pack the buttons into the window
        easy_button.pack(pady=10)
        medium_button.pack(pady=10)
        hard_button.pack(pady=10)

        self.difficulty = None

        # Center the window on the screen
        self.center_window()

        # Set the size and background color of the window
        self.root.geometry("400x300")
        self.root.configure(bg="#000000")

    def select_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.root.destroy()

    def run(self):
        self.root.mainloop()

    def center_window(self):
        # Get the size of the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position of the window
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)

        # Set the position of the window
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and run the GUI
