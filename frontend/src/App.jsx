import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";

import Sidebar from "./components/Sidebar";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import CreateWorkflow from "./pages/CreateWorkflow";
import Workflows from "./pages/Workflows";
import Logs from "./pages/Logs";
import Integrations from "./pages/Integrations";
import Leads from "./pages/Leads";


function AppLayout() {

  const location = useLocation();

  // HIDE SIDEBAR ON LOGIN PAGE

  const hideSidebar = location.pathname === "/login";

  return (

    <div className="flex">

      {!hideSidebar && <Sidebar />}

      <div className="flex-1">

        <Routes>

          <Route path="/login" element={<Login />} />

          <Route path="/" element={<Dashboard />} />

          <Route
            path="/create-workflow"
            element={<CreateWorkflow />}
          />

          <Route
            path="/workflows"
            element={<Workflows />}
          />

          <Route path="/logs" element={<Logs />} />

          <Route
            path="/integrations"
            element={<Integrations />}
          />
          
          <Route
            path="/leads"
            element={<Leads />}
          />
        </Routes>

      </div>

    </div>
  );
}

function App() {

  return (

    <BrowserRouter>
      <AppLayout />
    </BrowserRouter>

  );
}

export default App;