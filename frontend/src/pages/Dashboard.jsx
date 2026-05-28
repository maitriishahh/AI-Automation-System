import { useEffect, useState } from "react";
import API from "../services/api";
import StatsCard from "../components/StatsCard";

function Dashboard() {

  const [overview, setOverview] = useState(null);

  useEffect(() => {
    fetchOverview();
  }, []);

  const fetchOverview = async () => {
    try {

      const response = await API.get("/dashboard/overview");

      setOverview(response.data);

    } catch (error) {
      console.log(error);
    }
  };

  if (!overview) {
    return <div className="p-6">Loading...</div>;
  }

  return (
    <div className="p-6">

      <h1 className="text-3xl font-bold mb-6">
        Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <StatsCard
          title="Total Workflows"
          value={overview.total_workflows}
        />

        <StatsCard
          title="Workflow Runs"
          value={overview.workflow_runs}
        />

        <StatsCard
          title="Successful Runs"
          value={overview.successful_runs}
        />

        <StatsCard
          title="Failed Runs"
          value={overview.failed_runs}
        />

        <StatsCard
          title="Pending Jobs"
          value={overview.pending_jobs}
        />

        <StatsCard
          title="Success Rate"
          value={`${overview.success_rate}%`}
        />

        <div className="mt-10 grid grid-cols-1 md:grid-cols-2 gap-6">

  <div className="bg-white rounded-xl shadow p-6">

    <h2 className="text-xl font-semibold mb-4">
      System Status
    </h2>

    <div className="space-y-2">

      <p>
        Queue Monitoring Active
      </p>

      <p>
        Workflow Engine Running
      </p>

      <p>
        Integrations Connected
      </p>

    </div>

  </div>

  <div className="bg-white rounded-xl shadow p-6">

    <h2 className="text-xl font-semibold mb-4">
      Quick Summary
    </h2>

    <p>
      Success Rate:
      {" "}
      <span className="font-bold">
        {overview.success_rate}%
      </span>
    </p>

    <p className="mt-2">
      Total Executions:
      {" "}
      <span className="font-bold">
        {overview.workflow_runs}
      </span>
    </p>

  </div>

</div>

      </div>

    </div>
  );
}

export default Dashboard;