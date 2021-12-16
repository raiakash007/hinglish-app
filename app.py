from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route('/')
def home():
   url = "http://127.0.0.1:5001/name"
   headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'Accept': 'text/plain',
   }
   payload = {"data":"dfsfsfsf","id":100}
   response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
   #return response.text
   # Code here will react to failed requests
   return render_template('index.html')
if __name__ == '__main__':
   app.run(port=5000)
