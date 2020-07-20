#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *


class logo(Scene):
    def construct(self):
        logo  = TextMobject("Intuitio")
        logo.scale(2)

        self.play(Write(logo))
        self.wait(1)

class 