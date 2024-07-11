from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/convert/<int:timestamp>')
def convert(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    formatted_time = dt.strftime('%B %d, %Y, %I:%M %p')
    return jsonify({"formatted_time": formatted_time})

if __name__ == '__main__':
    app.run(debug=True)
