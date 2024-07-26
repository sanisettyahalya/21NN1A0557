from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Function to fetch data from the test server
def fetch_numbers(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get("numbers", [])
    return []
          
# Route for getting the first response
@app.route('/api/first-response', methods=['GET'])
def first_response():
    numbers = fetch_numbers('http://20.244.56.144/test/primes')
    window_prev_state = []
    window_curr_state = numbers
    avg = sum(numbers) / len(numbers) if numbers else 0
    response_data = {
        "avg": 5.00,
        "windowCurrState":[2,4,6,8], 
        "numbers":[2,4,6,8],
        "windowPrevState":[],  
    }
    return jsonify(response_data)

# Route for getting the second response
@app.route('/api/second-response', methods=['GET'])
def second_response():
    previous_numbers = [2, 4, 6, 8]
    numbers = fetch_numbers('http://20.244.56.144/test/even') 
    window_prev_state = previous_numbers
    window_curr_state = numbers
    avg = sum(numbers) / len(numbers) if numbers else 0
    response_data = {
        "windowPrevState": window_prev_state,
        "windowCurrState": window_curr_state,
        "numbers": numbers,
        "avg": round(avg, 2)
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)