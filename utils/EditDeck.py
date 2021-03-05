import numpy as np


class EditDeck:
    """
    This class is a switch will allow for editing the input deck.
    """

    def __init__(self, ref_deck="default_deck.inp"):
        ###
        self.deck = open(ref_deck, "r")#.readlines()
        self.new_deck = None
        self.open_deck = None
        self.open_lines = None

    def open_new_deck(self, new_deck):
        # self.open_deck = open(new_deck, 'r')
        self.open_lines = self.deck.readlines()
        self.new_deck = open(new_deck, "w")
        self.new_deck.writelines(self.deck)

    def close_new_deck(self):
        self.new_deck.writelines(self.open_lines)
        self.new_deck.close()
        self.deck.close()

    # define switch methods
    def core_density(self, new_val):
        print("EDIT: core_density")

        # iterate through lines until the edit is made
        lines = self.open_lines
        in_progress = True
        i = 0
        while in_progress:
            line = lines[i]
            splits = line.split()
            if "$core_density" in splits:
                splits[2] = str(new_val)
                self.open_lines[i] = " ".join(splits)
                in_progress = False
            elif i > len(lines):
                print("ERROR: flag was not found. Moving to next edit.")
                in_progress = False
            i += 1
        # Record update to script
        # self.new_deck.writelines(lines)
        # self.open_deck = open()
        # TODO: check that this works

    def containment_density(self, new_val):
        print("EDIT: containment_density")

        # iterate through lines until the edit is made
        lines = self.open_lines
        in_progress = True
        i = 0
        while in_progress:
            line = lines[i]
            splits = line.split()
            if "$containment_density" in splits:
                splits[2] = str(new_val)
                self.open_lines[i] = " ".join(splits)
                in_progress = False
            elif i > len(lines):
                print("ERROR: flag was not found. Moving to next edit.")
                in_progress = False
            i += 1
        # Record update to script
        # self.new_deck.writelines(lines)

    def core_radius(self, new_val):
        print("EDIT: core_radius")

        # iterate through lines until the edit is made
        lines = self.open_lines
        in_progress = True;
        i = 0
        while in_progress:
            line = lines[i]
            splits = line.split()
            if "$core_radius" in splits:
                splits[2] = str(new_val)
                self.open_lines[i] = " ".join(splits)
                in_progress = False
            elif i > len(lines):
                print("ERROR: flag was not found. Moving to next edit.")
                in_progress = False
            i += 1
        # Record update to script
        # self.new_deck.writelines(lines)

    def core_bottom(self, new_val):
        print("EDIT: core_bottom")

        # iterate through lines until the edit is made
        lines = self.open_lines
        in_progress = True;
        i = 0
        while in_progress:
            line = lines[i]
            splits = line.split()
            if "$core_bottom" in splits:
                splits[2] = str(new_val)
                self.open_lines[i] = " ".join(splits)
                in_progress = False
            elif i > len(lines):
                print("ERROR: flag was not found. Moving to next edit.")
                in_progress = False
            i += 1
        # Record update to script
        # self.new_deck.writelines(lines)

    def core_top(self, new_val):
        print("EDIT: core_top")

        # iterate through lines until the edit is made
        lines = self.open_lines
        in_progress = True;
        i = 0
        while in_progress:
            line = lines[i]
            splits = line.split()
            if "$core_top" in splits:
                splits[2] = str(new_val)
                self.open_lines[i] = " ".join(splits)
                in_progress = False
            elif i > len(lines):
                print("ERROR: flag was not found. Moving to next edit.")
                in_progress = False
            i += 1
        # Record update to script
        # self.new_deck.writelines(lines)

    def containment_radius(self, new_val):
        print("EDIT: containment_radius")

        # iterate through lines until the edit is made
        lines = self.open_lines
        in_progress = True;
        i = 0
        while in_progress:
            line = lines[i]
            splits = line.split()
            if "$containment_radius" in splits:
                splits[2] = str(new_val)
                self.open_lines[i] = " ".join(splits)
                in_progress = False
            elif i > len(lines):
                print("ERROR: flag was not found. Moving to next edit.")
                in_progress = False
            i += 1
        # Record update to script
        # self.new_deck.writelines(lines)

    def containment_bottom(self, new_val):
        print("EDIT: containment_bottom")

        # iterate through lines until the edit is made
        lines = self.open_lines
        in_progress = True;
        i = 0
        while in_progress:
            line = lines[i]
            splits = line.split()
            if "$containment_bottom" in splits:
                splits[2] = str(new_val)
                self.open_lines[i] = " ".join(splits)
                in_progress = False
            elif i > len(lines):
                print("ERROR: flag was not found. Moving to next edit.")
                in_progress = False
            i += 1
        # Record update to script
        # self.new_deck.writelines(lines)

    def containment_top(self, new_val):
        print("EDIT: containment_top")

        # iterate through lines until the edit is made
        lines = self.open_lines
        in_progress = True;
        i = 0
        while in_progress:
            line = lines[i]
            splits = line.split()
            if "$containment_top" in splits:
                splits[2] = str(new_val)
                self.open_lines[i] = " ".join(splits)
                in_progress = False
            elif i > len(lines):
                print("ERROR: flag was not found. Moving to next edit.")
                in_progress = False
            i += 1
        # Record update to script
        # self.new_deck.writelines(lines)

    # def M1(self, new_val):
    #     print("EDIT: M1")
    #
    #     # iterate though lines until the edit is made
    #     lines = self.new_deck.readlines()
    #     in_progress = True
    #     i = 0
    #     while in_progress:
    #         line = lines[i]
    #         splits = line.split()
    #         if "$M1_start" in splits

    # TODO: def more functions

    def set_switch(self):
        self.switch = {
            "core_density": self.core_density,
            "containment_density": self.containment_density,
            "core_radius": self.core_radius,
            "core_bottom": self.core_bottom,
            "core_top": self.core_top,
            "containment_radius": self.containment_radius,
            "containment_bottom": self.containment_bottom,
            "containment_top": self.containment_top
        }
