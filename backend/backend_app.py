import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import datetime

app = Flask(__name__, static_folder='static')
CORS(app)  # enable CORS

# Swagger configuration
SWAGGER_URL = "/api/docs"
API_URL = "/static/masterblog.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': 'Masterblog API'}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

CORS(app)  # This will enable CORS for all routes
FILENAME = 'posts.json'
def read_posts():
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_posts(posts):
    with open(FILENAME, 'w') as f:
        json.dump(posts, f, indent=4)

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = read_posts()
    sort_field = request.args.get('sort')
    direction = request.args.get('direction', 'asc')
    valid_fields = ["title", "content", "author", "date"]
    if sort_field:
        if sort_field not in valid_fields:
            return jsonify({"error": f"Invalid sort field: {sort_field}"}), 400
        reverse = direction == 'desc'
        if sort_field == 'date':
            posts.sort(key=lambda p: datetime.strptime(p['date'], "%Y-%m-%d"), reverse=reverse)
        else:
            posts.sort(key=lambda p: p[sort_field].lower(), reverse=reverse)
    return jsonify(posts), 200


@app.route('/api/posts/search', methods=["GET"])
def search_posts():
    title_query = request.args.get('title', '').lower()
    content_query = request.args.get('content', '').lower()
    author_query = request.args.get('author', '').lower()
    date_query = request.args.get('date', '')
    posts = read_posts()
    results = []
    for post in posts:
        title_match = title_query in post['title'].lower() if title_query else False
        content_match = content_query in post['content'].lower() if content_query else False
        author_match = author_query in post['author'].lower() if author_query else False
        date_match = date_query == post['date'] if date_query else False

        if title_match or content_match or author_match or date_match:
            results.append(post)

    return jsonify(results), 200

@app.route('/api/posts/<int:post_id>', methods=["DELETE"])
def delete_post(post_id):
    posts = read_posts()
    post_to_delete = next((post for post in posts if post["id"] == post_id), None)
    if not post_to_delete:
        return jsonify({"error": f"Post with id {post_id} not found"}), 404
    posts.remove(post_to_delete)
    write_posts(posts)
    return jsonify({"message": f"Post with id {post_id} has been deleted successfully"}), 200

@app.route('/api/posts/<int:post_id>', methods=["PUT"])
def update_post(post_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    posts = read_posts()
    post_to_update = next((post for post in posts if post["id"] == post_id), None)
    if not post_to_update:
        return jsonify({"error": f"Post with id {post_id} not found"}), 404
    title = data.get('title', post_to_update['title'])
    content = data.get('content', post_to_update['content'])
    author = data.get('author', post_to_update['author'])
    date_str = data.get('date', post_to_update['date'])

    if not validate_date(date_str):
        return jsonify({"error": "Invalid date format, must be YYYY-MM-DD"}), 400

    post_to_update.update({
        "title": title,
        "content": content,
        "author": author,
        "date": date_str
    })
    write_posts(posts)
    return jsonify(post_to_update), 200


@app.route('/api/posts', methods=['POST'])
def add_posts():
    data = request.get_json()
    if not data:
        return jsonify({"error: Request body must be JSON"}), 400
    title = data.get('title')
    content = data.get('content')
    author = data.get('author')
    date_str = data.get('date', datetime.today().strftime("%Y-%m-%d"))
    missing_field = []
    if not title:
        missing_field.append(title)
    if not content:
        missing_field.append(content)
    if not validate_date(date_str):
        return jsonify({"error": "Invalid date must be YYYY-MM-DD"}), 400
    if missing_field:
        return jsonify({"error": f"Missing field {', '.join(missing_field)}"}), 400
    posts = read_posts()
    new_id = max((post["id"] for post in posts), default=0) + 1
    new_posts = {
        "id": new_id,
        "title": title,
        "content": content,
        "author": author,
        "date": date_str
    }
    posts.append(new_posts)
    write_posts(posts)
    return jsonify(new_posts), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
