import sys
import ttk
import Tkinter as tk
import requests

from config import applongname, appversion
import myNotebook as nb
from config import config

this = sys.modules[__name__]

def plugin_start():
	print "Loading EOProgression..."
	return "Test"

def plugin_prefs(parent):
	frame = nb.Frame(parent)
	frame.columnconfigure(1, weight=1)
	
	plugin_label = nb.Label(frame, text="EOProgression Configuration")
	plugin_label.grid(padx=10, row=8, sticky=tk.W)
	
	return frame

def prefs_changed():
	
def plugin_stop():
	print "EOProgression Closing"