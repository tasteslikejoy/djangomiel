import React, { useContext, useState } from "react";
import { Link } from "react-router-dom";
import AuthContext from "../context/AuthContext";
import "./Header.css";

const Header = () => {
    let { user, logoutUser } = useContext(AuthContext)

    const [quotas, setQuotas] = useState({ used: 12, total: 12 });
    const currentMonth = new Date().toLocaleString("ru-RU", { month: "long" });

    const handleLogout = () => {
        logoutUser();
        console.log("Выход из системы");
    };

    return (
        <header className="header">
            <div className="header__logo">
                <img src="./src/assets/logo-image.svg" alt="Изображение логотипа Миэль" />
                <img src="./src/assets/logo-text.svg" alt="Текст логотипа Миэль" />
            </div>

            <div className="header__quotas">
                <p className="header__quota-title">
                    Квоты:
                    <span className="header__quota-month">{currentMonth}</span>
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
                    Офис {user.office}
                    <br />
                    <span>{user.username}</span>
                </p>
            </div>

            <div className="header__button">
                <button className="header__logout" onClick={logoutUser}>
                    Выйти
                </button>
            </div>
        </header>
    );
};

export default Header;