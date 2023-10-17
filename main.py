import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


# Function to handle image upload
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image_path.set(file_path)


# Function to add watermark to the image
def add_watermark():
    image_file = image_path.get()
    watermark_text = watermark_entry.get()
    watermark_x = int(x_entry.get())
    watermark_y = int(y_entry.get())

    if image_file and watermark_text:
        image = Image.open(image_file)
        draw = ImageDraw.Draw(image)
        width, height = image.size

        # Set watermark text font and size
        font = ImageFont.truetype("arial.ttf", 50)

        # Calculate watermark position
        x = watermark_x
        y = watermark_y

        # Add watermark text to the image
        draw.text((x, y), watermark_text, font=font, fill=(128, 128, 128, 128))

        # Save the modified image
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            image.save(save_path)
            result_label.config(text="Watermark added successfully!")
    else:
        result_label.config(text="Please select an image and enter a watermark text.")


# Create the main application window
window = tk.Tk()
window.title("Image Watermarking App")

# Create and position the widgets
upload_button = tk.Button(window, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

image_path = tk.StringVar()
image_entry = tk.Entry(window, textvariable=image_path, state="readonly", width=40)
image_entry.pack(pady=5)

watermark_label = tk.Label(window, text="Enter Watermark Text:")
watermark_label.pack()

watermark_entry = tk.Entry(window, width=40)
watermark_entry.pack(pady=5)

x_label = tk.Label(window, text="Enter Watermark X (0 = Top):")
x_label.pack()

x_entry = tk.Entry(window, width=40)
x_entry.pack(pady=5)

y_label = tk.Label(window, text="Enter Watermark Y (0 = Left):")
y_label.pack()

y_entry = tk.Entry(window, width=40)
y_entry.pack(pady=5)

add_button = tk.Button(window, text="Add Watermark", command=add_watermark)
add_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

# Start the application
window.mainloop()