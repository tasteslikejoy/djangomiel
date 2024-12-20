import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import React, { Component } from 'react';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import { AuthProvider } from './context/AuthContext'
import PrivateRoute from './utils/PrivateRoute'
import './App.css';

class App extends Component {
  render() {
    return (
      <div>
        <Router>
            <AuthProvider>
                <Routes>
                    <Route path="/" element={<PrivateRoute><Dashboard/></PrivateRoute>} />
                    <Route path="/login" element={<div className='login-container'><Login/></div>}/>
                </Routes>
            </AuthProvider>
        </Router>
      </div>
    );
  }
}

export default App;