from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

postList = {'test': 1}

@app.route('/', methods = ['GET','POST'])
def home():
	if request.method == 'POST':
		if "upvote" in request.form:
			postList[request.form['upvote']] +=1
			return redirect(url_for('home'))
		elif "downvote" in request.form:
			postList[request.form['downvote']] -=1
			return redirect(url_for('home'))
	sorted_posts = sorted(postList.items(), key = lambda x:x[1], reverse = True)[:20]
	return render_template('home.html',posts = sorted_posts)

@app.route('/submit_post',methods = ['GET','POST'])
def submit_post():
	if request.method == 'POST':
		title = request.form['post_title']
		postList[title] = 1
		return redirect(url_for('home'))
	return render_template('submit_post.html',posts = postList)
	

	
if __name__ == "__main__":
    app.run()