import tkinter as tk
from tkinter import filedialog, messagebox
import base64
import os

class Base64ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Base64 Image Encoder/Decoder")
        self.root.geometry("400x200")
        
        self.encode_btn = tk.Button(root, text="Mã hóa ảnh sang Base64", command=self.encode_image)
        self.encode_btn.pack(pady=20)
        
        self.decode_btn = tk.Button(root, text="Giải mã Base64 thành ảnh", command=self.decode_image)
        self.decode_btn.pack(pady=20)

    def encode_image(self):
        img_path = filedialog.askopenfilename(
            title="Chọn file ảnh",
            filetypes=[
                ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.heic"),
                ("PNG Image", "*.png"),
                ("JPEG Image", "*.jpg;*.jpeg"),
                ("Bitmap Image", "*.bmp"),
                ("GIF Image", "*.gif"),
                ("HEIC Image", "*.heic")
            ]
        )
        if not img_path:
            return
        try:
            with open(img_path, "rb") as img_file:
                b64_str = base64.b64encode(img_file.read()).decode('utf-8')
            # Lấy tên file gốc không có phần mở rộng
            base_name = os.path.splitext(os.path.basename(img_path))[0]
            default_txt_name = base_name + ".txt"
            save_path = filedialog.asksaveasfilename(
                title="Lưu file Base64",
                defaultextension=".txt",
                initialfile=default_txt_name,
                filetypes=[("Text Files", "*.txt")]
            )
            if save_path:
                with open(save_path, "w") as txt_file:
                    txt_file.write(b64_str)
                messagebox.showinfo("Thành công", f"Đã mã hóa và lưu vào {save_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def decode_image(self):
        txt_path = filedialog.askopenfilename(title="Chọn file Base64 (.txt)", filetypes=[("Text Files", "*.txt")])
        if not txt_path:
            return
        try:
            with open(txt_path, "r") as txt_file:
                b64_str = txt_file.read()
            img_data = base64.b64decode(b64_str)
            save_path = filedialog.asksaveasfilename(title="Lưu file ảnh", defaultextension=".png", filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg;*.jpeg"), ("Bitmap Image", "*.bmp"), ("GIF Image", "*.gif")])
            if save_path:
                with open(save_path, "wb") as img_file:
                    img_file.write(img_data)
                messagebox.showinfo("Thành công", f"Đã giải mã và lưu vào {save_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = Base64ImageApp(root)
    root.mainloop()
