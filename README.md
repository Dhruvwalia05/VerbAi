# VerbAi

VerbAi is a Django-based web application designed to provide ratings for uploaded stories, assessing their child-friendliness, and analyzing and providing the moral of the story. This project leverages artificial intelligence to analyze text and provide meaningful insights, making it a helpful tool for parents, educators, and writers.

## Features
- Upload stories in text format.
- Analyze the child-friendliness of the story.
- Generate a moral or lesson for the story.
- User-friendly interface for uploading and viewing results.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (with Django Templates)
- **Database**: SQLite
- **AI/ML**: Integrated AI models for story analysis

## Installation

### Prerequisites
- Python 3.8+
- Django (version compatible with the project requirements)
- Git (optional, for cloning the repository)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd VerbAi
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: .\env\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the application in your browser at `http://127.0.0.1:8000/`.

## Usage
- Navigate to the application’s homepage.
- Upload a story in text format using the provided interface.
- View the child-friendliness rating and the moral of the story.

## Project Structure
```
VerbAi/
|— .git/                # Git repository metadata
|— db.sqlite3          # SQLite database
|— manage.py           # Django management script
|— static/              # Static files (CSS, JS, Images)
|— story/               # Main application logic
|— templates/           # HTML templates
|— VerbAi/              # Project configuration files
|— LICENSE              # License information
```

## Contributors
- **Team Member 1**: Role (e.g., Backend Developer)
- **Team Member 2**: Role (e.g., Frontend Developer)
- **Team Member 3**: Role (e.g., AI Specialist)
- **Team Member 4**: Role (e.g., Project Manager)

## License
This project is licensed under the terms specified in the [LICENSE](./LICENSE) file.

## Acknowledgments
- Special thanks to the contributors and mentors who guided the development of VerbAi.
- Tools and libraries used include Django, Python, and AI models.

---

Feel free to contribute to this project by submitting issues or pull requests!

