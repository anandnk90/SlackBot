import logging
import runpy

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	file_globals = runpy.run_path("factreader.py")
	return 'Hello World!'

if __name__=='__main__':
	app.rum(host='127.0.0.1', port=8080, debug='True')
