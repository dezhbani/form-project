import { Route, Routes, Navigate } from 'react-router-dom';
import { useState } from 'react';
import Verify from './components/Verify';
import './App.css';


//Components
import Signup from './components/Signup';

function App() {

  const [state, setState] = useState({id: "", phone:""});

  return (
    <div>
      <Routes>
        <Route path="/" element={<Navigate to="/sign-up"/>} />
        <Route path="/sign-up" element={<Signup state={state} setState={setState} />} />
        <Route path="/sign-up/verify" element={<Verify state={state}/>}/>
      </Routes>
    </div>
  );
}

export default App;
