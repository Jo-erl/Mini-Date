import tkinter as tk
from datetime import datetime
from tkinter import font as tkfont

def update_date():
    """Update the date label with the current date."""
    current_date = datetime.now().strftime('%b %d, %Y')
    canvas.itemconfig(date_text, text=current_date)
    canvas.after(1000, update_date)  # Call this function again after 1000ms (1 second)

def on_drag_start(event):
    """Start dragging the window."""
    root.x = event.x
    root.y = event.y

def on_drag_motion(event):
    """Move the window during dragging."""
    delta_x = event.x - root.x
    delta_y = event.y - root.y
    new_x = root.winfo_x() + delta_x
    new_y = root.winfo_y() + delta_y
    root.geometry(f'+{new_x}+{new_y}')

# Create the main window
root = tk.Tk()
root.title("Mini Digital Date")

# Remove window border and title bar
root.overrideredirect(True)

# Make the window always on top
root.attributes('-topmost', True)

# Set the dimensions and style of the window
width = 112
height = 40
root.geometry(f"{width}x{height}")

# Calculate initial position (center-right of the screen with padding)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - width - 20  # 20 pixels from the right edge
y = (screen_height // 2) - (height // 2)  # Center vertically
root.geometry(f"{width}x{height}+{x}+{y}")

root.configure(bg='black')  # Background color

# Load the custom font with fallback
def get_font(family, size, weight):
    try:
        return tkfont.Font(family=family, size=size, weight=weight)
    except tkfont.TclError:
        print(f"Font {family} not found. Using Arial as fallback.")
        return tkfont.Font(family="Arial", size=size, weight=weight)

custom_font = get_font('Poppins', 13, 'bold')

# Create a canvas to draw the rectangle
canvas = tk.Canvas(root, bg='black', bd=0, highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Draw the rectangle
canvas.create_rectangle(
    10, 2, width - 10, height - 2,
    fill='black', outline='black'
)

# Create the date text on the canvas
date_text = canvas.create_text(
    width // 2, height // 2,
    text='', font=custom_font, fill='white'
)

# Call the update_date function
update_date()

# Make the window draggable
canvas.bind('<Button-1>', on_drag_start)
canvas.bind('<B1-Motion>', on_drag_motion)

# Run the Tkinter event loop
root.mainloop()