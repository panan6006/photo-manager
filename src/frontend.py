import tkinter as tk
from PIL import Image, ImageTk
import os

class Frontend:

    def __init__(self, files, fm):
        self.first_image_index = 0
        self.control_panel_size = 5

        self.image_width = 200
        self.image_height = 200

        self.output_image_width = 75
        self.output_image_height = 75

        self.files = files
        self.fm = fm

        self.window = tk.Tk()
        self.window.state('zoomed')
        self.window.configure(background='#555555')
        self.window.title('Photo Manager')
        self.window.bind("<Key>", self.read_input)

        self.control_frame = tk.Frame(name="control_frame")
        self.control_frame.pack()

        self.output_frame = tk.Frame()
        self.output_frame.pack()

        self.output_images = []
        self.active_image = ''

    def create_image_control(self):
        self.images = []

        for i in range(self.control_panel_size):
            if self.first_image_index + i < len(self.files):

                image_path = self.files[self.first_image_index + i]

                image_width = self.image_width
                image_height = self.image_height

                if len(self.images) == int(self.control_panel_size / 2):
                    image_width *= 2
                    image_height *= 2
                    self.active_image = image_path

                img = ImageTk.PhotoImage(Image.open(image_path).resize((image_width, image_height), Image.Resampling.LANCZOS))
                self.images.append(img)

                image_frame = tk.Frame(self.control_frame, name=f"control_frame_{i}")

                canvas = tk.Canvas(image_frame, width=image_width, height=image_height, bg='black', name=f"control_canvas_{i}")
                canvas.pack()

                canvas.create_image(0, 0, anchor='nw', image=img)

                label = tk.Label(image_frame, text=image_path)
                label.pack()

                image_frame.pack(side=tk.LEFT)

    def run(self):
        self.window.mainloop()

    def read_input(self, event):
        key = event.keysym
        print(f"Key pressed: {key}")
        print(self.first_image_index)
        print(self.active_image)

        if key == 'Left':
            self.first_image_index -= 1
            self.create_image_control()
        if key == 'Right':
            self.first_image_index += 1
            self.create_image_control()
        if key == '0' or key == '1' or key == '2' or key == '3' or key == '4' or key == '5' or key == '6' or key == '7' or key == '8' or key == '9':
            self.files = self.fm.move_image(self.active_image, int(key))
            self.create_output_panels(self.fm.output_root)
            self.create_image_control()
        if key == 'Delete':
            self.files = self.fm.remove_image(self.active_image)
            self.create_image_control()

    def create_output_panels(self, folder_path):
        for index, x in enumerate(next(os.walk(folder_path))[1]):
            self.create_output_panel(index, folder_path, x)


    def create_output_panel(self, index, folder_path, folder_name):
        counter = 0

        files = self.fm.read_images(f"{folder_path}/{folder_name}/")

        self.output_imgs = []

        self.main_folder_frame = tk.Frame(self.output_frame, padx=20, name=f'output_{index}')
        self.main_folder_frame.pack(side=tk.LEFT)

        folder_label = tk.Label(self.main_folder_frame, text=f"{index}: {folder_name} ({len(files)})")
        folder_label.pack()

        main_output_width = self.output_image_width * 2
        main_output_height = self.output_image_height * 2

        self.last_image_canvas = tk.Canvas(self.main_folder_frame, width=main_output_width, height=main_output_height, bg="black", name=f"output_canvas_{index}_{counter}")
        self.last_image_canvas.pack()

        if 0 <= counter < len(files):

            img = ImageTk.PhotoImage(Image.open(files[counter]).resize((main_output_width, main_output_height), Image.Resampling.LANCZOS))
            self.output_imgs.append(img)
            self.last_image_canvas.create_image(0, 0, anchor='nw', image=img)
            l2 = tk.Label(self.main_folder_frame, text=files[counter])
        else:
            l2 = tk.Label(self.main_folder_frame, text="---")

        l2.pack()

        for i in range(2):
            container = tk.Frame(self.main_folder_frame)
            container.pack()

            for j in range(2):
                counter += 1

                self.canvas = tk.Canvas(container, width=self.output_image_width, height=self.output_image_height, bg="black", name=f"output_canvas_{index}_{counter}")
                self.canvas.pack(side=tk.LEFT)

                if 0 <= counter < len(files):
                    img = ImageTk.PhotoImage(Image.open(files[counter]).resize((self.output_image_width, self.output_image_height), Image.Resampling.LANCZOS))
                    self.output_images.append(img)

                    self.canvas.create_image(0, 0, anchor='nw', image=img)

        self.output_images.append(self.output_imgs)