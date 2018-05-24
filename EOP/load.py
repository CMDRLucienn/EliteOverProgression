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

def plugin_app(parent):
	this.parent = parent
	button = tk.Button(parent, text="EOProgression", command=plugin_window)

def plugin_window(parent):
	this.window = tk.TopLevel()
	this.window.title("EOProgression")
	this.window.resizable(width=False, height=False)
	
	tab = nb.Notebook(this.window)
	
	combat_page = nb.Frame(tab) # Combat tab
	
	trader_page = nb.Frame(tab) # Trade tab
	
	explor_page = nb.Frame(tab) # Explorer tab
	
	tab.add(combat_page, text='Combat')
	tab.add(trader_page, text='Trade')
	tab.add(explor_page, text='Exploration')
	
	tab.pack(expand=1, fill="both")
	
	this.window.mainloop()
	
def plugin_stop():
	print "EOProgression Closing"
	
def plugin_prefs(parent):
	frame = nb.Frame(parent)
	frame.columnconfigure(1, weight=1)
	
	plugin_label = nb.Label(frame, text="EOProgression Configuration")
	plugin_label.grid(padx=10, row=8, sticky=tk.W)
	
	return frame

def prefs_changed():