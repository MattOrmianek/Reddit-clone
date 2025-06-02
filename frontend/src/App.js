import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [posts, setPosts] = useState([]);

  // Base URL for the backend API can be configured via REACT_APP_API_URL.
  // Default to localhost if no environment variable is provided.
  const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';

  useEffect(() => {
    axios.get(`${apiUrl}/posts`).then(res => {
      setPosts(res.data);
    });
  }, [apiUrl]);

  return (
    <div>
      <h1>Reddit Clone</h1>
      {posts.map(p => (
        <div key={p.id}>
          <h3>{p.title}</h3>
          <p>{p.content}</p>
          <small>by {p.author}</small>
        </div>
      ))}
    </div>
  );
}

export default App;
