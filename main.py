import tkinter as tk
import tkinter.filedialog as fd
from pypdf import PdfWriter


class AppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("ProjectPDF - free PDF manipulation tool")

        self.label = tk.Label(self.root, text="What do you want to do with your PDF?", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.btn0 = tk.Button(self.buttonframe, text="Merge", pady=10, padx=10, font=('Arial', 18), command=self.create_merge_window)
        self.btn0.grid(row=0, column=0)

        self.buttonframe.pack(fill='x')
        self.root.mainloop()

    def create_merge_window(self):
        merge_window = tk.Toplevel()
        merge_window.title('Merge PDF!')
        merge_window.geometry('400x400')

        self.selected_files = []

        merger_window_frame = tk.Frame(merge_window)
        merger_window_frame.columnconfigure(0, weight=1)
        merger_window_frame.columnconfigure(1, weight=1)
        merger_window_frame.columnconfigure(2, weight=1)

        merger_label = tk.Label(merger_window_frame, text="PDF Merger")
        merger_label.grid(row=0, column=1)

        mrg_btn0 = tk.Button(merger_window_frame, text='Select files to merge', command=self.select_pdf_file)
        mrg_btn0.grid(row=1, column=0)

        merger_window_frame.pack()

    def select_pdf_file(self):
        file_path = fd.askopenfilename()
        if file_path:
            self.selected_files.append(file_path)
            print(f"Selected file: {file_path}")


def merge_pdf(write_path, name, *args):
    try:
        merger = PdfWriter()

        for pdf in args:
            merger.append(pdf)

        merger.write(write_path + name + ".pdf")
        merger.close()
    except Exception as e:
        print(e)


AppGUI()
