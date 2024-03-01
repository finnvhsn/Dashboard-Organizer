from project import create_app
from project.models import initialize_db


app = create_app()

initialize_db()

if __name__ == '__main__':
    app.run(debug=True)
    