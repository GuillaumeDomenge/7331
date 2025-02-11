from manim import *


class CreatingMobjects(Scene):
	def construct(self):
		circle = Circle()
		self.add(circle)
		self.play(square.animate.shift(UP), run_time = 10)