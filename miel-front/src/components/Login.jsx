import React, { Component, useContext } from "react";
import AuthContext from '../context/AuthContext'
import "./Login.css";

const Login = () => {
    let {loginUser} = useContext(AuthContext)
    return (
      <div className="login">
        <div className="login__logo">
          <img src="/src/assets/logo.gif" alt="Изображение логотипа Миэль" />
        </div>
        <h1 className="login__title">Витрина кандидатов</h1>
        <form className="login__form" onSubmit={loginUser}>
          <label className="login__label">Аккаунт</label>
          <input
            type="email"
            name="email"
            placeholder="Электронная почта"
            className="login__input"
          />
          <label className="login__label">Пароль</label>
          <input
            type="password"
            name="password"
            placeholder="Введите пароль"
            className="login__input"
          />
          <a href="#" className="login__forgot">
            Забыли пароль?
          </a>
          <button type="submit" className="login__button">
            Вход
          </button>
        </form>
      </div>
    )
}

export default Login;