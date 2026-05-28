import { useState } from "react";
import API from "../services/api";

function CreateWorkflow() {

  const [formData, setFormData] = useState({
    name: "",
    description: "",
    workflow_json: ""
  });

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      const payload = {

        name: formData.name,

        description: formData.description,

        workflow_json: {
          workflow_type: formData.workflow_json
        }
      };

      await API.post(
        "/workflows/",
        payload
      );

      alert("Workflow created successfully");

      setFormData({
        name: "",
        description: "",
        workflow_json: ""
      });

    } catch (error) {

      console.log(error);

      alert("Failed to create workflow");
    }
  };

  return (

    <div className="p-6">

      <h1 className="text-3xl font-bold mb-6">
        Create Workflow
      </h1>

      <form
        onSubmit={handleSubmit}
        className="bg-white rounded-xl shadow p-6 max-w-2xl"
      >

        {/* Name */}

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
            placeholder="Lead Capture Workflow"
            required
          />

        </div>

        {/* Description */}

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
          />

        </div>

        {/* Workflow Type */}

        <div className="mb-6">

          <label className="block mb-2 font-medium">
            Workflow Type
          </label>

          <select
            name="workflow_json"
            value={formData.workflow_json}
            onChange={handleChange}
            className="w-full border rounded p-3"
            required
          >

            <option value="">
              Select Workflow
            </option>

            <option value="lead_capture">
              Lead Capture
            </option>

            <option value="email_automation">
              Email Automation
            </option>

            <option value="notification_workflow">
              Notification Workflow
            </option>

          </select>

        </div>

        {/* Submit */}

        <button
          type="submit"
          className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded transition"
        >
          Save Workflow
        </button>

      </form>

    </div>

  );
}

export default CreateWorkflow;