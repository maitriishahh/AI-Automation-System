from app.workflows.constants import (

    # node types
    TRIGGER_NODE,
    CONDITION_NODE,
    ACTION_NODE,

    # supported values
    SUPPORTED_NODE_TYPES,
    SUPPORTED_OPERATORS,
    SUPPORTED_SERVICES
)


class WorkflowValidator:

    @staticmethod
    def validate(workflow_json: dict):

        nodes = workflow_json.get("nodes", [])


        if not nodes:
            raise ValueError(
                "Workflow must contain nodes"
            )


        for node in nodes:


            node_id = node.get("id")

            if not node_id:
                raise ValueError(
                    "Node ID missing"
                )

            node_type = node.get("type")

            if node_type not in SUPPORTED_NODE_TYPES:
                raise ValueError(
                    f"Invalid node type: {node_type}"
                )


            if node_type == CONDITION_NODE:

                operator = node.get("operator")

                if operator not in SUPPORTED_OPERATORS:
                    raise ValueError(
                        f"Unsupported operator: {operator}"
                    )

                if not node.get("field"):
                    raise ValueError(
                        "Condition field missing"
                    )

                if "value" not in node:
                    raise ValueError(
                        "Condition value missing"
                    )

            if node_type in [ACTION_NODE, TRIGGER_NODE]:

                service = node.get("service")

                if not service:
                    raise ValueError(
                        "Service missing in node"
                    )

                if service not in SUPPORTED_SERVICES:
                    raise ValueError(
                        f"Unsupported service: {service}"
                    )


        trigger_count = len([
            node for node in nodes
            if node.get("type") == TRIGGER_NODE
        ])

        if trigger_count == 0:
            raise ValueError(
                "Workflow must contain at least one trigger node"
            )

        return True