from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

postList = {}

@app.route('/', methods = ['GET','POST'])
def home():
	##upvote and downvote changes
	if request.method == 'POST':
		##request.form['upvote'] is the post title, as assigned in the html code
		if "upvote" in request.form:
			postList[request.form['upvote']] +=1
			return redirect(url_for('home'))
		elif "downvote" in request.form:
			postList[request.form['downvote']] -=1
			return redirect(url_for('home'))
			
	#display the posts in descending order
	sorted_posts = sorted(postList.items(), key = lambda x:x[1], reverse = True)[:20]
	return render_template('home.html',posts = sorted_posts)

@app.route('/submit_post',methods = ['GET','POST'])
def submit_post():
	##add the post title to the dictionary when submitted, also set the default vote to 1
	if request.method == 'POST':
		title = request.form['post_title']
		postList[title] = 1
		return redirect(url_for('home'))
	return render_template('submit_post.html',posts = postList)
	
if __name__ == "__main__":
    app.run(host='0.0.0.0')