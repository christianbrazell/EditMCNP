
import json
from utils.EditDeck import EditDeck


class MCFRTank:

    def __init__(self, config="default"):
        # # set paths for file bases
        # self.c_base = os.path("configs")
        # self.u_base = os.path("utils)

        # load config
        self.config = json.load(open(config))
        self.keys = list(self.config.keys())

    def load_config(self, config_json):
        jdata = json.load(open(config_json))

        # This will overwrite keys that already exist, and add keys that do not
        for key in self.keys:
            self.config[key] = jdata[key]

        self.keys = list(self.config.keys())

    def update_deck(self, new_deck, deck="default_deck.inp"):
        print("Starting deck update.")

        # load the editor class from EditDeck.py
        editor = EditDeck(deck)
        editor.open_new_deck(new_deck)
        editor.set_switch()
        switch_keys = list(editor.switch.keys())

        # make edits
        for key in self.keys:
            if key in switch_keys:
                editor.switch[key](self.config[key])
            else:
                print(f"ERROR: \"{key}\" is in config but not in the switch keys.")

        # close file
        editor.close_new_deck()
        print("Deck updated, file closed.")