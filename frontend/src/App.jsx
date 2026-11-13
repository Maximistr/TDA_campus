import { useEffect, useState } from "react";

export default function App() {
  const [status, setStatus] = useState("checking...");
  const [team, setTeam] = useState(null);
  const [teamError, setTeamError] = useState(false);

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

    fetch(`${apiUrl}/v1/team`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Team request failed: ${response.status}`);
        }
        return response.json();
      })
      .then(setTeam)
      .catch(() => setTeamError(true));
  }, []);

  return (
    <main>
      <p>Status: {status}</p>
      {team ? (
        <footer>
          <p>Team: {team.name}</p>
          <p>Members: {team.members.join(", ")}</p>
        </footer>
      ) : (
        <p>{teamError ? "Team data unavailable" : "Loading team..."}</p>
      )}
    </main>
  );
}
