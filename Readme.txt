Reddit clone
Developed by Daniel Liauw on 26 April 2017

Website is developed with python flask so that post/get method can be used.

Data structure used is dictionary (to make it more simple, was thinking about using json 
but since there's no need for the data to be stored even after closing the apps), 
since there is only 2 variables (post title and amount of votes)

upvoting and creating a new post uses a similar POST method.

title of post is assigned to each upvote/downvote button's value, so that we can know which button is clicked and make it easier to update the dictionary.

static/style.css used for all page.

templates/home.html is the home page that display list of posts.
templates/submit_post.html is the page where users can submit a new post.

To run locally, go to the Reddit.py directory and type "python Reddit.py" on the command line.
Then, open localhost:5000 on browser.
Other users on the same network can open on machineIP:5000


Format of the list of posts is: votecount title
Users won't be able to type more than 255 char in the input field.

Assumptions:
no users that submit the same title.