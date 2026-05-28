from app.workflows.executor import NodeExecutor

class WorkflowEngine:

    @staticmethod
    async def run_workflow(workflow_json: dict, payload: dict):

        nodes = workflow_json.get("nodes", [])

        execution_results = []


        for node in nodes:

            result = await NodeExecutor.execute_node(
                node=node,
                payload=payload
            )

            execution_results.append(result)


            if (
                result.get("status") == "condition_evaluated"
                and result.get("result") is False
            ):

                return {
                    "workflow_status": "stopped",
                    "reason": "condition_failed",
                    "execution_results": execution_results
                }


        return {
            "workflow_status": "completed",
            "execution_results": execution_results
        }