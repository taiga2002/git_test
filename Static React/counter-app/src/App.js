
import './App.css';
import { useState } from "react";
import Button from './Button';

function App() {
  const [count, setCount] = useState(0);
  const increment = () => {
    setCount(count + 1);
  }
  const decrement = () => {
    setCount(count - 1);
  }

  return (
    <div className="App">
      <h2>Count: {count}</h2>
      <Button task = {increment} title = "+"/>
      <Button task = {decrement} title = "-"/>
    </div>
  );
}

export default App;
