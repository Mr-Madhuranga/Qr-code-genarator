import qrcode
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x200")
        
        self.label = tk.Label(root, text="Enter text or URL:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.button.pack(pady=10)
        
    def generate_qr_code(self):
        text = self.entry.get()
        if text:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            img = qr.make_image(fill='black', back_color='white')
            
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png")])
            if file_path:
                img.save(file_path)
                messagebox.showinfo("Success", "QR Code generated and saved successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter text or URL to generate QR code.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
