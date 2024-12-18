import React, { Component } from "react";
import "./Header.css";


class Header extends Component {
  render() {
    const { userData } = this.props;

    if (!userData) {
      return null;
    }

    const { name, office, quotas } = userData;
    const currentMonth = new Date().toLocaleString("ru-RU", { month: "long" });

    return (
      <header className="header">
        <div className="header__logo">
          <img src="./src/assets/logo-image.svg" alt="Изображение логотипа Миэль" />
          <img src="./src/assets/logo-text.svg" alt="Текст логотипа Миэль" />
        </div>

        <div className="header__quotas">
          <p className="header__quota-title">Квоты:
            <span className="header__quota-month">{currentMonth}</span>
          </p>
          <p className="header__quota-number">
            <strong className="header__quota-used">{quotas.used}</strong>
            <span className="header__quota-total">/{quotas.total}</span>
          </p>
        </div>

        <div className="header__user">
          <p>Офис {office}<br /><span>{name}</span></p>
        </div>

        <div className="header__button">
          <button className="header__logout" onClick={this.props.onLogout}>
            Выйти
          </button>
        </div>
      </header>
    );
  }
}

export default Header;