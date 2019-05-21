import os
import redis
from flask import Flask, render_template, jsonify

APP_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_FOLDER = os.path.join(APP_DIR, '../build/')
redis = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=os.environ['REDIS_DB_NO'])

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)

@app.route('/')
def root_url():
    return render_template('index.html')

@app.route('/api/json')
def api_json():
    response = jsonify({"targets": ["A001", "B001", "AB001", "BA001"]})
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)