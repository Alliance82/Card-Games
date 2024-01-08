# Created By Alliance82
# Created On 1/7/2024
# This file builds and displays a full deck of 52 cards in the tkinter GUI
import tkinter as tk
from PIL import Image, ImageTk

# File path to the card images
file_path = ''
# Four card suits and the associated values
card_suits = ["spades", "hearts", "diamonds", "clubs"]
card_values = {
    "ace": 1, 
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5,
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10,
    "jack": 10, 
    "queen": 10, 
    "king": 10,
}

def display_all_cards():
    def resize_images(event):
        nonlocal image_width, image_height

        # Dynamically recalculates the card sizes to take up the whole GUI
        image_width = event.width // cards_per_row
        image_height = event.height // cards_per_column

        update_images()

    def update_images():
        canvas.delete("all")

        # Display all 52 cards in a grid
        for i, suit in enumerate(card_suits):
            for j, (card, value) in enumerate(card_values.items()):
                card_file_path = f'{file_path}{card}_of_{suit}.png'
                image = Image.open(card_file_path)
                resized_image = image.resize((image_width, image_height))
                tk_image = ImageTk.PhotoImage(resized_image)
                canvas.create_image(j * image_width, i * image_height, anchor=tk.NW, image=tk_image)

                # Store each image and card 
                photo_references.append(tk_image)

    # Create the Tkinter root window
    root = tk.Tk()
    root.title("All Cards Display")

    # Create a canvas to display the cards in a grid
    canvas = tk.Canvas(root)
    
    # Will cause the window to open in full screen every time
    root.wm_state('zoomed')
    canvas.pack(fill=tk.BOTH, expand=True)

    # Find the initial screen width and height, used to calculate the card height, width
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the initial image width and height
    # Set the number of cards per row and column
    cards_per_row = 13
    cards_per_column = 4
    image_width = screen_width // cards_per_row
    image_height = screen_height // cards_per_column
    photo_references = []

    # Bind resize_images and update the images
    root.bind("<Configure>", resize_images)
    update_images()

    root.mainloop()

display_all_cards()
