from flask import Flask, jsonify, request
# initialize our Flask application
app= Flask(__name__)
@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        cid = posted_data['id']
        return jsonify({"code":"200","id":cid})
if __name__ == '__main__':
   app.run(port=5001)
