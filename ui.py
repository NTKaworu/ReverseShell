import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("MakiaHack")
window.resizable(False, False)

def printText():
    text = "test"
    text_out = tk.Label(window, text=text, fg="green", font="Poppins")
    text_out.grid(row=1, column=0)

button = tk.Button(text="Start", command=printText)
button.grid(row=0, column=0)



if __name__ == "__main__":
    window.mainloop()