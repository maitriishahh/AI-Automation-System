from app.workflows.constants import(
    EQUALS,
    NOT_EQUALS,
    GREATER_THAN,
    LESS_THAN,
    GREATER_THAN_EQUAL,
    LESS_THAN_EQUAL,
    CONTAINS
)

class ConditionEvaluator:
    @staticmethod
    def evaluate(payload: dict, condition_node: dict) -> bool:

        field = condition_node.get("field")
        operator = condition_node.get("operator")
        expected_value = condition_node.get("value")

        actual_value = payload.get(field)

        if operator == EQUALS:
            return actual_value == expected_value

        elif operator == NOT_EQUALS:
            return actual_value != expected_value

        elif operator == GREATER_THAN:
            return actual_value > expected_value

        elif operator == LESS_THAN:
            return actual_value < expected_value

        elif operator == GREATER_THAN_EQUAL:
            return actual_value >= expected_value

        elif operator == LESS_THAN_EQUAL:
            return actual_value <= expected_value

        elif operator == CONTAINS:
            return expected_value in actual_value

        raise ValueError(f"Unsupported operator: {operator}")