import tkinter as tk
from tkinter import filedialog, messagebox
import re


class TextProcessorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Processor")

        # Input Text
        self.input_text = tk.Text(self.window, height=10, width=50)
        self.input_text.pack()

        # Open Button
        self.open_button = tk.Button(self.window, text="Open File", command=self.open_file)
        self.open_button.pack()

        # Process Button
        self.process_button = tk.Button(self.window, text="Process", command=self.process_text)
        self.process_button.pack()

    def open_file(self):
        # Open a file dialog to select a file
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        # Read the contents of the selected file
        if file_path:
            with open(file_path, 'r') as file:
                file_contents = file.read()

            # Set the file contents as the input text
            self.input_text.delete('1.0', tk.END)
            self.input_text.insert(tk.END, file_contents)

    def process_text(self):
        # Get the input text
        text = self.input_text.get("1.0", tk.END)

        # Remove duplicate words while preserving order
        processed_text = self.remove_duplicates(text)

        # Save the processed text to a new file
        self.save_to_file(processed_text)

    def remove_duplicates(self, text):
        # Use regular expressions to find unique words while preserving order
        unique_words = []
        seen_words = set()
        for word in re.findall(r'\b\w+\b', text):
            if word not in seen_words:
                unique_words.append(word)
                seen_words.add(word)

        processed_text = ' '.join(unique_words)

        return processed_text

    def save_to_file(self, text):
        # Save the processed text to a new file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text)

            messagebox.showinfo("Text Processor", "Processed text saved successfully.")

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    # Create an instance of the GUI
    gui = TextProcessorGUI()
    gui.run()
