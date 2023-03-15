from flask import Flask,request
from flask import Response

import os
import socket
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    html = """
Server hostname <b>{hostname}</b> {serveraddr}<br/>
Using IP <b>{remoteip}</b><br/>
URL is {url}
"""
    return html.format(hostname=socket.gethostname(),remoteip=request.remote_addr, serveraddr=request.server, url=request.url)

@app.route("/headers")
def headers():
  return Response(str(request.headers),mimetype='text/plain')
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
	
	
	
	
	
