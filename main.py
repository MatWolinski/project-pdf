import tkinter as tk
from tkinter import filedialog
import pypdf
import os

from pypdf import PdfMerger, PdfWriter


class AppGUI:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("ProjectPDF - free PDF manipulation tool")

        self.label = tk.Label(self.root, text="What do you want to do with your PDF?", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.buttonframe = tk.Frame(self.root)

        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.btn0 = tk.Button(self.buttonframe, text = "Merge", pady=10, padx=10, font=('Arial', 18), command=self.show_merge_menu)
        self.btn0.grid(row=0, column=0)

        self.buttonframe.pack(fill='x')
        self.root.mainloop()

    def show_merge_menu(self):
        def __init__(self):
            self.rootm = tk.Tk()
            self.rootm.geometry("500x500")
            self.rootm.title("ProjectPDF - free PDF manipulation tool - Merge")

            self.labelm = tk.Label(self.root, text="Choose PDFs to merge?", font=('Arial', 18))
            self.labelm.pack(padx=10, pady=10)

            self.btnm0 = tk.Button(text = "Select your PDFs to merge", pady=10, padx=10, font=('Arial', 18), command=self.select_path())
            self.btnm0.pack(self.rootm)

            self.rootm.mainloop()

    def select_path(self):
        # merger = PdfWriter()
        self.filez = filedialog.askopenfilename()
AppGUI()
