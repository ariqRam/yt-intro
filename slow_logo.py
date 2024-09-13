from manim import *

class SlowDrawingScene(Scene):
	def construct(self):
		self.camera.background_color = "#2C2C2C"

		chars = ["A", "R", "I", "Q"]
		letters = [
				SVGMobject(f"media/{char}.svg", stroke_color=WHITE, stroke_width=2)
				for char in chars
		]

		logo = VGroup(*letters).arrange(RIGHT, buff=0.3)
		logo.scale(0.8)

		logo.move_to(ORIGIN)

		animations = [Create(letter, run_time=1.2) for letter in letters]
		self.play(LaggedStart(*animations, lag_ratio=0.6))

		self.play(*[
			letter.animate.set_stroke("#2C2C2C", width=2).set_fill(WHITE, opacity=1)
			for letter in letters
		])

		self.play(
			logo.animate.scale(100), run_time=1.5, rate_func=rate_functions.ease_in_quart,
		)
