from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

postList = {'test': 1}

@app.route('/')
def home():
    return render_template('home.html',posts = postList)

@app.route('/submit_post',methods = ['GET','POST'])
def submit_post():
	if request.method == 'POST':
		title = request.form['post_title']
		postList[title] = 1
		return redirect(url_for('home'))
	return render_template('submit_post.html',posts = postList)
	

	
if __name__ == "__main__":
    app.run()