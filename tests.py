"""
Unit tests for the Rule Engine.
These tests validate the core functionality of the rule engine, including rule creation, combination, and evaluation.
"""
import unittest
from rule_engine import create_rule, combine_rules, evaluate_rule

class TestRuleEngine(unittest.TestCase):
    def test_create_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)  # Use self.assertIsNotNone for better unittest integration

    def test_combine_rules(self):
        rule1 = create_rule("age > 30 AND department = 'Sales'")
        rule2 = create_rule("salary > 50000")
        combined = combine_rules([rule1, rule2])
        self.assertIsNotNone(combined)

    def test_evaluate_rule(self):
        data = {"age": 35, "department": "Sales", "salary": 60000}
        rule = create_rule("age > 30 AND department = 'Sales'")
        result = evaluate_rule(rule, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
