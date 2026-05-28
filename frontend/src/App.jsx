import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Workflows from "./pages/Workflows";
import Logs from "./pages/Logs";
import Integrations from "./pages/Integrations";
import CreateWorkflow from "./pages/CreateWorkflow";


function App() {

  return (

    <BrowserRouter>

      <div className="flex min-h-screen">

        {/* SIDEBAR */}

        <div className="w-64 bg-gray-900 text-white p-6">

          <h1 className="text-2xl font-bold mb-8">
            AI Automation
          </h1>

          <div className="space-y-4">

            <Link
              to="/"
              className="block hover:text-blue-400"
            >
              Dashboard
            </Link>

              <Link
              to="/create-workflow"
              className="block hover:text-blue-400 transition"
            >
              Create Workflow
            </Link>

            <Link
              to="/workflows"
              className="block hover:text-blue-400"
            >
              Workflows
            </Link>

            <Link
              to="/logs"
              className="block hover:text-blue-400"
            >
              Logs
            </Link>

            <Link
              to="/integrations"
              className="block hover:text-blue-400"
            >
              Integrations
            </Link>

          </div>

        </div>

        {/* MAIN CONTENT */}

        <div className="flex-1 bg-gray-100 min-h-screen">

          <Routes>

            <Route
              path="/"
              element={<Dashboard />}
            />
              <Route
              path="/create-workflow"
              element={<CreateWorkflow />}
/>
            <Route
              path="/workflows"
              element={<Workflows />}
            />

            <Route
              path="/logs"
              element={<Logs />}
            />

            <Route
              path="/integrations"
              element={<Integrations />}
            />

          </Routes>

        </div>

      </div>

    </BrowserRouter>

  );
}

export default App;