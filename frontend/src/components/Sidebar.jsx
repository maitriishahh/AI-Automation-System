import {
  Link,
  useNavigate,
  useLocation
} from "react-router-dom";

function Sidebar() {

  const navigate = useNavigate();

  const location = useLocation();

  const handleLogout = () => {

    localStorage.removeItem("token");
    localStorage.removeItem("workspace_id");
    localStorage.removeItem("workspace_email");

    navigate("/login");
  };

  // ACTIVE LINK STYLE

  const activeClass = (path) => {

    return location.pathname === path

      ? "font-bold text-blue-400"

      : "text-white";
  };

  return (

    <div className="w-64 min-h-screen bg-black text-white flex flex-col justify-between p-6">

      <div>

        {/* LOGO */}

        <h1 className="text-4xl font-bold mb-12 text-center">
          AI Automation
        </h1>

        {/* MENU */}

        <div className="flex flex-col gap-6 text-lg">

          <Link
            to="/"
            className={`${activeClass("/")} hover:text-blue-400 transition`}
          >
            Dashboard
          </Link>

          <Link
            to="/create-workflow"
            className={`${activeClass("/create-workflow")} hover:text-blue-400 transition`}
          >
            Create Workflow
          </Link>

          <Link
            to="/workflows"
            className={`${activeClass("/workflows")} hover:text-blue-400 transition`}
          >
            Workflows
          </Link>

          <Link
            to="/logs"
            className={`${activeClass("/logs")} hover:text-blue-400 transition`}
          >
            Logs
          </Link>

          <Link
            to="/integrations"
            className={`${activeClass("/integrations")} hover:text-blue-400 transition`}
          >
            Integrations
          </Link>

          <Link
            to="/leads"
            className={`${activeClass("/leads")} hover:text-blue-400 transition`}
          >
            Leads CRM
          </Link>

        </div>

      </div>

      {/* FOOTER */}

      <div>

        <p className="mb-4 text-sm text-gray-400">
          {
            localStorage.getItem(
              "workspace_email"
            )
          }
        </p>

        <button
          onClick={handleLogout}
          className="w-full bg-red-600 hover:bg-red-700 py-2 rounded"
        >
          Logout
        </button>

      </div>

    </div>

  );
}

export default Sidebar;