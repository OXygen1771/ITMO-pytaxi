from ..tui.app import DBApp


def tui() -> None:
	"""
	Launch the TUI app
	"""

	app = DBApp()
	app.run()

__all__ = ['tui']
