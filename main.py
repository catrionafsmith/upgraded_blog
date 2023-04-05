from flask import Flask, render_template
import urllib.request, requests, json
url = "https://api.npoint.io/5cb04341e30db4f385c2"
posts = requests.get(url).json()
    # data = response.text
    # posts = json.loads(data)

app = Flask(__name__)

@app.route('/')
def go_home():
    return render_template('index.html', posts=posts)

@app.route('/about.html')
def go_about():
    return render_template('about.html')

@app.route('/contact.html')
def go_contact():
    return render_template('contact.html')

@app.route('/post.html/<int:id>')
def post(id):
    return render_template('post.html', posts=posts, id=id)

if __name__ == "__main__":
    app.run(debug=True, port=8080)