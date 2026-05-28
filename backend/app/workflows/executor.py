from app.workflows.conditions import (
    ConditionEvaluator
)

from app.workflows.action_registry import (
    get_action
)

from app.utils.retry import (
    retry_handler
)

from app.workflows.constants import (

    TRIGGER_NODE,
    CONDITION_NODE,
    ACTION_NODE,

    EXECUTION_SUCCESS,
    EXECUTION_FAILED
)


class NodeExecutor:

    @staticmethod
    async def execute_node(
        node: dict,
        payload: dict
    ):

        try:

            node_type = node.get("type")


            if node_type in [
                TRIGGER_NODE,
                ACTION_NODE
            ]:

                service_name = node.get("service")

                action_function = get_action(
                    service_name
                )

                result = await retry_handler(
                    action_function,
                    payload
                )

                return {
                    "status": EXECUTION_SUCCESS,
                    "node_type": node_type,
                    "service": service_name,
                    "result": result
                }


            elif node_type == CONDITION_NODE:

                result = ConditionEvaluator.evaluate(
                    payload,
                    node
                )

                return {
                    "status": EXECUTION_SUCCESS,
                    "node_type": node_type,
                    "result": result
                }

            raise ValueError(
                f"Unsupported node type: {node_type}"
            )

        except Exception as e:

            return {
                "status": EXECUTION_FAILED,
                "node_type": node.get("type"),
                "error": str(e)
            }