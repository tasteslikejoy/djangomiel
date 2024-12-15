// import React, { Component } from "react";
// import "./Header.css";

// class Header extends Component{
//     constructor(props){
//         super(props);
//         this.state = {
//             user: { name: "Иван Иванов", office: "№12" },
//             quotas: { used: 12, total: 12 },
//             currentMonth: new Date().toLocaleString("ru-RU", { month: "long" }),
//         };
//     }

//     handleLogout = () => {
//         console.log("Выход из системы");
//       };
    
//     render() {
//         const { user, quotas, currentMonth } = this.state;
    
//         return (
//           <header className="header">
//             <div className="header__logo">
//               <img src="./src/assets/logo-image.svg" alt="Изображение логотипа Миэль" />
//               <img src="./src/assets/logo-text.svg" alt="Текст логотипа Миэль" />
//             </div>

//             <div className="header__quotas">
//               <p className="header__quota-title">Квоты:
//                 <span className="header__quota-month">{currentMonth}</span>
//               </p>
//               <p className="header__quota-number">
//                 <strong className="header__quota-used">{quotas.used}</strong>
//                 <span className="header__quota-total">/{quotas.total}</span>
//               </p>
//             </div>

//             <div className="header__search">
//               <input type="text" placeholder="Поиск" />
//               <img src="./src/assets/search.svg" alt="Поиск" />
//             </div>
    
    
//             <div className="header__actions">
//               <button className="header__notifications">
//                 <img src="./src/assets/notifications.svg" alt="Уведомления" />
//               </button>
//               <button className="header__chat">Связь с админом</button>

//             </div>
    
//             <div className="header__user">
//               <p>Офис {user.office}<br /><span>{user.name}</span></p>
//             </div>

//             <div className="header__button">
//               <button className="header__logout" onClick={this.handleLogout}>
//                 Выйти
//               </button>
//             </div>
//           </header>
//         );
//     }
// }


// export default Header;

import React from "react";
import "./Header.css";

function Header({ userData, onLogout }) {
  const { first_name, last_name, office, quotas } = userData;
  const currentMonth = new Date().toLocaleString("ru-RU", { month: "long" });

  return (
    <header className="header">
      <div className="header__logo">
        <img src="./src/assets/logo-image.svg" alt="Изображение логотипа Миэль" />
        <img src="./src/assets/logo-text.svg" alt="Текст логотипа Миэль" />
      </div>

      <div className="header__quotas">
        <p className="header__quota-title">
          Квоты: <span className="header__quota-month">{currentMonth}</span>
        </p>
        <p className="header__quota-number">
          <strong className="header__quota-used">{quotas.used}</strong>
          <span className="header__quota-total">/{quotas.total}</span>
        </p>
      </div>

      <div className="header__search">
        <input type="text" placeholder="Поиск" />
        <img src="./src/assets/search.svg" alt="Поиск" />
      </div>

      <div className="header__actions">
        <button className="header__notifications">
          <img src="./src/assets/notifications.svg" alt="Уведомления" />
        </button>
        <button className="header__chat">Связь с админом</button>
      </div>

      <div className="header__user">
        <p>
          Офис {office}
          <br />
          <span>{first_name} {last_name}</span>
        </p>
      </div>

      <div className="header__button">
        <button className="header__logout" onClick={onLogout}>
          Выйти
        </button>
      </div>
    </header>
  );
}

export default Header;
