import { useEffect, useState } from "react";
import API from "../services/api";

function Workflows() {

  const [workflows, setWorkflows] = useState([]);

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    fetchWorkflows();

  }, []);

  // ==========================================
  // FETCH WORKFLOWS
  // ==========================================

  const fetchWorkflows = async () => {

    try {

      const response = await API.get(
        "/dashboard/workflows"
      );

      console.log(response.data);

      // MERGE SIMILAR WORKFLOWS

const mergedWorkflows = {};

response.data.forEach((workflow) => {

  const normalizedName =
    workflow.workflow_name
      .toLowerCase()
      .replace("workflow", "")
      .replace("automation", "")
      .trim();

  if (!mergedWorkflows[normalizedName]) {

    mergedWorkflows[normalizedName] = {
      ...workflow
    };

  } else {

    mergedWorkflows[normalizedName]
      .total_runs += workflow.total_runs;

    mergedWorkflows[normalizedName]
      .successful_runs += workflow.successful_runs;

    mergedWorkflows[normalizedName]
      .failed_runs += workflow.failed_runs;
  }
});

setWorkflows(
  Object.values(mergedWorkflows)
);
    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };

  // ==========================================
  // RUN WORKFLOW
  // ==========================================

  const runWorkflow = async (id) => {

    try {

      const response = await API.post(

        `/workflows/${id}/execute`,

        {
          trigger: "manual"
        }

      );

      console.log(response.data);

      alert("Workflow added to queue");

      fetchWorkflows();

    } catch (error) {

      console.log(error);

      alert("Workflow execution failed");

    }
  };

  return (

    <div className="p-8">

      {/* HEADER */}

      <div className="mb-8">

        <h1 className="text-4xl font-bold">
          Workflows
        </h1>

        <p className="text-gray-500 mt-2">
          Monitor workflow executions and automation performance
        </p>

      </div>

      {/* TABLE */}

      <div className="bg-white rounded-2xl shadow-xl overflow-hidden">

        <table className="w-full">

          <thead className="bg-gray-100">

            <tr>

              <th className="p-4 text-left">
                Workflow
              </th>

              <th className="p-4 text-left">
                Total Runs
              </th>

              <th className="p-4 text-left">
                Success
              </th>

              <th className="p-4 text-left">
                Failed
              </th>

              <th className="p-4 text-left">
                Success Rate
              </th>

              <th className="p-4 text-left">
                Action
              </th>

            </tr>

          </thead>

          <tbody>

            {loading ? (

              <tr>

                <td
                  colSpan="6"
                  className="p-6 text-center"
                >
                  Loading workflows...
                </td>

              </tr>

            ) : workflows.length === 0 ? (

              <tr>

                <td
                  colSpan="6"
                  className="p-6 text-center text-gray-500"
                >
                  No workflows found
                </td>

              </tr>

            ) : (

              workflows.map((workflow) => {

                const successRate = workflow.total_runs > 0

                  ? Math.round(
                      (
                        workflow.successful_runs /
                        workflow.total_runs
                      ) * 100
                    )

                  : 0;

                return (

                  <tr
                    key={workflow.workflow_id}
                    className="border-t hover:bg-gray-50 transition"
                  >

                    {/* WORKFLOW NAME */}

                    <td className="p-4">

                      <div className="font-semibold text-lg">
                        {workflow.workflow_name}
                      </div>

                    </td>

                    {/* TOTAL RUNS */}

                    <td className="p-4 font-medium">

                      {workflow.total_runs}

                    </td>

                    {/* SUCCESS */}

                    <td className="p-4">

                      <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-medium">

                        {workflow.successful_runs}

                      </span>

                    </td>

                    {/* FAILED */}

                    <td className="p-4">

                      <span className="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm font-medium">

                        {workflow.failed_runs}

                      </span>

                    </td>

                    {/* SUCCESS RATE */}

                    <td className="p-4">

                      <span className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm font-medium">

                        {successRate}%

                      </span>

                    </td>

                    {/* ACTION */}

                    <td className="p-4">

                      <button
                        onClick={() =>
                          runWorkflow(
                            workflow.workflow_id
                          )
                        }
                        className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg transition"
                      >
                        Run
                      </button>

                    </td>

                  </tr>

                );
              })

            )}

          </tbody>

        </table>

      </div>

    </div>

  );
}

export default Workflows;