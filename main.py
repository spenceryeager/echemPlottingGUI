import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Test GUI")

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=100, pady=200)
        tk.Label(dialog_frame, text='This will be the future GUI to do all my electrochemistry plotting!').pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()