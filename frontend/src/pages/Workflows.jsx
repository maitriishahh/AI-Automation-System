import { useEffect, useState } from "react";
import API from "../services/api";

function Workflows() {

  const [workflows, setWorkflows] = useState([]);

  useEffect(() => {
    fetchWorkflows();
  }, []);

  const fetchWorkflows = async () => {

    try {

      const response = await API.get(
        "/dashboard/workflows"
      );

      setWorkflows(response.data);

    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="p-6">

      <h1 className="text-3xl font-bold mb-6">
        Workflows
      </h1>

      <div className="bg-white rounded-xl shadow overflow-hidden">

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

            </tr>

          </thead>

          <tbody>

            {workflows.map((workflow) => (

              <tr
                key={workflow.workflow_id}
                className="border-t"
              >

                <td className="p-4">
                  {workflow.workflow_name}
                </td>

                <td className="p-4">
                  {workflow.total_runs}
                </td>

                <td className="p-4 text-green-600 font-semibold">
  {workflow.successful_runs}
</td>

                <td className="p-4 text-red-600 font-semibold">
  {workflow.failed_runs}
</td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default Workflows;