from tkinter import *
from tkinter import filedialog


def main():
    root = Tk()
    root.title("Time Stamp Stripper")
    root.geometry("500x500")
    # root.configure(bg="#000000")
    """get_text = Entry(root, width=50, borderwidth=1)
    get_text.grid(row=0, column=0, columnspan=4)
    get_text.focus()"""
    def browsefiles():
        global filename
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select a text file to strip", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        global text_file
        #text_file = get_text.get()
        text_file = filename
        with open(text_file) as file:
            for rfile in file:
                pos = rfile.find(':')  # find the time stamps
                remove = rfile[pos-2:pos+3]  # select the time stamps
                global result
                result = rfile.replace(remove, "")  # remove them
                # print(result.rstrip())
                display.insert(INSERT, str(result))
    """def strip_button():
        global text_file
        #text_file = get_text.get()
        text_file = filename
        with open(text_file) as file:
            for rfile in file:
                pos = rfile.find(':') #find the time stamps
                remove = rfile[pos-2:pos+3] #select the time stamps
                global result
                result = rfile.replace(remove, "") #remove them
                #print(result.rstrip())
                display.insert(INSERT,str(result))"""
    scrollbar = Scrollbar(root, orient="horizontal")
    display = Text(root, width=69, height=150, borderwidth=2, xscrollcommand=scrollbar.set)
    # display.focus()
    display.grid(row=1, column=0, columnspan=5)
    button_selectfile = Button(root, text="Select a text file", padx=5, pady=5, command=browsefiles)
    #button = Button(root, text="STRIP", padx=5, pady=5, command=strip_button)
    #button.grid(row=0, column=1)
    button_selectfile.grid(row=0, column=2)

    root.mainloop()


if __name__ == '__main__':
    main()
