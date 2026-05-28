import { useState } from "react";

function CreateWorkflow() {

  const [formData, setFormData] = useState({
    name: "",
    description: "",
    workflow_type: "gmail",
    recipient_email: ""
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      setLoading(true);

      const token = localStorage.getItem("token");

      // BACKEND PAYLOAD

      const payload = {

        name: formData.name,

        description: formData.description,

        workflow_json: {

  nodes: [

  // TRIGGER NODE

  {
    id: 1,

    type: "trigger",

    service: "gmail"
  },

  // ACTION NODE

  {
    id: 2,

    type: "action",

    service: "gmail",

    config: {

      recipient_email:
        formData.recipient_email
    }
  }

]
}
      };

      console.log(payload);

      const response = await fetch(
        "http://127.0.0.1:8000/workflows/",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",

            Authorization: `Bearer ${token}`
          },

          body: JSON.stringify(payload)
        }
      );

      const data = await response.json();

      console.log(data);
      if (!response.ok) {

        alert(data.detail || "Workflow creation failed");

        return;
      }

      alert("Workflow created successfully");

      // RESET FORM

      setFormData({
        name: "",
        description: "",
        workflow_type: "email_automation",
        recipient_email: ""
      });

    } catch (error) {

      console.error(error);

      alert("Server error");

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="p-8">

      <div className="max-w-2xl bg-white shadow-xl rounded-2xl p-8">

        <h1 className="text-3xl font-bold mb-6">
          Create Workflow
        </h1>

        <form onSubmit={handleSubmit}>

  {/* WORKFLOW TYPE */}

  <div className="mb-4">

    <label className="block mb-2 font-medium">
      Workflow Type
    </label>

    <select
      name="workflow_type"
      value={formData.workflow_type}
      onChange={handleChange}
      className="w-full border rounded p-3"
    >

      <option value="gmail">
        Email Automation
      </option>

      <option value="telegram">
        Telegram Automation
      </option>

    </select>

  </div>

  {/* WORKFLOW NAME */}

  <div className="mb-4">

    <label className="block mb-2 font-medium">
      Workflow Name
    </label>

    <input
      type="text"
      name="name"
      value={formData.name}
      onChange={handleChange}
      className="w-full border rounded p-3"
      placeholder="Gmail Automation"
      required
    />

  </div>

  {/* DESCRIPTION */}

  <div className="mb-4">

    <label className="block mb-2 font-medium">
      Description
    </label>

    <textarea
      name="description"
      value={formData.description}
      onChange={handleChange}
      className="w-full border rounded p-3"
      placeholder="Workflow description"
      rows="4"
    />

  </div>

  {/* RECIPIENT EMAIL */}

  <div className="mb-6">

    <label className="block mb-2 font-medium">
      Recipient Email
    </label>

    <input
      type="email"
      name="recipient_email"
      value={formData.recipient_email}
      onChange={handleChange}
      className="w-full border rounded p-3"
      placeholder="client@gmail.com"
      required
    />

  </div>

  {/* BUTTON */}

  <button
    type="submit"
    disabled={loading}
    className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded"
  >
    {
      loading
        ? "Creating..."
        : "Create Workflow"
    }
  </button>

</form>

      </div>

    </div>

  );
}

export default CreateWorkflow;