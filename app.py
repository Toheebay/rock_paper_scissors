from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Choices available in the game
choices = ["rock", "paper", "scissors"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie! 🤝"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win! for PLP Game🎉"
    else:
        result = "Computer Wins! 😢"

    return jsonify({'user_choice': user_choice, 'computer_choice': computer_choice, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
