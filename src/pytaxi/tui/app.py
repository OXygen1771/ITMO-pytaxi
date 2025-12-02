from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static


class DBApp(App):
	"""
	TUI app for a taxi service.
	"""

	TITLE = "pytaxi"

	BINDINGS = [
		("q", "quit", "Выход"),
	]

	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)

	def compose(self) -> ComposeResult:
		"""
		Compose the application window

		:return: Window with all the app's widgets
		:rtype: ComposeResult
		"""

		yield Header()

		yield Static("Hello, World!")

		yield Footer()

	def on_mount(self) -> None:
		"""
		Performs actions when the app window is mounted.

		Currently, sets the app theme to Catppuccin Mocha.

		:return: None
		:rtype: None
		"""

		self.theme = "catppuccin-mocha"
