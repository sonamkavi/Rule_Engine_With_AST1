# ----------------------------------------------
# IMPORT LIBRARIES
# ----------------------------------------------

import re  # Regular expression library for tokenizing the rule strings


# CLASS DEFINITION FOR NODE
class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type =type  # 'operator' or 'operand'
        self.value = value      # e.g., 'AND', 'OR', or a tuple (attribute, operator, value)
        self.left = left        # left child Node
        self.right = right      # right child Node


# FUNCTION TO TOKENIZE RULE STRING
def tokenize(rule_string):
    # Use regex to split by spaces and symbols like '(', ')', '>', '=', etc.
    return re.findall(r"\w+|[><=()]|AND|OR", rule_string)


# FUNCTION TO PARSE TOKENS INTO AST
def parse_tokens_to_ast(tokens):
    # Build the AST recursively from the tokens
    # This function needs implementation to handle operator precedence
    # For demonstration, assume a simple left-to-right parse:
    root = Node('operand', value=(tokens[0], tokens[1], int(tokens[2])))
    return root


# FUNCTION TO CREATE RULE (AST)
def create_rule(rule_string):
    tokens = tokenize(rule_string)  # Split into tokens like ['(', 'age', '>', '30', 'AND', ...]
    ast = parse_tokens_to_ast(tokens)  # Parse tokens and return AST
    return ast

def compare(attribute, comparison_value, operator):
    """Compare the attribute against the comparison_value based on the given operator."""
    if operator == '>':
        return attribute > comparison_value
    elif operator == '<':
        return attribute < comparison_value
    elif operator == '=':
        return attribute == comparison_value
    elif operator == '!=':
        return attribute != comparison_value
    elif operator == '>=':
        return attribute >= comparison_value
    elif operator == '<=':
        return attribute <= comparison_value
    else:
        raise ValueError(f"Invalid operator: {operator}")
    
# FUNCTION TO COMBINE MULTIPLE ASTS
def combine_rules(rule_asts):
    if len(rule_asts) == 1:
        return rule_asts[0]
    
    # Combine the first two ASTs with an 'AND' operator, then recursively combine
    combined = Node('operator', 'AND', rule_asts[0], rule_asts[1])
    return combine_rules([combined] + rule_asts[2:])


# FUNCTION TO EVALUATE RULE (AST) AGAINST DATA


def evaluate_rule(ast, data):
    if ast.type == "operand":
        attribute_name = ast.value[0]  # Get the attribute name from the operand
        operator = ast.value[1]          # Get the comparison operator
        comparison_value = ast.value[2]  # Get the value to compare against
        attribute = data.get(attribute_name)  # Get the actual attribute value from the data
        return compare(attribute, comparison_value, operator)  # Call the compare function
    elif ast.type == "operator":
        left_eval = evaluate_rule(ast.left, data)
        right_eval = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_eval and right_eval
        elif ast.value == "OR":
            return left_eval or right_eval
