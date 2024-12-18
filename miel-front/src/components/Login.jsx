import React, { Component } from "react";
import axios from 'axios';
import "./Login.css";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      password: "",
    };
  }

  handleChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  };

  handleSubmit = async (event) => {
    event.preventDefault();
    const { email, password } = this.state;
  
    try {
      const response = await axios.post('http://localhost:3000/auth/jwt/create', {
        username: email,
        password,
      });
  
      if (response.status === 200 || response.status === 201) {
        const { access, refresh, name } = response.data;
  
        localStorage.setItem('accessToken', access);
        localStorage.setItem('refreshToken', refresh);

        this.props.onLogin(access, { name, email });
      }
    } catch (error) {
      console.error('Ошибка при входе:', error);

      this.setState({ errorMessage: 'Неверный логин или пароль' });
    }
  };

  render() {
    return (
      <div className="login">
        <div className="login__logo">
          <img src="./src/assets/logo1.gif" alt="Изображение логотипа Миэль" />
        </div>
        <h1 className="login__title">Витрина кандидатов</h1>
        <form className="login__form" onSubmit={this.handleSubmit}>
          <label className="login__label">Аккаунт</label>
          <input
            type="email"
            name="email"
            value={this.state.email}
            onChange={this.handleChange}
            placeholder="Электронная почта"
            className="login__input"
          />
          <label className="login__label">Пароль</label>
          <input
            type="password"
            name="password"
            value={this.state.password}
            onChange={this.handleChange}
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
    );
  }
}

export default Login;
