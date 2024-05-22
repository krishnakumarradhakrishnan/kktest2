import json

from flask import Flask, request, jsonify

app = Flask(__name__)
data = {"incomes": [{"name":"Krishna","rollno":2001115}]}

@app.route('/incomes', methods=['POST'])
def incomes_post():
    new_income = request.get_json()
    data["incomes"].append(new_income)
    with open('output.json', 'w') as f:
        json.dump(data, f)
    return jsonify({"message": "Income added successfully"}), 201

@app.route('/incomes/<int:index>', methods=['GET','PUT','DELETE'])
def incomes(index):

    if request.method == 'GET':
        with open('output.json', 'r') as f:
            loaded_data = json.load(f)

            if 0 <= index < len(loaded_data["incomes"]):
                name = loaded_data["incomes"][index]["name"] 
                rollno = loaded_data["incomes"][index]["rollno"]
            else:
                name = "world"
                rollno="NA"
            return jsonify({"message": f"Hello {name}, Your RollNo: {rollno}"}), 200  

            
    if request.method == 'PUT':
        with open('output.json', 'r') as f:
            loaded_data = json.load(f)
            if 0 <= index < len(loaded_data["incomes"]):
                updated_income = request.get_json()
                loaded_data["incomes"][index] = updated_income
                with open('output.json', 'w') as f:
                    json.dump(loaded_data, f)
                return jsonify({"message": "Income updated successfully"}), 200
            else:
                return jsonify({"message": "Index out of range"}), 404

    if request.method == 'DELETE':
        with open('output.json', 'r') as f:
            loaded_data = json.load(f)
            if 0 <= index < len(loaded_data["incomes"]):
                del loaded_data["incomes"][index]
                with open('output.json', 'w') as f:
                    json.dump(loaded_data, f)
                return jsonify({"message": "Income deleted successfully"}), 200
            else:
                return jsonify({"message": "Index out of range"}), 404

if __name__ == '__main__':
    app.run(debug=True,port=9876)
