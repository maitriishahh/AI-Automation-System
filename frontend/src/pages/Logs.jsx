import { useEffect, useState } from "react";
import API from "../services/api";

function Logs() {

  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetchLogs();
  }, []);

  const fetchLogs = async () => {

    try {

      const response = await API.get(
        "/dashboard/logs"
      );

      setLogs(response.data);

    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="p-6">

      <h1 className="text-3xl font-bold mb-6">
        Workflow Logs
      </h1>

      <div className="bg-white rounded-xl shadow overflow-hidden">

        <table className="w-full">

          <thead className="bg-gray-100">

            <tr>

              <th className="p-4 text-left">
                Workflow
              </th>

              <th className="p-4 text-left">
                Status
              </th>

              <th className="p-4 text-left">
                Started
              </th>

              <th className="p-4 text-left">
                Finished
              </th>

            </tr>

          </thead>

          <tbody>

  {logs.length === 0 ? (

    <tr>

      <td
        colSpan="4"
        className="p-6 text-center text-gray-500"
      >
        No logs found
      </td>

    </tr>

  ) : (

    logs.map((log) => (

      <tr
        key={log.id}
        className="border-t"
      >

        <td className="p-4">
          {log.workflow_name}
        </td>

        <td className="p-4">

          <span
            className={
              log.status === "failed"
                ? "text-red-600 font-semibold"
                : "text-green-600 font-semibold"
            }
          >
            {log.status}
          </span>

        </td>

        <td className="p-4">
          {new Date(log.started_at).toLocaleTimeString()}
        </td>

        <td className="p-4">
          {log.finished_at
  ? new Date(log.finished_at).toLocaleTimeString()
  : "Running"}
        </td>

      </tr>

    ))

  )}

</tbody>

        </table>

      </div>

    </div>
  );
}

export default Logs;