from flask import Flask,request, render_template

app= Flask (__name__)

########################### Mapping Multiple URLS#############
@app.route('/')
@app.route('/<user>')
def index(user=None):
	return render_template("user.html",user=user)
	#return 'This is the Hoempage'

@app.route('/about')
def about():
	return 'This is the About Page'

########################Passing variable##################
# @app.route('/profile1/<user>')
# def profile(user):
# 	return '<h2>This is the About '+user+'<h2>'

#######################Passing int variable################
@app.route('/post/<int:postid>')
def post(postid):
	return '<h2>Post ID is '+str(postid)+'<h2>'

#########################Method Used#######################

@app.route('/method',methods=['GET','POST'])
def method():
	if request.method=='GET':
		return '<h2>Method Used is '+str(request.method)+'<h2>'
	else:
		return '<h2>Method Used is '+str(request.method)+'<h2>'


############################ HTML Templates################
@app.route('/profile/<name>')
def profile(name):
	return render_template("profile.html",name=name)


############################ Passing List #################
@app.route('/shopping')
def shopping():
	food=["milk","bread","butter"]
	return render_template("shopping.html",food=food)


if __name__=="__main__":
	app.run(debug=True)
