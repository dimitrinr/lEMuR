import tkinter as tk
import tkinter.messagebox as msg
import subprocess

class ToolbarApp:
    def __init__(self, root):
        self.root = root
        toolbar = tk.Frame(root)
        
        about_btn = tk.Button(toolbar, text="ABOUT", command=self.show_about)
        about_btn.pack(side="left")
        
        exit_btn = tk.Button(toolbar, text="EXIT", command=root.quit)
        exit_btn.pack(side="left")

        potato_btn = tk.Button(toolbar, text="POTATO", command=self.run_command)
        potato_btn.pack(side="left")
        
        toolbar.pack(side="top", fill="x")

    def show_about(self):
        msg.showinfo("About", "Hello World")

    def run_command(self):
        subprocess.run(["echo", "hihi"], shell=True)

root = tk.Tk()
app = ToolbarApp(root)
root.mainloop()
