# Name : Jay mangukiya
# PRN : 26070122272
# Batch : CSE C3
from flask import Flask, jsonify, request, render_template_string
app = Flask(__name__)
menu = {"poha": 30, "tea": 25, "sandwich": 50}
@app.route("/menu", methods=['GET'])
def get_menu():
    html = "<html><body><h1>Canteen Menu</h1><ul>"
    for item, price in menu.items():
        html += f"<li>{item} - {price}</li>"
    html += "</ul></body></html>"
    return html

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