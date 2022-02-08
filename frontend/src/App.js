import './App.css';
import { Route, Routes, Navigate } from 'react-router-dom';

//Components
import Signup from './components/Signup';

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Navigate to="/sign-up"/>} />
        <Route path="/sign-up" element={<Signup/>} />
      </Routes>
    </div>
  );
}

export default App;
