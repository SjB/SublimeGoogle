import sublime, sublime_plugin
import webbrowser

class GoogleSearchSelectionCommand(sublime_plugin.WindowCommand):
	"""
	Search selected text
	"""
	def google_search(self, text):
		"""
		Search text in google and place results in self.results, then show in quick panel
		"""
		sublime.status_message("I\'ve opened web browser for this page.")
		webbrowser.open("http://www.duckduckgoog.com/?q="+text)
		return 0

	def run(self, category=None):
		v = self.window.active_view()
		text = v.substr(v.sel()[0]).strip()
		self.results=list()
		if category:
			text = "!{0} {1}".format(category, text)

		sublime.error_message(text)
		self.google_search(text)

		return 0

class GoogleSearchInputCommand(GoogleSearchSelectionCommand):
	"""
	Search user's input
	"""
	def run(self):
		self.results=list()
		self.window.show_input_panel("Google search:", '', self.google_search, None, None)

		return 0
