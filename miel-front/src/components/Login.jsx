// import React, { Component } from "react";
// import "./Login.css";

// class Login extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       email: "",
//       password: "",
//     };
//   }

//   handleChange = (event) => {
//     const { name, value } = event.target;
//     this.setState({ [name]: value });
//   };

//   handleSubmit = (event) => {
//     event.preventDefault();
//     console.log("Email:", this.state.email);
//     console.log("Password:", this.state.password);
//   };

//   render() {
//     return (
//       <div className="login">
//         <div className="login__logo">
//             <img src="./src/assets/logo.mp4" alt="Изображение логотипа Миэль" />
//         </div>
//         <h1 className="login__title">Витрина кандидатов</h1>
//         <form className="login__form" onSubmit={this.handleSubmit}>
//           <label className="login__label">
//             Аккаунт</label>
//             <input
//               type="email"
//               name="email"
//               value={this.state.email}
//               onChange={this.handleChange}
//               placeholder="Электронная почта"
//               className="login__input"
//             />
          
//           <label className="login__label">
//             Пароль</label>
//             <input
//               type="password"
//               name="password"
//               value={this.state.password}
//               onChange={this.handleChange}
//               placeholder="Введите пароль"
//               className="login__input"
//             />
//           <a href="#" className="login__forgot">
//             Забыли пароль?
//           </a>
//           <button type="submit" className="login__button">
//             Вход
//           </button>
//         </form>
//       </div>
//     );
//   }
// }

// export default Login;

import React, { Component } from "react";
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

  handleSubmit = (event) => {
    event.preventDefault();
    const { email, password } = this.state;
    this.props.onLogin(email, password);
  };

  render() {
    return (
      <div className="login">
        <div className="login__logo">
          <img src="./src/assets/logo.gif" alt="Изображение логотипа Миэль" />
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
