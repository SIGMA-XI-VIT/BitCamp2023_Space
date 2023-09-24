import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SpaceDebrisSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Space Debris Simulator")
        
        # Create labels, entry fields, and buttons
        self.label_position = tk.Label(master, text="Initial Position (x, y, z):")
        self.entry_position = tk.Entry(master)
        self.label_velocity = tk.Label(master, text="Initial Velocity (dx/dt, dy/dt, dz/dt):")
        self.entry_velocity = tk.Entry(master)
        self.button_simulate = tk.Button(master, text="Simulate", command=self.simulate_motion)
        
        # Place widgets on the grid
        self.label_position.grid(row=0, column=0, sticky="w")
        self.entry_position.grid(row=0, column=1)
        self.label_velocity.grid(row=1, column=0, sticky="w")
        self.entry_velocity.grid(row=1, column=1)
        self.button_simulate.grid(row=2, column=0, columnspan=2)
        
        # Create separate FigureCanvasTkAgg for each coordinate with smaller figsize
        figsize = (4, 2)  # Adjust the size as needed
        self.figure_x, self.ax_x = plt.subplots(figsize=figsize)
        self.canvas_x = FigureCanvasTkAgg(self.figure_x, master=master)
        self.canvas_x.get_tk_widget().grid(row=3, column=0)
        
        self.figure_y, self.ax_y = plt.subplots(figsize=figsize)
        self.canvas_y = FigureCanvasTkAgg(self.figure_y, master=master)
        self.canvas_y.get_tk_widget().grid(row=3, column=1)
        
        self.figure_z, self.ax_z = plt.subplots(figsize=figsize)
        self.canvas_z = FigureCanvasTkAgg(self.figure_z, master=master)
        self.canvas_z.get_tk_widget().grid(row=3, column=2)
        
    def simulate_motion(self):
        try:
            initial_position = tuple(map(float, self.entry_position.get().split(',')))
            initial_velocity = tuple(map(float, self.entry_velocity.get().split(',')))
            debris = SpaceDebris(1, initial_position, initial_velocity)
            delta_t = 1  # Time step (in seconds)
            positions = []  # List to store positions for plotting
            for _ in range(10):
                debris.update_position(delta_t)
                positions.append(debris.position)
            self.plot_positions(positions)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}") 
    
    def plot_positions(self, positions):
        x, y, z = zip(*positions)
        a, b, c = (200,)*10,(200,)*10,(200,)*10
        
        # Plot x position
        self.ax_x.clear()
        self.ax_x.plot(x, label='x')
        self.ax_x.plot(a, label='a')
        self.ax_x.legend()
        self.canvas_x.draw()
        
        # Plot y position
        self.ax_y.clear()
        self.ax_y.plot(y, label='y')
        self.ax_y.plot(b, label='b')
        self.ax_y.legend()
        self.canvas_y.draw()
        
        # Plot z position
        self.ax_z.clear()
        self.ax_z.plot(z, label='z')
        self.ax_z.plot(c, label='c')
        self.ax_z.legend()
        self.canvas_z.draw()

class SpaceDebris:
    def __init__(self, id, position, velocity):
        self.id = id
        self.position = position
        self.velocity = velocity
        
    def update_position(self, delta_t):
        self.position = tuple(p + v * delta_t for p, v in zip(self.position, self.velocity))

root=tk.Tk()
app=SpaceDebrisSimulator(root)
root.mainloop()
