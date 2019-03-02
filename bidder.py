import uuid
import time
import random

from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/make-bid')
def create_bid():
    placement_id = request.args.get('placement-id')
    # time.sleep(1)
    if placement_id is None:
        return jsonify({'error': 'placement-id is needed in query params!'}), 400

    to_bid = bool(random.getrandbits(1))
    if to_bid:
        bid = {
            "id": uuid.uuid4(),
            "placementID": placement_id,
            "bidPrice": random.randint(5, 10),
            "currency": "USD"
        }
        return jsonify(bid), 200
    else:
        return jsonify(), 204


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
