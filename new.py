import kivy
import random
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


def callback(instance):
        print('The button <%s> is being pressed' % instance.text)

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class Buttons(App):
    def Orientation(self, orient):
        self.orient = orient

    def build(self):
        layout = BoxLayout(padding=0, orientation=self.orient)
        colors = [red, green, blue, purple]
        btn1 = Button(text="macera buglem", background_color=random.choice(colors))
        layout.add_widget(btn1)
        btn1.bind(on_press=self.btn_pressed)
        btn3 = Button(text="buglem", background_color=random.choice(colors))
        layout.add_widget(btn3)
        btn3.bind(on_press=self.btn_pressed1)
        btn2 = Button(text="eglence buglem", background_color=random.choice(colors))
        layout.add_widget(btn2)
        btn2.bind(on_press=self.btn_pressed2)
        btn4 = Button(text="guzel buglem", background_color=random.choice(colors))
        layout.add_widget(btn4)
        btn4.bind(on_press=self.btn_pressed3)
        btn5 = Button(text="harika buglem", background_color=random.choice(colors))
        layout.add_widget(btn5)
        btn5.bind(on_press=self.btn_pressed4)
        self.sound = SoundLoader.load('Sesmacera.m4a')
        self.sound1 = SoundLoader.load('eğlence.m4a')
        self.sound2 = SoundLoader.load('Sesebrar.m4a')
        self.sound3 = SoundLoader.load('buglem.m4a')
        self.sound4 = SoundLoader.load('bugli.m4a')
        return layout
    def btn_pressed(self, test):
        if self.sound.state == 'play':
            self.sound.stop()
            self.sound.play()
        else:
            self.sound.play()
    def btn_pressed1(self, test):
        if self.sound1.state == 'play':
            self.sound1.stop()
            self.sound1.play()
        else:
            self.sound1.play()
    def btn_pressed2(self, test):
        if self.sound2.state == 'play':
            self.sound2.stop()
            self.sound2.play()
        else:
            self.sound2.play()
    def btn_pressed3(self, test):
        if self.sound3.state == 'play':
            self.sound3.stop()
            self.sound3.play()
        else:
            self.sound3.play()
    def btn_pressed4(self, test):
        if self.sound4.state == 'play':
            self.sound4.stop()
            self.sound4.play()
        else:
            self.sound4.play()
    
if __name__ == "__main__":
    app = Buttons()
    app.Orientation(orient="vertical")
    app.run()