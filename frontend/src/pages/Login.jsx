import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: ""
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

      // FORM DATA REQUIRED FOR OAuth2PasswordRequestForm

      const body = new URLSearchParams();

      body.append("username", formData.email);
      body.append("password", formData.password);

      const response = await fetch(
        "http://127.0.0.1:8000/auth/login",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/x-www-form-urlencoded"
          },
          body
        }
      );

      const data = await response.json();

      console.log(data);

      if (!response.ok) {

        alert(data.detail || "Login failed");
        return;
      }

      // STORE TOKEN

      localStorage.setItem(
        "token",
        data.access_token
      );

      // FETCH USER DETAILS

      const meResponse = await fetch(
        "http://127.0.0.1:8000/auth/me",
        {
          headers: {
            Authorization:
              `Bearer ${data.access_token}`
          }
        }
      );

      const meData = await meResponse.json();

      console.log(meData);

      // STORE WORKSPACE DATA

      localStorage.setItem(
        "workspace_id",
        meData.workspace_id
      );

      localStorage.setItem(
        "workspace_email",
        meData.email
      );

      // REDIRECT

      navigate("/");

    } catch (error) {

      console.error(error);

      alert("Server error");

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="min-h-screen flex items-center justify-center bg-linear-to-br from-blue-100 via-white to-purple-100">

      <div className="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-md">

        <h1 className="text-3xl font-bold mb-6 text-center">
          AI Automation Login
        </h1>

        <form onSubmit={handleSubmit}>

          {/* EMAIL */}

          <div className="mb-4">

            <label className="block mb-2 font-medium">
              Email
            </label>

            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="w-full border rounded p-3"
              placeholder="user1@gmail.com"
              required
            />

          </div>

          {/* PASSWORD */}

          <div className="mb-6">

            <label className="block mb-2 font-medium">
              Password
            </label>

            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="w-full border rounded p-3"
              placeholder="Enter password"
              required
            />

          </div>

          {/* BUTTON */}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded transition"
          >
            {loading ? "Logging in..." : "Login"}
          </button>

        </form>

      </div>

    </div>

  );
}

export default Login;