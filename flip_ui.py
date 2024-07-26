import tkinter as tk
import subprocess
import os

class FlipApp:
    def __init__(self, root):
        self.root = root
        root.title("FLIP Application")
        
        self.label = tk.Label(root, text="Welcome to FLIP!", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        self.run_button = tk.Button(root, text="Run FLIP", command=self.run_flip)
        self.run_button.pack(pady=10)
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)
    
    def run_flip(self):
        # Command to run the software
        # Ensure 'main.py' is in the same directory as the executable
        flip_command = os.path.join(os.path.dirname(__file__), "main.py")
        
        subprocess.run(["python", flip_command])

if __name__ == "__main__":
    root = tk.Tk()
    app = FlipApp(root)
    root.geometry("300x200")
    root.mainloop()
