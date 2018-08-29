#!/usr/bin/python3
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ImageTabValidation():
    data_validation_title = "Data Validation"
    valid_input_instructions = "Please follow these rules when making your selections."
    name_length = "Please enter a name with a length greater than 0 and less than {0}."
    case_insensitive = "Names must be case-insensitive (ex; 'Apple' = 'apple')."
    duplicate_name_msg = "That name is already in this image category. Please choose another name."
    duplicate_category_msg = "A category with that name already exists. Choose another name."
    input_category_name_msg = "Enter a category name."
    generator_exit_msg = "All images have been added."
    info_box_title = "Image Library"
    saved_msg = "The categories list has been added to, and the images loaded were saved in their own directory."

    invalid_input_msg = [
                         valid_input_instructions,
                         name_length,
                         case_insensitive,]
    input_instructions = "\n\n".join(invalid_input_msg)

    copy_images_title = "Copy Images"
    copy_images_msg = str("".join(["Do you want to delete the images from the",
                        "\n",
                        "place you loaded them from?"]))

    def valid_img_name(self, name, length, img_dict):
        """Validates the image name, returns Boolean."""
        if self.valid_img_name_type(name) \
            and self.valid_img_name_length(name, length) \
            and not self.duplicate_img_name(name, img_dict):
            return True
        else:
            self.duplicate_name()
            return False

    def valid_img_name_type(self, name):
        """Validates image name type, returns None."""
        if type(name) == str:
            return True
        else:
            return False

    def valid_img_name_length(self, name, length):
        """Validates image name length, returns None."""
        if len(name) < length and len(name) > 0:
            return True
        else:
            return False

    def duplicate_img_name(self, name, dictionary):
        """Checks for duplicate image name, returns None."""
        if name in dictionary.keys():
            return True 
        else:
            return False

    def valid_category_name(self, name, category_dir):
        """Validates the category name, returns Boolean."""
        if os.path.exists(category_dir):
            self.duplicate_category()
            return False
        else:
            return True

    def duplicate_name(self):
        """Shows duplicate name message, returns None."""
        messagebox.showinfo(title = self.info_box_title, message = self.duplicate_name_msg)

    def duplicate_category(self):
        """Checks for duplicate category, returns Boolean."""
        messagebox.showinfo(title = self.info_box_title, message = self.duplicate_category_msg)

    def ask_to_delete(self):
        """Shows a message box asking user to delete images, returns Boolean."""
        messagebox.askyesno(title = self.copy_images_title, message = self.copy_images_msg)

    def saved_message(self):
        """Shows a message box that the images are saved, returns None."""
        messagebox.showinfo(title = self.info_box_title, message = self.saved_msg)

    def show_input_instructions(self):
        """Shows input instructions in an info box, returns None."""
        messagebox.showinfo(title = self.info_box_title, message = self.name_length)

    def show_finish_message(self):
        """Shows a message that the images are done loading, returns None."""
        messagebox.showinfo(title = self.info_box_title, message = self.generator_exit_msg)

    def request_category_name(self):
        """Asks the user to input a category name, returns None."""
        messagebox.showinfo(title = self.info_box_title, message = self.input_category_name_msg)
       
