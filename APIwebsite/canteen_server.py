from flask import Flask, jsonify, request
app = Flask(__name__)
menu = {"poha": 30, "tea": 25, "sandwich": 50}
@app.route("/menu", methods=['GET'])
def get_menu():
    return jsonify(menu)

@app.route("/order", methods=["POST"])
def place_order():
    order = request.get_json()
    item = order["item"]
    quantity = order["quantity"]
    total = menu[item] * quantity
    return jsonify({
        "order_id": 12345,
        "total": total,
        "status": "Order placed successfully"
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)  