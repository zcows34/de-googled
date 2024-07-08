import requests
import json
import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def site():
	url="https://faas-syd1-c274eac6.doserverless.co/api/v1/web/fn-b2d904ad-e0b4-4658-a393-149bf99d228b/default/searchup"
	if not request.args.get("q"):
		return open("default.html").read()+"<center><p>To get started add ?q=(query) into the url bar</p><p>Example: .../?q=hello+world</p></center></body></html>"
	query={
		"query":request.args.get("q")
	}
	response=requests.post(url,data=query).text
	renc=json.loads(response)
	if not renc['items']:
		return open("default.html").read()+"<center><p>No results found</p></center></body></html>"
	items=renc['items']
	n=""
	for obj in items:
		n=n+f"<h2>{obj['title']} (<a href=\"{obj['link']}\" target=\"_blank\" rel=\"noopener noreferrer\">{obj['link']}</a>)</h2><p>{obj['htmlSnippet']}</p><br/>"
	print(f'{request.remote_addr}, {request.args.get("q")}')
	return open("default.html").read()+"\n"+n+"</center></body></html>"
