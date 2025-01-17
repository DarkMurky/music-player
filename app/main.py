import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Music Player')
        self.geometry('620x210')
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()

    app.mainloop()
