from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

COLORS = ['black', 'brown', 'gold', 'green', 'white']

@app.route('/')
def home():
    """Home page where users can place bets."""
    return render_template('home.html', colors=COLORS)


@app.route('/bet', methods=['POST'])
def bet():
    """Process user's bet and send them to the race page."""
    user_bet = request.form.get('color')
    return render_template('race.html', user_bet=user_bet)


@app.route('/race_data', methods=['GET'])
def race_data():
    """Generate random race data."""
    finish_line = 500  # The finish line position
    turtles = {color: 0 for color in COLORS}  # Initialize positions
    winner = None

    while not winner:
        for color in turtles:
            turtles[color] += random.randint(1, 10)  # Random progress
            if turtles[color] >= finish_line:
                winner = color
                break

    return jsonify({"positions": turtles, "winner": winner})


if __name__ == "__main__":
    app.run(debug=True)
