import os
from flask import Flask, render_template

class secondexample:
	
	NAME = "Second Plugin" #plugin name
	version = "0.1" # plugin version
	plugins_folder = "plugins/"
	
	
	# The html page of work, you can use the pages of the project like: 'index.html' or 'outit_saved'(defualt setting).
	# You can also create the html page (using the default html page for the template) and write its name here
	
	htmlpage = "mypage.html" 
	
	# Html code for the page 'index.html' or 'outfit_saved.html' if it is selected in htmlpage variable.
	
	topcode = "" # refert to pluginname/top.html
	buttomcode = "" # refert to pluginname/buttom.html
	
	def __init__(self, main):
	
		if main:
			self.plugins_folder = ""
	
		if self.htmlpage == "outfit_saved.html" or self.htmlpage == "index.html":
			
			# Load the html codes
			self.load_html()
	
	def load_html(self):
		
		with open(self.plugins_folder+self.NAME+"/topcode.html", "r") as f:
			self.topcode = f.read()
		
		with open(self.plugins_folder+self.NAME+"/buttomcode.html", "r") as f:
			self.buttomcode = f.read()
	
	# Write here the code that is called when the page is loaded (only for index.html and outfit_saved.html)
	def setHtml(self):
		
		if self.htmlpage == "outfit_saved.html" or self.htmlpage == "index.html":
			
			self.load_html()
		
		self.topcode = self.topcode.replace("{{ name }}", self.NAME)
		self.buttomcode = self.buttomcode.replace("{{ name }}", self.NAME)
	
	def get_html_page(self):
		
		return render_template(self.NAME+"/"+self.htmlpage, name=self.NAME)
	
	# write here your parallel process code
	def start(self):
		
		pass

app = Flask(__name__)

@app.route("/")
def index():
	
	return plugin.get_html_page()

if __name__ == "__main__":

	plugin = secondexample(True)
	plugin.start()
	from jinja2 import FileSystemLoader
	app.jinja_loader = FileSystemLoader([""])

	ip = "127.0.0.1"
	app.run(host=ip)
