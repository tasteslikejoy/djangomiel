import React, { useState, useEffect, useContext } from 'react';
import AuthContext from '../context/AuthContext';
import Header from './Header';
import Sidebar from './Sidebar';
import Candidates from './Candidates';
import Favourites from './Favourites';
import Invited from './Invited';
import './Dashboard.css';

const Dashboard = () => {
  const { authTokens, logoutUser } = useContext(AuthContext);
  let [user, setProfile] = useState([])

  useEffect(() => {
      getProfile()
  },[])

  const handleMenuClick = (component) => {
    setActiveComponent(component);
  };

  let ContentComponent;
  switch (activeComponent) {
    case "Витрина кандидатов":
      ContentComponent = <Candidates />;
      break;
    case "Избранные":
      ContentComponent = <Favourites />;
      break;
    case "Приглашенные кандидаты":
      ContentComponent = <Invited />;
      break;
    default:
      ContentComponent = <Candidates />;
  }

  const getProfile = async() => {
      let response = await fetch('localhost:3000/auth/users', {
      method: 'GET',
      headers:{
          'Content-Type': 'application/json',
          'Authorization':'Bearer ' + String(authTokens.access)
      }
      })
      let data = await response.json()
      console.log(data)
      if(response.status === 200){
          setProfile(data)
      } else if(response.statusText === 'Unauthorized'){
          logoutUser()
      }
  }

  return (
  <div className="app-container">
    <Header  />
    <div className="main-content">
      <Sidebar onMenuClick={handleMenuClick} />
      <div className="content">{ContentComponent}</div>
    </div>
  </div>
  )
}

export default Dashboard;