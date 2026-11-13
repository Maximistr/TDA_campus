import { useEffect, useState } from "react";

export default function App() {
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    const apiUrl = import.meta.env.VITE_API_URL || "/api";

    fetch(`${apiUrl}/v1/health`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Health request failed: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setStatus(data.status.toUpperCase()))
      .catch(() => setStatus("UNAVAILABLE"));
  }, []);

  return <p>Status: {status}</p>;
}
