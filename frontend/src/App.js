import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/posts').then(res => {
      setPosts(res.data);
    });
  }, []);

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
