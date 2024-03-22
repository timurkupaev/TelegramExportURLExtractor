import tkinter as tk
from tkinter import filedialog, messagebox, Text
import json
import os


class URLExtractorApp:
    def __init__(self):
        """Initialize the main application window and GUI components."""
        self.root = tk.Tk()
        self.initialize_gui()
        self.json_files = []

    def initialize_gui(self):
        """Set up the GUI layout, including buttons and the text display area."""
        self.root.title("URL Extractor")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.geometry('800x600+200+100')
        self.load_files_button = tk.Button(self.root, text="Load JSON Files", command=self.load_files)
        self.load_files_button.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.load_folder_button = tk.Button(self.root, text="Load Folder with JSON Files", command=self.load_folder)
        self.load_folder_button.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
        self.save_button = tk.Button(self.root, text="Save URLs to File", command=self.save_urls)
        self.save_button.grid(row=0, column=2, sticky='ew', padx=5, pady=5)
        self.output_text = Text(self.root, state='disabled', wrap='word', height=10)
        self.output_text.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=5, pady=5)
        self.root.grid_rowconfigure(1, weight=1)

    def load_folder(self):
        """
        Open a dialog for the user to select a folder. Then, find and list all JSON files
        within the selected folder and its subfolders.
        """
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return
        self.json_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".json"):
                    full_path = os.path.join(root, file)
                    self.json_files.append(full_path)
        if self.json_files:
            self.extract_urls()
        else:
            messagebox.showwarning("Warning", "No JSON files found in the selected folder.")

    def display_urls(self, urls):
        """
        Display the extracted URLs in the text widget.
        :param urls: A list of URLs to be displayed.
        """
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, tk.END)
        for url in urls:
            self.output_text.insert(tk.END, url + "\n")
        self.output_text.config(state='disabled')

    def load_files(self):
        """
        Open a dialog for the user to select one or more JSON files. Then, load these files
        for URL extraction.
        """
        self.json_files = filedialog.askopenfilenames(filetypes=[("JSON files", "*.json")])
        if self.json_files:
            print(f"Loaded files: {self.json_files}")
            self.extract_urls()

    def extract_urls(self):
        """
        Extract URLs from the loaded JSON files and display them in the text widget.
        """
        if not self.json_files:
            messagebox.showwarning("Warning", "No files loaded.")
            return
        self.extracted_urls = set()
        for file_path in self.json_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for message in data.get("messages", []):
                    if isinstance(message.get("text"), list):
                        for text_item in message["text"]:
                            if isinstance(text_item, dict) and text_item.get("type") == "link":
                                self.extracted_urls.add(text_item.get("text"))
        self.display_urls(list(self.extracted_urls))
    def save_urls(self):
        """
        Open a dialog for the user to choose a filename and location to save the extracted URLs
        to a text file.
        """
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialfile="extracted_urls.txt"
        )
        if not filepath:
            return
        if not hasattr(self, 'extracted_urls') or not self.extracted_urls:
            messagebox.showwarning("Warning", "No URLs extracted.")
            return
        with open(filepath, 'w', encoding='utf-8') as file:
            for url in self.extracted_urls:
                file.write(url + "\n")



if __name__ == "__main__":
    URLExtractor = URLExtractorApp()
    URLExtractor.root.mainloop()



