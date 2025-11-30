from kivy.lang import Builder
from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

KV = '''
<CircularButton>:
    canvas.before:
        Color:
            rgba: root.btn_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.size[0] / 2,]

<MainScreen>:
    md_bg_color: 0.1, 0.1, 0.1, 1

    MDFloatLayout:
        CircularButton:
            id: circle
            size_hint: None, None
            size: "150dp", "150dp"
            pos_hint: {"center_x": .5, "center_y": .5}
            btn_color: 0.2, 0.6, 1, 0.8
        
        MDLabel:
            id: status_label
            text: "Нажми"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "H4"
            pos_hint: {"center_x": .5, "center_y": .5}

    MDFillRoundFlatButton:
        text: "СТАРТ / СТОП"
        pos_hint: {"center_x": .5, "y": .1}
        font_size: "18sp"
        md_bg_color: 0.2, 0.2, 0.2, 1
        text_color: 1, 1, 1, 1
        on_release: root.toggle_animation()
'''

class CircularButton(CommonElevationBehavior, MDFloatLayout):
    from kivy.properties import ColorProperty
    btn_color = ColorProperty([0.2, 0.6, 1, 0.8])

class MainScreen(MDScreen):
    is_animating = False

    def toggle_animation(self):
        circle = self.ids.circle
        label = self.ids.status_label
        
        if self.is_animating:
            Animation.cancel_all(circle)
            anim = Animation(size=("150dp", "150dp"), btn_color=[0.2, 0.6, 1, 0.8], d=0.5, t='out_elastic')
            anim.start(circle)
            label.text = "Нажми"
            self.is_animating = False
        else:
            self.is_animating = True
            self.animate_inhale(circle, label)

    def animate_inhale(self, widget, label):
        if not self.is_animating: return
        label.text = "Вдох"
        anim = Animation(size=("300dp", "300dp"), btn_color=[0.4, 0.8, 0.5, 1], d=4, t='in_out_sine')
        anim.bind(on_complete=lambda *args: self.animate_exhale(widget, label))
        anim.start(widget)

    def animate_exhale(self, widget, label):
        if not self.is_animating: return
        label.text = "Выдох"
        anim = Animation(size=("150dp", "150dp"), btn_color=[0.2, 0.6, 1, 0.8], d=4, t='in_out_sine')
        anim.bind(on_complete=lambda *args: self.animate_inhale(widget, label))
        anim.start(widget)

class ZenApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

if __name__ == '__main__':
    ZenApp().run()
