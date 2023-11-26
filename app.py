from flask import Flask, render_template

app = Flask(__name__)

# Define routes for each HTML file
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/event')
def event():
    return render_template('event.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
