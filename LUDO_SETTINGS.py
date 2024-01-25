from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk
from pygame import mixer

class Settings:
    def __init__(self, master):
        self.master = master
        master.title("Settings")
        master.geometry('350x300')

        # Initialize mixer and load music
        mixer.init()
        mixer.music.load("assets/bensound-summer_mp3_music.mp3")

        # Create buttons
        self.play = Button(master, text='Play Music', width=14, bg='red', fg='black', command=self.play_music)
        self.play.place(x=50, y=20)

        self.stop = Button(master, text='Stop Music', width=14, bg='green', fg='black', command=self.stop_music)
        self.stop.place(x=50, y=80)

        self.show_dice_button = Button(master, text='Show Dice', width=14, bg='blue', fg='black', command=self.show_dice)
        self.show_dice_button.place(x=50, y=140)

        self.select_dice_button = Button(master, text='Select Dice', width=14, bg='orange', fg='black', command=self.select_dice)
        self.select_dice_button.place(x=50, y=200)

        self.ok = Button(master, text='Close', width=14, bg='purple', fg='black', command=master.destroy)
        self.ok.place(x=50, y=250)

        self.image_label = Label(master)
        self.image_label.place(x=210, y=100)

        # List of dice image paths
        self.dice_image_paths = [
            r"C:\Users\DELL\Documents\P2 COMP 111\ludo\assets\de1.png",
            r"C:\Users\DELL\Documents\P2 COMP 111\ludo\assets\purple_dice1.jpeg",
            r"C:\Users\DELL\Documents\P2 COMP 111\ludo\assets\blue_dice1.jpeg",
            r"C:\Users\DELL\Documents\P2 COMP 111\ludo\assets\red_dice1.jpeg",
            r"C:\Users\DELL\Documents\P2 COMP 111\ludo\assets\white_dice1.jpeg",
            r"C:\Users\DELL\Documents\P2 COMP 111\ludo\assets\yellow_dice1.jpeg"
        ]

        # Initialize the current index
        self.current_dice_index = 0

        # Save path for the selected dice image
        self.dice_button_paths = {
            self.select_dice_button: r"C:\Users\DELL\Documents\P2 COMP 111\ludo\assets\selected_dice.jpeg",
        }

        # Label to show the saved dice image
        self.show_saved_image = Label(master)
        self.show_saved_image.place(x=210, y=200)

        # Initialize the current index
        self.current_dice_index = 0

    def play_music(self):
        if self.play["text"] == "Play Music":
            self.play["bg"] = "red"
            mixer.music.play()
        else:
            return

    def stop_music(self):
        if self.stop["text"] == "Stop Music":
            self.stop["bg"] = "green"
            mixer.music.pause()
        else:
            return

    def show_dice(self):
        # Get the next dice image path
        image_path = self.dice_image_paths[self.current_dice_index]

        # Load and display the next dice image
        im = Image.open(image_path)
        photo = ImageTk.PhotoImage(im)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Update the current index
        self.current_dice_index = (self.current_dice_index + 1) % len(self.dice_image_paths)

        # Update the associated path for the select_dice_button
        self.dice_button_paths[self.select_dice_button] = image_path

    def select_dice(self):
        # Get the associated file path for the button
        file_path = self.dice_button_paths.get(self.select_dice_button)

        if file_path:
            # Load and display the selected dice image
            im = Image.open(file_path)
            photo = ImageTk.PhotoImage(im)
            self.image_label.config(image=photo)
            self.image_label.image = photo

            # Update the show_saved_image Label
            saved_image = ImageTk.PhotoImage(Image.open(file_path))
            self.show_saved_image.config(image=saved_image)
            self.show_saved_image.image = saved_image

    def main(self):
        self.play_music()
        self.stop_music()
        self.show_dice()
        self.select_dice()

if __name__ == '__main__':
    root = Tk()
    settings = Settings(root)
    root.mainloop()
