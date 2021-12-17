from flask import Flask, jsonify, request
#importing Translator from googletrans.
from googletrans import Translator

# initialize our Flask application
app= Flask(__name__)
@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        cid = posted_data['id']
        return jsonify({"code":"200","id":cid})

@app.route("/apiprocessconverter", methods=["POST"])
def setApiprocessconverter():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        translator = Translator()
        translation = translator.translate(data, dest='en')
        return translation.text

if __name__ == '__main__':
   app.run(port=5001)
