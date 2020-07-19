#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *

class Intro(Scene):
    def construct(self):
        NameSlide = TextMobject("Intuition around Convolution",tex_to_color_map={"Convolution": YELLOW})
        NameSlide.scale(2)

        self.play(Write(NameSlide))
        self.wait(2)