# Masterblog API

A full-stack blogging application with a RESTful API backend built with Flask and a frontend interface. This project demonstrates CRUD operations, API documentation with Swagger, and a clean separation between backend and frontend components.

## Features

- **RESTful API** for blog post management
- **CRUD Operations**: Create, Read, Update, and Delete blog posts
- **Search & Filter**: Search posts by title, content, author, or date
- **Sorting**: Sort posts by title, content, author, or date in ascending/descending order
- **API Documentation**: Interactive Swagger UI documentation
- **CORS Enabled**: Cross-Origin Resource Sharing for frontend-backend communication
- **JSON Storage**: Simple file-based data persistence
- **Date Validation**: Ensures proper date formatting (YYYY-MM-DD)

## Tech Stack

### Backend
- **Flask** 3.1.2 - Web framework
- **Flask-CORS** 6.0.1 - Cross-Origin Resource Sharing
- **Flask-Swagger-UI** 5.21.0 - API documentation

### Frontend
- HTML/CSS/JavaScript
- Flask templating

## Project Structure

Masterblog-API/  
├── backend/  
│ ├── backend_app.py # Main Flask API application  
│ ├── posts.json # Blog posts data storage  
│ └── static/ # Swagger documentation files  
├── frontend/  
│ ├── frontend_app.py # Frontend Flask application  
│ ├── static/ # CSS and JavaScript files  
│ └── templates/ # HTML templates  
├── requirements.txt # Python dependencies  
├── posts.json # Root-level posts storage  
└── LICENSE # MIT License

## Installation

### Prerequisites
- Python 3.7 or higher
- pip

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Miami05/Masterblog-API.git
```
```bash
cd Masterblog-API
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage

### Running the Backend API

```bash
cd backend
```
```bash
python backend_app.py
```

The API will be available at `http://localhost:5002`

### Running the Frontend
```bash
cd frontend
```
```bash
python frontend_app.py
```

The frontend will be available at the configured port (check `frontend_app.py`)

## API Endpoints

### Get All Posts
```
GET /api/posts
```
**Query Parameters:**
- `sort` - Field to sort by (title, content, author, date)
- `direction` - Sort direction (asc, desc)

### Search Posts
```
GET /api/posts/search
```
**Query Parameters:**
- `title` - Search by title
- `content` - Search by content
- `author` - Search by author
- `date` - Search by date (YYYY-MM-DD)

### Create a Post
```
POST /api/posts
```
**Request Body:**
```
{  
"title": "Post Title",  
"content": "Post content here",  
"author": "Author Name",  
"date": "2025-11-24"  
}
```

### Update a Post
```
PUT /api/posts/{post_id}
```
**Request Body:**
```
{  
"title": "Updated Title",  
"content": "Updated content",  
"author": "Updated Author",  
"date": "2025-11-24"  
}
```


### Delete a Post
```
DELETE /api/posts/{post_id}
```


## API Documentation

Interactive API documentation is available via Swagger UI when the backend is running:

```
http://localhost:5002/api/docs
```

## Data Model

Each blog post has the following structure:

```
{  
"id": 1,  
"title": "Post Title",  
"content": "Post content",  
"author": "Author Name",  
"date": "2025-11-24"  
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200` - Success
- `201` - Created
- `400` - Bad Request (invalid data)
- `404` - Not Found (post doesn't exist)

## Development

### Adding New Features

1. Backend changes go in `backend/backend_app.py`
2. Frontend changes go in the `frontend/` directory
3. Update Swagger documentation in `backend/static/`

### Testing

Test the API endpoints using:
- Swagger UI (`/api/docs`)
- Postman or similar API testing tools
- curl commands

Example curl command:
```
curl -X POST http://localhost:5002/api/posts
-H "Content-Type: application/json"  
-d '{"title":"Test","content":"Content","author":"Author"}'
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- Built with Flask framework
- API documentation powered by Swagger UI
