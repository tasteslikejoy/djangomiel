import React, { Component } from "react";
import "./Header.css";

class Header extends Component{
    constructor(props){
        super(props);
        this.state = {
            user: { name: "Иван Иванов", office: "№12" },
            currentMonth: new Date().toLocaleString("ru-RU", { month: "long" }),
        };
    }

    handleLogout = () => {
        console.log("Выход из системы");
      };
    
    render() {
        const { user, quotas, currentMonth } = this.state;
    
        return (
          <header className="header">
            <div className="header__logo">
              <img src="./src/assets/logo-image.svg" alt="Изображение логотипа Миэль" />
              <img src="./src/assets/logo-text.svg" alt="Текст логотипа Миэль" />
            </div>

            <div className="header__search">
              <input type="text" placeholder="Поиск" />
              <img src="./src/assets/search.svg" alt="Поиск" />
            </div>

            <div className="header__user">
              <p>{user.name}</p>
            </div>

            <div className="header__button">
              <button className="header__logout" onClick={this.handleLogout}>
                Выйти
              </button>
            </div>
          </header>
        );
    }
}


export default Header;