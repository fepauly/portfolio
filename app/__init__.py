from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.get('/experience')
    def get_experience():
        return render_template('partials/tab_titles_experience.html')

    @app.get('/skills')
    def get_skills():
        return render_template('partials/tab_titles_skills.html')
        
    @app.get('/education')
    def get_education():
        return render_template('partials/tab_titles_education.html')

    return app

