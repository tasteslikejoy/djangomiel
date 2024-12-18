import React, { Component } from 'react';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import './App.css';

class App extends Component {
  state = {
    isLoggedIn: false,
    token: null,
    userData: null,
  };
  

  handleLogin = (token, userData) => {
    this.setState({
      isLoggedIn: true,
      token,
      userData,
    });
  };

  handleLogout = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    this.setState({ isLoggedIn: false, token: null, userData: null });
  };
  
  render() {
    const { isLoggedIn, userData } = this.state;

    return (
      <div>
        {isLoggedIn ? (
          <Dashboard onLogout={this.handleLogout} userData={userData} />
        ) : (
          <div className="login-container">
            <Login onLogin={this.handleLogin} />
          </div>  
        )}
      </div>
    );
  }
}

export default App;