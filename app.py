from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
from authenticate import authenticate
from scraper import start_scraper
from database import get_results, get_status, save_scrape_job
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Configure rate limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route('/start', methods=['POST'])
@limiter.limit("10 per minute")
def start():
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    try:
        job_id = start_scraper(data)
        save_scrape_job(job_id, data)
        return jsonify({"message": "Scrape started", "job_id": job_id}), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/results/<job_id>', methods=['GET'])
def results(job_id):
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    try:
        results = get_results(job_id)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status/<job_id>', methods=['GET'])
def status(job_id):
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    try:
        status = get_status(job_id)
        return jsonify({"job_id": job_id, "status": status}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)