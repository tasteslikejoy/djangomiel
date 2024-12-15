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
      "Витрина кандидатов",
      "Избранные",
      "Приглашенные кандидаты",
    ];

    return (
      <div className="sidebar">
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
      </div>
    );
  }
}

export default Sidebar;
