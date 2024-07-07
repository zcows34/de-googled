import urllib.parse
import requests
import json
def main(args):
    html="""<!DOCTYPE html>
<html>
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    <style>
        .header {
            font-family: "Poppins", sans-serif;
            font-weight: 400;
            font-style: normal;
            color: white;
            background-color: skyblue;
            padding-top:7%;
        }
        p {
            font-family: "Poppins", sans-serif;
            font-weight: 400;
            font-style: normal;
            font-size: 100%;
            padding-left: 2%;
            padding-right: 2%;
        }
	h2 {
            font-family: "Poppins", sans-serif;
            font-weight: 600;
            font-style: normal;
            font-size: 130%;
            padding-left: 2%;
            padding-right: 2%;
        }
        a {
            color:blue;
        }
    </style>
</head>
<body>
    <div class="header">
        <center><h1>DeGoogled Google Search</h1></center>
    </div>
    <center>"""
    if not args.get('q'):
        return {"body":html+"<center><p>To get started add ?q=(query) into the url bar</p><p>Example: .../?q=hello+world</p></center></body></html>"}
    q=urllib.parse.quote(args['q'])
    url=""
    
    response=requests.get(url).text
    renc=json.loads(response)
    items=renc['items']
    n=""
    for obj in items:
        n=n+f"<h2>{obj['title']} (<a href=\"{obj['link']}\" target=\"_blank\" rel=\"noopener noreferrer\">{obj['link']}</a>)</h2><p>{obj['htmlSnippet']}</p><br/>"
    print(n)
    return {"body": html+"\n"+n+"</center></body></html>"}
