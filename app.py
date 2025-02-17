from flask import Flask, render_template, url_for, redirect
import os

app = Flask(__name__, template_folder='.', static_folder='static')

# Ensure the static/images directory exists
os.makedirs(os.path.join(app.static_folder, 'images'), exist_ok=True)

@app.route('/linkedin')
def linkedin():
    return redirect('https://www.linkedin.com/in/malapaka-krishna-sairam')

@app.route('/github')
def github():
    return redirect('https://github.com/krishnasairammalapaka')

@app.route('/traffic-management')
def traffic_management():
    return render_template('traffic-management.html')

@app.route('/greens-cart')
def greens_cart():
    return render_template('greens-cart.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
