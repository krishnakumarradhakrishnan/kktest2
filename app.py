import json
#test meaasage for branch
from flask import Flask, request, jsonify

app = Flask(__name__)
data = {"Students": [{"name":"Krishna","rollno":2001115}]}

@app.route('/Students', methods=['POST'])
def Students_post():
    new_income = request.get_json()
    data["Students"].append(new_income)
    with open('output.json', 'w') as f:
        json.dump(data, f)
    return jsonify({"message": "Income added successfully"}), 201

@app.route('/Students/<int:index>', methods=['GET','PUT','DELETE'])
def Students(index):

    if request.method == 'GET':
        with open('output.json', 'r') as f:
            loaded_data = json.load(f)

            if 0 <= index < len(loaded_data["Students"]):
                name = loaded_data["Students"][index]["name"] 
                rollno = loaded_data["Students"][index]["rollno"]
            else:
                name = "world"
                rollno="NA"
            return jsonify({"message": f"Hello {name}, Your RollNo: {rollno}"}), 200  

            
    if request.method == 'PUT':
        with open('output.json', 'r') as f:
            loaded_data = json.load(f)
            if 0 <= index < len(loaded_data["Students"]):
                updated_income = request.get_json()
                loaded_data["Students"][index] = updated_income
                with open('output.json', 'w') as f:
                    json.dump(loaded_data, f)
                return jsonify({"message": "Income updated successfully"}), 200
            else:
                return jsonify({"message": "Index out of range"}), 404

    if request.method == 'DELETE':
        with open('output.json', 'r') as f:
            loaded_data = json.load(f)
            if 0 <= index < len(loaded_data["Students"]):
                del loaded_data["Students"][index]
                with open('output.json', 'w') as f:
                    json.dump(loaded_data, f)
                return jsonify({"message": "Income deleted successfully"}), 200
            else:
                return jsonify({"message": "Index out of range"}), 404

if __name__ == '__main__':
    app.run(debug=True,port=9876)
