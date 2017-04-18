import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.behaviors.emacs import EmacsBehavior
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from pymongo import MongoClient
import os
class homeAction(StackLayout):
    
    def loginFunction(self, username, password):
        if username and password:
            try:
                client = MongoClient()
                db = client['remindersNote']
                cursor = db.users.find({"username" : username}).count()
                if cursor > 0:
                    popup = Popup(title='Message', content=Label(text=username + " " + password), size_hint=(None, None), size=(200, 80))
                else:
                    popup = Popup(title='Message', content=Label(text="Incorrect Input"), size_hint=(None, None), size=(200, 80))
                popup.open()
            except Exception:
                self.display.text = "Error Input"
        else:
                self.display.text = "Required Field"

    def registerApp(self):
        os.system("python register.py")

    def forgotApp(self):
        os.system("python forgotpass.py")

class homeLog(App):

    def build(self):
        return homeAction()

homelog = homeLog()

homelog.run()