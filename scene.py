from manim import *

class Test(Scene):
    def construct(self):
        box = Square(color=RED, fill_opacity=0.5)
        self.play(DrawBorderThenFill(box))
        self.wait()
