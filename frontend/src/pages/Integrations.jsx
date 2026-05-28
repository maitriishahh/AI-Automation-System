import { useEffect, useState } from "react";
import API from "../services/api";

function Integrations() {

  const [integrations, setIntegrations] = useState([]);

  useEffect(() => {
    fetchIntegrations();
  }, []);

  const fetchIntegrations = async () => {

    try {

      const response = await API.get(
        "/dashboard/integrations"
      );

      setIntegrations(response.data);

    } catch (error) {
      console.log(error);
    }
  };

  return (

    <div className="p-6">

      <h1 className="text-3xl font-bold mb-6">
        Integrations
      </h1>

      {/* IF DB HAS INTEGRATIONS */}

      {integrations.length > 0 ? (

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {integrations.map((integration) => (

            <div
              key={integration.id}
              className="bg-white rounded-xl shadow p-6"
            >

              <h2 className="text-xl font-semibold mb-2 capitalize">
                {integration.type}
              </h2>

              <p className="text-green-600 font-semibold">
                Connected
              </p>

              <p className="text-sm text-gray-500 mt-2">
                Workspace ID:
                {" "}
                {integration.workspace_id}
              </p>

            </div>

          ))}

        </div>

      ) : (

        /* DEFAULT SUPPORTED INTEGRATIONS */

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold mb-2">
              Gmail
            </h2>

            <p className="text-green-600 font-semibold">
              Supported
            </p>

          </div>

          <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold mb-2">
              Telegram
            </h2>

            <p className="text-green-600 font-semibold">
              Supported
            </p>

          </div>

          <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold mb-2">
              Google Sheets
            </h2>

            <p className="text-green-600 font-semibold">
              Supported
            </p>

          </div>

          <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold mb-2">
              Webhook
            </h2>

            <p className="text-green-600 font-semibold">
              Supported
            </p>

          </div>

        </div>

      )}

    </div>

  );
}

export default Integrations;