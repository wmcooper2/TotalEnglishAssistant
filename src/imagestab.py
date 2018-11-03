#!/usr/bin/env python3
"""Images tab for Total English Assistant."""

#stand lib
import os
import sys
import json
import shutil
import tkinter as tk

#3rd party
from PIL import Image
from PIL import ImageTk
from pathlib import Path
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox

#custom
from imagestabvalidation import ImageTabValidation 
import directories

class ImagesTab():
    """Creates the 'Image' tab in the GUI. Returns None."""
    check               = ImageTabValidation()
    JSONFILE            = "categories.js"
    SAVEDIR             = Path(directories.ROOTDIR, directories.IMAGEDIR)
    save_file           = Path(SAVEDIR, JSONFILE)
    load_path           = ""
    paths               = []
    img_ref             = "" 
    IMAGE_SIZE          = 500, 500
    MAX_LENGTH          = 30
    counter             = 0
    image_dictionary    = {}
    category_path       = ""
    category_header     = ""
    image               = ""

    def __init__(self, tab_control):
        """Draws the widgets of the Image tab to the GUI. Returns None."""
        self.image_library_tab = ttk.Frame(tab_control)
        tab_control.add(self.image_library_tab, text="Images")
        tab_control.grid(column=0, row=0, pady=6, padx=6)

        self.choose_directory_button = ttk.Button(self.image_library_tab, 
            text="Choose Directory", command=self.choose_directory)
        self.choose_directory_button.grid(column=0, columnspan=2, row=0, 
            padx=6, pady=6)
        
        self.category_box = ttk.LabelFrame(self.image_library_tab, 
            text="Give your collection a name")
        self.category_box.grid(column=0, columnspan=2, row=1, 
            padx=6, pady=6)
        self.category_name = ttk.Entry(self.category_box)
        self.category_name.grid(padx=6, pady=6)        

        self.image_frame = ttk.LabelFrame(self.image_library_tab)
        self.image_frame.grid(column=0, columnspan=2, row=2, padx=6, pady=6)
        self.image_name_entry = ttk.Entry(self.image_frame)
        self.image_name_entry.grid(column=0, columnspan=2, row=0, 
            padx=6, pady=6)
        image_save_button = ttk.Button(self.image_frame, text="Next", 
            command=self.next_img)
        image_save_button.grid(column=0, columnspan=2, row=1, 
            padx=6, pady=6)

        self.canvas = tk.Label(self.image_frame)
        self.choose_directory_button.focus()

    def choose_directory(self): 
        """Resets the instance attributes and the widget in the GUI.
        Returns None."""
        self.load_path = filedialog.askdirectory()
        self.reset_all_attributes()
        self.load_img_paths()
        self.draw_img()
        self.category_name.focus()        

    def reset_all_attributes(self):
        """Resets all of the class attributes. Returns None."""
        self.image_dictionary = {}
        self.counter = 0
        self.paths = []
        self.canvas.grid_forget()

    def load_img_paths(self): 
        """Loads Posixpaths of image files into 'self.paths'.
        Returns None."""
        [self.paths.append(path) for path in Path(self.load_path).glob("./[a-z]*")] 

    def draw_img(self):
        """Draws a single image to the GUI. Returns None."""
        self.image = self.paths[self.counter]
        photo = self.convert_img()
        self.canvas = tk.Label(self.image_frame, image=photo)
        self.canvas.grid(column=0, columnspan=2, row=2)

    def convert_img(self):
        """Converts 'self.image' for tkinter. Returns photo object."""
        temp = Image.open(self.image)
        temp.thumbnail(self.IMAGE_SIZE)
        photo = ImageTk.PhotoImage(temp)
        self.img_ref = photo
        return photo
        
    def next_img(self):
        """Loads the next image to the GUI. Returns None."""
        self.new_category_path()
        is_valid = self.is_valid_category() and self.is_valid_img()
        try:
            if is_valid: 
                self.add_to_dictionary()
                self.counter = self.counter + 1 
                self.canvas.grid_forget()
                self.draw_img()
                self.image_name_entry.focus()
        except IndexError:
            self.finished_naming()
        self.image_name_entry.delete(0, "end")

    def is_valid_category(self):
        """Validates category. Returns Boolean."""
        if self.check.valid_category_name(self.category_name, self.category_path):
            return True
        else:
            self.category_name.delete(0, "end")
            self.category_name.focus()
            return False

    def is_valid_img(self):
        """Validates image. Returns Boolean"""
        if self.check.valid_img_name(self.image_name_entry.get(), 
            self.MAX_LENGTH, self.image_dictionary):
            return True
        else:
            self.image_name_entry.delete(0, "end")
            self.image_name_entry.focus()
            return False

    def new_category_path(self):
        """Makes the category path. Returns String."""
        if len(self.category_name.get()) > 0:
            self.category_path = os.path.join(self.SAVEDIR, 
                self.category_name.get())
        else:
            self.check.request_category_name()    

    def set_json_var_name(self):
        """Sets the var name for '.json' object. Returns None."""
        self.category_header = "\n\n"+"var "+self.category_name.get()+" = "

    def add_to_dictionary(self):
        """Adds relative path name of image to '.json' object.
        Returns None."""
        if self.check.valid_img_name(self.image_name_entry.get(), 
            self.MAX_LENGTH, self.image_dictionary): 
            path = os.path.join(self.SAVEDIR, 
                self.category_name.get(), 
                self.image_name_entry.get() + self.image.suffix)
            self.image_dictionary[self.image_name_entry.get()] = path
        self.image_name_entry.delete(0, "end")
            
    def finished_naming(self):
        """Resets attributes when finished loading all the images from the
            user-specfied file. Returns None."""
        self.save_json_object_to_file()
        self.copy_images()
        self.category_name.delete(0, "end")
        self.choose_directory_button.focus()

    def save_json_object_to_file(self):
        """Saves the '.json' object to disk. Returns None."""
        self.set_json_var_name()
        category_file = "../"+"/".join(self.save_file.parts[1:])
        save_here = open(category_file, "a+")
        save_here.write(self.category_header)
        json.dump(self.image_dictionary, save_here, 
            sort_keys=True, indent=4)
        save_here.close()
        self.check.saved_message()

    def copy_images(self):
        """Copies images to 'TotalEnglishAssistant/Images'. Returns None."""
        copy_here = os.path.join(directories.IMAGEDIR, self.category_name.get()) 
        answer = self.check.ask_to_delete()
        if answer == True:
            for path in self.paths:
                path = os.path(path)
                shutil.move(path, copy_here)
        else:
            for path in self.paths:
                shutil.copy2(path, copy_here)

    def quit_(self):
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()

if __name__ == '__main__':
    win = tk.Tk()
    win.title("Test of Image Library Tab only")
    tab_control = ttk.Notebook(win)
    menuBar = Menu(win)
    win.config(menu=menuBar)
    images_tab = ImagesTab(tab_control)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="Exit", command=images_tab.quit_)
    menuBar.add_cascade(label="File", menu=fileMenu)
    win.mainloop()
