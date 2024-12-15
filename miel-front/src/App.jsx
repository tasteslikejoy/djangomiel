// import {useState, useEffect} from 'react'
// import axios from 'axios'
// import Header from './components/Header'
// import Sidebar from './components/Sidebar'

// import FilterSortPanel from './components/FilterSortPanel'
// import Login from './components/Login'
// import './App.css'
// import React from 'react'
// import UserCard from './components/UserCard'


// function App() {
//   return (
//     <div className="app-container">
//       <Header />
//       <div className="main-content">
//         <Sidebar />
//         <section className="content">
//           <FilterSortPanel />
//           <div className="cards">
//             <UserCard />
//             <UserCard />
//             <UserCard />
//             <UserCard />
//             <UserCard />
//             <UserCard />
//             <UserCard />
//             <UserCard />
//             <UserCard />
//           </div>
//         </section>
        
//       </div>
//       {/* <Login /> */}
//     </div>
//   );
// }

// export default App


import { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import FilterSortPanel from './components/FilterSortPanel';
import Login from './components/Login';
import './App.css';
import React from 'react';
import UserCard from './components/UserCard';


function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      setIsLoggedIn(true);
      //загрузка данных пользователя
    }
  }, []);

  const handleLogin = async (email, password) => {
    try {
      const response = await axios.post('http://localhost:8000/auth/jwt/create', {
        username: email,
        password: password,
      });
      if (response.status === 201) {
        localStorage.setItem('accessToken', response.data.access);
        localStorage.setItem('refreshToken', response.data.refresh);
        setIsLoggedIn(true);
        setUserData({ name: response.data.name, email });
      }
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    setIsLoggedIn(false);
    setUserData(null);
  };

  return (
    <div className="app-container">
      {isLoggedIn ? (
        <>
          <Header userData={userData} onLogout={handleLogout} />
          <div className="main-content">
            <Sidebar />
            <section className="content">
              <FilterSortPanel />
              <div className="cards">
                {Array.from({ length: 9 }).map((_, index) => (
                  <UserCard key={index} />
                ))}
              </div>
            </section>
          </div>
        </>
      ) : (
        <Login onLogin={handleLogin} />
      )}
    </div>
  );
}

export default App;
