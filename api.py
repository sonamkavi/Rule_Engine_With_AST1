
# IMPORT LIBRARIES AND MODULES
from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule, Node  # Make sure to import Node class
from database import insert_rule, fetch_rules

# INITIALIZE FLASK APP
app = Flask(__name__)  # Create a Flask app instance


# CREATE RULE ENDPOINT

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json['rule_string']  # Get the rule string from the request body
    ast = create_rule(rule_string)     # Convert the rule string to an Abstract Syntax Tree (AST)

    # Store the rule in the database
    insert_rule(rule_string, str(ast))
    return jsonify({'ast': str(ast)})


# COMBINE RULES ENDPOINT
@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json['rules']
    combined_ast = combine_rules([create_rule(rule) for rule in rules])
    return jsonify({'combined_ast': str(combined_ast)})

# EVALUATE RULE ENDPOINT
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    ast_data = request.json['ast']  # This should be a JSON object
    data = request.json['data']

    # Function to reconstruct the AST from the incoming JSON data
    def reconstruct_node(node_data):
        if node_data['type'] == 'operand':
            return Node(type='operand', value=node_data['value'])
        elif node_data['type'] == 'operator':
            left_child = reconstruct_node(node_data['left'])
            right_child = reconstruct_node(node_data['right'])
            return Node(type='operator', value=node_data['value'], left=left_child, right=right_child)

    try:
        ast = reconstruct_node(ast_data)  # Reconstruct the AST
        result = evaluate_rule(ast, data)  # Evaluate the rule
        return jsonify({'result': result})
    except Exception as e:
        print("Error:", str(e))  # Print the error message for debugging
        return jsonify({"error": str(e)}), 400


# RUN THE APP
if __name__ == '__main__':
    app.run(debug=True)
