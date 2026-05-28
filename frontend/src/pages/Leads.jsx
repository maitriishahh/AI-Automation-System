import { useState } from "react";

function Leads() {

  const [leads] = useState([

    {
      id: 1,
      name: "John Doe",
      email: "john@gmail.com",
      status: "NEW",
      conversion: "PENDING"
    },

    {
      id: 2,
      name: "Sarah Smith",
      email: "sarah@gmail.com",
      status: "CONTACTED",
      conversion: "CONVERTED"
    }

  ]);

  return (

    <div className="p-8">

      <h1 className="text-4xl font-bold mb-8">
        Leads CRM
      </h1>

      <div className="bg-white rounded-2xl shadow-xl overflow-hidden">

        <table className="w-full">

          <thead className="bg-gray-100">

            <tr>

              <th className="p-4 text-left">
                Name
              </th>

              <th className="p-4 text-left">
                Email
              </th>

              <th className="p-4 text-left">
                Status
              </th>

              <th className="p-4 text-left">
                Conversion
              </th>

            </tr>

          </thead>

          <tbody>

            {leads.map((lead) => (

              <tr
                key={lead.id}
                className="border-t"
              >

                <td className="p-4 font-medium">
                  {lead.name}
                </td>

                <td className="p-4">
                  {lead.email}
                </td>

                <td className="p-4">

                  <span className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm">

                    {lead.status}

                  </span>

                </td>

                <td className="p-4">

                  {lead.conversion ===
                  "CONVERTED" ? (

                    <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">
                      Converted
                    </span>

                  ) : (

                    <span className="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm">
                      Pending
                    </span>

                  )}

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>

  );
}

export default Leads;