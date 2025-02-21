from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()
        if not data or 'data' not in data:
            return jsonify({"is_success": False, "error": "Invalid input"}), 400

        
        items = data.get('data', [])

        
        numbers = [item for item in items if item.isdigit()]
        alphabets = [item for item in items if item.isalpha()]

        
        highest_alphabet = []
        if alphabets:
            highest_alphabet = [max(alphabets, key=lambda x: x.upper())]

        
        user_id = "Ayush_kumar_singh_05072003"
        college_email = "22bcs12351@cuchd.in"
        college_roll_number = "22BCS12351"

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": college_email,
            "roll_number": college_roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)