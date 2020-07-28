'''
tkauto_tpl.py
Used with tkauto.py and tkmenu.py
'''

from tkinter import *
# from tkinter.font import Font
# import requests, sys, os, csv, webbrowser
# from tkinter.filedialog import askopenfilename
# from tkinter import messagebox

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        # self.columnconfigure(1, weight=1, pad=100)
        # self.rowconfigure(1, weight=1, pad=20)

    # INSERT TKAUTO OUTPUT BELOW HERE
        menubar = Menu(root)
        mn_file = Menu(menubar, tearoff=0)
        mn_file.add_command(label="New", command=self.mn_file_new, accelerator="Ctrl-n", underline=1)
        mn_file.add_command(label="Open", command=self.nm_file_open)
        mn_file.add_command(label="Save", command=self.nm_file_save, accelerator="Ctrl-s", underline=1)
        mn_file.add_command(label="Save-As", command=self.nm_file_saveas)
        mn_file.add_separator()
        mn_file.add_command(label="Exit", command=self.nm_file_exit, accelerator="Ctrl-q")
        menubar.add_cascade(label="File", menu=mn_file)
        mn_edit = Menu(menubar, tearoff=0)
        mn_edit.add_command(label="Undo", command=self.mn_edit_undo, accelerator="Ctrl-z")
        mn_edit.add_command(label="Select All", command=self.mn_edit_selall, accelerator="Ctrl-a")
        submenu = Menu(mn_edit, tearoff=False)
        submenu.add_command(label="Copy", command=self.mn_edit_copy, accelerator="Ctrl-c")
        submenu.add_command(label="Paste", command=self.mn_edit_paste, accelerator="Ctrl-v")
        mn_edit.add_cascade(label="Clipboard", menu=submenu, underline=2)
        menubar.add_cascade(label="Edit", menu=mn_edit)
        mn_help = Menu(menubar, tearoff=0)
        mn_help.add_command(label="Help Index", command=self.mn_help_index)
        mn_help.add_command(label="About…", command=self.mn_help_about)
        menubar.add_cascade(label="Help", menu=mn_help)
        root.config(menu=menubar) # display the menu


    def mn_file_new(self):
        ''' docstring '''

    def nm_file_open(self):
        ''' docstring '''

    def nm_file_save(self):
        ''' docstring '''

    def nm_file_saveas(self):
        ''' docstring '''

    def nm_file_exit(self):
        ''' docstring '''

    def mn_edit_undo(self):
        ''' docstring '''

    def mn_edit_selall(self):
        ''' docstring '''

    def mn_edit_copy(self):
        ''' docstring '''

    def mn_edit_paste(self):
        ''' docstring '''

    def mn_help_index(self):
        ''' docstring '''

    def mn_help_about(self):
        ''' docstring '''


    # def eventHandler(self):
    #     pass

    # def eventHandler(self):
    #     pass

#

# def save_location():
#     ''' executes at WM_DELETE_WINDOW event '''
#     with open("winfoxy", "w") as fout:
#         fout.write(str(root.winfo_x()) + "\n" + str(root.winfo_y() - 24))
#     root.destroy()

root = Tk()

root.geometry("200x120") # WxH+left+top
#   or the following:
#   the following repositions the window from last time '''
# if os.path.isfile("winfoxy"):
#     lcoor = tuple(open("winfoxy", 'r'))  # no relative path for this
#     root.geometry('350x200+%d+%d'%(int(lcoor[0].strip()),int(lcoor[1].strip())))
# else:
#     root.geometry("350x200") # WxH+left+top

root.title("title")
# root.configure(background='#666')
# root.overrideredirect(True) # removed window decorations
# root.resizable(0,0) # no resize & removes maximize button
# root.protocol("WM_DELETE_WINDOW", save_location)
app = Application(root)
app.mainloop()
