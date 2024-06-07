from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

answers = [
    "3/4", "14/15", "1 et 1/8", "2/3", "1 et 1/2",
    "29/35", "1 et 1/6", "7/11", "1 et 1/2", "7/12",
    "1/2", "1/3", "5/16", "7/10", "5/16",
    "1/2", "1/2", "1/2", "1/3", "1/3",
    "1/8", "1/21", "13/18", "1/2", "3/8",
    "11/20", "3/10", "1/3", "1/3", "15/22",
    "3/10", "8/15", "3/8", "5/9", "12/35",
    "3/10", "3/20", "5/21", "5/24", "8/45",
    "5/8", "2/21", "8/27", "2/5", "15/56"
]

entered_numbers = set()

def get_answer(number):
    if 1 <= number <= 45:
        return answers[number - 1]
    else:
        return "SVP entrez un numéro entre 1 et 45"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    number = data.get('number')

    if not isinstance(number, int):
        return jsonify({"error": "Erreur! SVP entrer un numéro valide!"})

    if not (1 <= number <= 45):
        return jsonify({"error": "SVP entrez un numéro entre 1 et 45"})

    if number in entered_numbers:
        return jsonify({"error": f"Le numéro {number} a déjà été entré. Essayez un autre numéro."})
    
    entered_numbers.add(number)
    answer = get_answer(number)
    return jsonify({"result": answer})

if __name__ == '__main__':
    app.run(debug=True)