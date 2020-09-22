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
        btn1 = Button(text="macera bulem", background_color=random.choice(colors))
        layout.add_widget(btn1)
        btn1.bind(on_press=self.btn_pressed)
        btn3 = Button(text="bulem", background_color=random.choice(colors))
        layout.add_widget(btn3)
        btn3.bind(on_press=self.btn_pressed)
        btn2 = Button(text="elence bulem", background_color=random.choice(colors))
        layout.add_widget(btn2)
        btn2.bind(on_press=self.btn_pressed)
        btn4 = Button(text="guzel bulem", background_color=random.choice(colors))
        layout.add_widget(btn4)
        btn4.bind(on_press=self.btn_pressed)
        self.sound = SoundLoader.load('yo.wav')
        return layout

    def btn_pressed(self, test):
        print(self.sound.state)
        if self.sound.state == 'play':
            self.sound.stop()
            self.sound.play()
        else:
            self.sound.play()



if __name__ == "__main__":
    app = Buttons()
    app.Orientation(orient="vertical")
    app.run()