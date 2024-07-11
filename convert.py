from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/convert_timestamp', methods=['GET'])
def convert_timestamp():
    try:
        timestamp = int(request.args.get('timestamp'))
        # If the timestamp is in milliseconds, divide by 1000
        # Example: timestamp /= 1000

        formatted_date = datetime.utcfromtimestamp(timestamp).strftime('%a %d %b %Y, %H:%M:%S GMT+0530')
        return jsonify({'formatted_date': formatted_date})
    except ValueError:
        return jsonify({'error': 'Invalid timestamp format'}), 400

if __name__ == '__main__':
    app.run(debug=True)
