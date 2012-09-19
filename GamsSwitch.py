# GAMS - Sublime Text 2 Plugin
# Created by Laurent Drouet
# https://github.com/lolow/sublime-gams

import os
import sublime, sublime_plugin


class GamsSwitchCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		# source file's path
		source      = self.view.file_name()
		source_path = os.path.dirname(source)
		
		# file path and extension
		fileName, fileExtension = os.path.splitext(source)

		# Find target file
		target_file  = None

		if fileExtension==".gms":
			target_file  = os.path.join(source_path,fileName+".lst")
		if fileExtension==".lst":
			target_file  = os.path.join(source_path,fileName+".gms")

		if target_file and os.path.exists(target_file):
			self.view.window().open_file(target_file)