from app.workflows.conditions import ConditionEvaluator
from app.workflows.action_registry import get_action
from app.utils.retry import retry_handler

from app.workflows.constants import (
    TRIGGER_NODE,
    CONDITION_NODE,
    ACTION_NODE
)


class NodeExecutor:

    @staticmethod
    async def execute_node(node: dict, payload: dict):

        node_type = node.get("type")


        if node_type == TRIGGER_NODE:

            service_name = node.get("service")

            action_function = get_action(service_name)

            result = await retry_handler(action_function,
            payload)

            return {
                "status": "trigger_executed",
                "service": service_name,
                "result": result
            }


        elif node_type == CONDITION_NODE:

            result = ConditionEvaluator.evaluate(payload, node)

            return {
                "status": "condition_evaluated",
                "result": result
            }


        elif node_type == ACTION_NODE:

            service_name = node.get("service")

            action_function = get_action(service_name)

            result = await retry_handler(action_function,
            payload) 
            
            return {
                "status": "action_executed",
                "service": service_name,
                "result": result
            }

        raise ValueError(f"Unsupported node type: {node_type}")