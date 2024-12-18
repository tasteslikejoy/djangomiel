import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './Header';
import Sidebar from './Sidebar';
import Candidates from './Candidates';
import Favourites from './Favourites';
import Invited from './Invited';
import './Dashboard.css';

const Dashboard = ({ onLogout }) => {
  const [userData, setUserData] = useState(null);
  const [activeComponent, setActiveComponent] = useState("Витрина кандидатов");

  useEffect(() => {
    const fetchData = async () => {
      const token = localStorage.getItem('accessToken');
      if (!token) {
        console.error('Токен отсутствует');
        return;
      }

      try {
        const response = await axios.get('http://localhost:3000/auth/jwt/create', { //??
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        setUserData(response.data);
      } catch (error) {
        console.error('Ошибка загрузки данных пользователя:', error);
        onLogout();
      }
    };

    fetchData();
  }, [onLogout]);

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

  if (!userData) {
    return <div>Загрузка данных пользователя...</div>;
  }

  return (
    <div className="app-container">
      <Header userData={userData} onLogout={onLogout} />
      <div className="main-content">
        <Sidebar onMenuClick={handleMenuClick} />
        <div className="content">{ContentComponent}</div>
      </div>
    </div>
  );
};

export default Dashboard;
