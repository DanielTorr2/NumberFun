import tkinter as tk
import random

# Goal of project will create GUI (Graphical User Interface) to visualize
# random distribution of rain droplets.

# Create the main application window
root = tk.Tk()
root.title("Rain Visualizer")
root.geometry("900x700")  # Set window size (width x height)

# Create a Canvas
canvas = tk.Canvas(root, width=900, height=700, bg="black")
canvas.pack()

# Function to randomly create coordinates
def getCoords():
    # Generate Random X1 and Y1
    x_one = random.randint(1, 900)
    y_one = random.randint(1, 700)

    # Set X2, Y2 to create a short vertical line (raindrop)
    x_two = x_one
    y_two = y_one + random.randint(5, 15)  # Randomize raindrop length

    return [x_one, y_one, x_two, y_two]

# Function to draw a single raindrop
def drawDroplet():
    coordinates = getCoords()
    canvas.create_line(
        coordinates[0], coordinates[1], coordinates[2], coordinates[3], fill="white"
    )

# Function to gradually draw multiple raindrops
def drawRaindrops():
    drawDroplet()  # Draw a single raindrop
    root.after(2, drawRaindrops)  # Call this function again after 10 milliseconds

# Start drawing raindrops
drawRaindrops()

# Run the application
root.mainloop()
