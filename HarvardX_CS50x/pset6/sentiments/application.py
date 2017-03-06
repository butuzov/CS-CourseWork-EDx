from flask import Flask, request, url_for, redirect, render_template
import helpers, os, sys
from analyzer import Analyzer


app = Flask(__name__)

def main():
	app.run(debug=True, port=8080, host="0.0.0.0")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/search")
def search():

	# validate screen_name
	screen_name = request.args.get("screen_name", "").lstrip("@")
	if not screen_name:
		return redirect(url_for("index"))

	# get screen_name's tweets
	tweets = helpers.get_user_timeline(screen_name, count=50 )

	# absolute paths to lists
	positives = os.path.join(sys.path[0], "positive-words.txt")
	negatives = os.path.join(sys.path[0], "negative-words.txt")

	# instantiate analyzer
	analyzer = Analyzer(positives, negatives)

	# analyze word
	positive, negative, neutral = 0, 0, 0

	for tweet in tweets:
		score = analyzer.analyze( tweet )

		if score > 0.0:
			positive += 1
		elif score < 0.0:
			negative += 1
		else:
			neutral += 1

	positive, negative, neutral = positive / len(tweets) , negative / len(tweets), neutral / len(tweets)


	# generate chart
	chart = helpers.chart(positive, negative, neutral)

	# render results
	return render_template("search.html", chart=chart, screen_name=screen_name)


if __name__ == "__main__":
	main()
