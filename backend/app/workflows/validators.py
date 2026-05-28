from app.workflows.constants import (
    SUPPORTED_NODE_TYPES,
    SUPPORTED_OPERATORS
)


class WorkflowValidator:

    @staticmethod
    def validate(workflow_json: dict):

        nodes = workflow_json.get("nodes", [])

        if not nodes:
            raise Exception("Workflow must contain nodes")

        for node in nodes:

            node_type = node.get("type")

            if node_type not in SUPPORTED_NODE_TYPES:
                raise Exception(
                    f"Invalid node type: {node_type}"
                )

          
            if node_type == "condition":

                operator = node.get("operator")

                if operator not in SUPPORTED_OPERATORS:
                    raise Exception(
                        f"Unsupported operator: {operator}"
                    )

            
            if node_type in ["action", "trigger"]:

                if not node.get("service"):
                    raise Exception(
                        "Service missing in node"
                    )

        return True