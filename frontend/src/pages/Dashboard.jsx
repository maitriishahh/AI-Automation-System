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

      const response = await API.get(
        "/dashboard/overview"
      );

      setOverview(response.data);

    } catch (error) {

      console.log(error);

    }
  };

  if (!overview) {

    return (

      <div className="p-6 text-xl font-semibold">
        Loading Dashboard...
      </div>

    );
  }

  return (

    <div className="p-6">

      {/* HEADER */}

      <div className="flex items-center justify-between mb-8">

        <div>

          <h1 className="text-4xl font-bold">
            Dashboard
          </h1>

          <p className="text-gray-500 mt-1">
            Workflow orchestration overview
          </p>

        </div>

        <div className="bg-green-100 text-green-700 px-4 py-2 rounded-full font-semibold">

          System Active

        </div>

      </div>

      {/* METRIC CARDS */}

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

      </div>

      {/* SYSTEM STATUS + SUMMARY */}

      <div className="mt-10 grid grid-cols-1 md:grid-cols-2 gap-6">

        {/* SYSTEM STATUS */}

        <div className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition duration-300">

          <h2 className="text-2xl font-bold mb-6">
            System Status
          </h2>

          <div className="space-y-4">

            <div className="flex items-center justify-between">

              <p>
                Queue Monitoring
              </p>

              <span className="bg-green-100 text-green-600 px-3 py-1 rounded-full text-sm font-semibold">
                ACTIVE
              </span>

            </div>

            <div className="flex items-center justify-between">

              <p>
                Workflow Engine
              </p>

              <span className="bg-green-100 text-green-600 px-3 py-1 rounded-full text-sm font-semibold">
                RUNNING
              </span>

            </div>

            <div className="flex items-center justify-between">

              <p>
                Integrations
              </p>

              <span className="bg-blue-100 text-blue-600 px-3 py-1 rounded-full text-sm font-semibold">
                CONNECTED
              </span>

            </div>

          </div>

        </div>

        {/* QUICK SUMMARY */}

        <div className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition duration-300">

          <h2 className="text-2xl font-bold mb-6">
            Quick Summary
          </h2>

          <div className="space-y-4">

            <div className="flex items-center justify-between">

              <p>
                Success Rate
              </p>

              <span className="font-bold text-green-600 text-lg">
                {overview.success_rate}%
              </span>

            </div>

            <div className="flex items-center justify-between">

              <p>
                Total Executions
              </p>

              <span className="font-bold text-lg">
                {overview.workflow_runs}
              </span>

            </div>

            <div className="flex items-center justify-between">

              <p>
                Pending Queue
              </p>

              <span className="font-bold text-yellow-600 text-lg">
                {overview.pending_jobs}
              </span>

            </div>

          </div>

        </div>

      </div>

      {/* RECENT ACTIVITY */}

      <div className="mt-10 bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition duration-300">

        <h2 className="text-2xl font-bold mb-6">
          Recent Activity
        </h2>

        <div className="space-y-4">

          <div className="flex items-center justify-between border-b pb-3">

            <div>

              <p className="font-semibold">
                Lead Workflow Executed
              </p>

              <p className="text-sm text-gray-500">
                Gmail automation completed successfully
              </p>

            </div>

            <span className="bg-green-100 text-green-600 px-3 py-1 rounded-full text-sm font-semibold">
              SUCCESS
            </span>

          </div>

          <div className="flex items-center justify-between border-b pb-3">

            <div>

              <p className="font-semibold">
                Telegram Alert Sent
              </p>

              <p className="text-sm text-gray-500">
                Queue worker processed notification
              </p>

            </div>

            <span className="bg-blue-100 text-blue-600 px-3 py-1 rounded-full text-sm font-semibold">
              SENT
            </span>

          </div>

          <div className="flex items-center justify-between">

            <div>

              <p className="font-semibold">
                Workflow Retry Triggered
              </p>

              <p className="text-sm text-gray-500">
                Automatic retry system activated
              </p>

            </div>

            <span className="bg-yellow-100 text-yellow-600 px-3 py-1 rounded-full text-sm font-semibold">
              RETRYING
            </span>

          </div>

        </div>

      </div>

    </div>

  );
}

export default Dashboard;