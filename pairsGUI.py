# gui.py
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from mClosestPairs import closestPairs  # Import the function from the other file
from math import comb  # For computing combinations

class ClosestPairsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Closest Pairs Finder")
        self.root.geometry("800x1000")

        # Bind the window close event to a custom function
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Store points in a list
        self.points = []
        self.lines = []
        
        # Create the matplotlib figure and axis
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 10)  # x-axis from 0 to 10
        self.ax.set_ylim(0, 10)  # y-axis from 0 to 10
        self.ax.set_title('Click to add points')

        # Embedding the matplotlib figure into tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.mpl_connect('button_press_event', self.add_point)
        
        # Textbox for entering number of closest pairs
        self.label = tk.Label(root, text="Enter number of closest pairs (max: 0):")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        # Frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)  # Add vertical padding

        # Button to compute closest pairs
        self.find_button = tk.Button(self.button_frame, text="Find Closest Pairs", command=self.compute_closest_pairs)
        self.find_button.pack(side=tk.LEFT, padx=5)  # Add horizontal padding

        # Reset button
        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=5)  # Add horizontal padding

        # Frame for Listbox and Scrollbar
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)  # Allow the frame to expand

        # Listbox to display closest pairs
        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Make the Listbox expand

        # Scrollbar for Listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Listbox and Scrollbar
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def on_closing(self):
        # Close the application properly
        self.root.quit()
        self.root.destroy()

    def add_point(self, event):
        # Add a point on mouse click
        if event.xdata is not None and event.ydata is not None:
            self.points.append((event.xdata, event.ydata))
            self.ax.plot(event.xdata, event.ydata, 'bo')  # blue dot for point
            self.update_max_pairs()  # Update the max pairs when a new point is added
            self.canvas.draw()

    def update_max_pairs(self):
        max_pairs = comb(len(self.points), 2) if len(self.points) > 1 else 0
        self.label.config(text=f"Enter number of closest pairs (max: {max_pairs}):")
        
    def compute_closest_pairs(self):
        try:
            m = int(self.entry.get()) if self.entry.get() else 0  # Check if entry is not empty
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number")
            return
        
        if len(self.points) < 2:
            messagebox.showwarning("Insufficient Points", "Not enough points to find pairs.")
            return
        
        # Ensure m does not exceed max allowed
        max_pairs = comb(len(self.points), 2)
        if m > max_pairs:
            m = max_pairs
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(m))  # Update the entry box
        
        # Call the closest pair finding function from closest_pairs.py
        closest_pairs = closestPairs(self.points, m)
        
        # Clear the previous lines and the listbox
        self.clear_lines()
        self.listbox.delete(0, tk.END)  # Clear the listbox
        
        # Draw lines between closest pairs and populate the listbox
        for p1, p2, dist in closest_pairs:  # Unpack the points and distance
            # Draw the line and keep the points
            line, = self.ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-')  # red line between pairs
            self.lines.append(line)
            # Format the coordinates and distance for the listbox
            formatted_p1 = f"({p1[0]:.2f}, {p1[1]:.2f})"
            formatted_p2 = f"({p2[0]:.2f}, {p2[1]:.2f})"
            self.listbox.insert(tk.END, f"Points: {formatted_p1}, Points: {formatted_p2} - Distance: {dist:.4f}")  # Add to listbox
        
        self.canvas.draw()

    def clear_lines(self):
        # Remove only the lines between points
        while self.lines:
            line = self.lines.pop()
            line.remove()  # Remove the line from the plot
        self.canvas.draw()

    def reset(self):
        # Clear all points, lines, and listbox
        self.points.clear()  # Clear the points list
        self.lines.clear()  # Clear the lines list
        self.ax.cla()  # Clear the axis
        self.ax.set_xlim(0, 10)  # Reset x-axis limits
        self.ax.set_ylim(0, 10)  # Reset y-axis limits
        self.ax.set_title('Click to add points')  # Reset title
        self.listbox.delete(0, tk.END)  # Clear the listbox
        self.entry.delete(0, tk.END)  # Clear the entry box
        self.label.config(text="Enter number of closest pairs (max: 0):")  # Reset label
        self.canvas.draw()  # Redraw the canvas

if __name__ == "__main__":
    root = tk.Tk()
    app = ClosestPairsGUI(root)
    root.mainloop()