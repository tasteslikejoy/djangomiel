import React, { Component } from "react";
import "./Sidebar.css";

class Sidebar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: "Витрина кандидатов",
    };
  }

  handleItemClick = (item) => {
    this.setState({ activeItem: item });
  };

  render() {
    const { activeItem } = this.state;

    const menuItems = [
      "Главная",
      "Витрина кандидатов",
      "Новые приглашения",
      "Архив кандидатов",
      "Офисы",
    ];

    return (
      <aside className="sidebar">
        {menuItems.map((item) => (
          <div
            key={item}
            className={`sidebar__item ${
              activeItem === item ? "sidebar__item--active" : ""
            }`}
            onClick={() => this.handleItemClick(item)}
          >
            {item}
          </div>
        ))}
        <button className="sidebar__button">
          <img src="./src/assets/plus.svg" alt="Добавить кандидата" />
          Добавить кандидата</button>
      </aside>
    );
  }
}

export default Sidebar;
