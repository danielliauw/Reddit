from flask import Flask, render_template
app = Flask(__name__)

postList = {'test': 1}

@app.route('/')
def home():
    return render_template('home.html',posts = postList)

@app.route('/submit_post')
def submit_post():
	return render_template('submit_post.html',posts = postList)
	

	
if __name__ == "__main__":
    app.run()