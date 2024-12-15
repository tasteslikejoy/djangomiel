import React, { Component } from "react";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
} from "chart.js";

import { Pie, Bar } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement);

import "./Dashboard.css";

class Card extends Component {
  render() {
    const { number, text } = this.props;
    return (
      <div className="card">
        <p className="card__number">{number}</p>
        <p className="card__text">{text}</p>
      </div>
    );
  }
}

class CandidateStatistics extends Component {
  render() {
    return (
      <div className="statistics__card">
        <h3>Статистика кандидатов</h3>
        <div className="statistics__number">47</div>
        <p>Всего кандидатов</p>
        <div className="statistics__details">
          <div className="statistics__numbers">
            <span className="number green">30</span>
            <span className="number gray">8</span>
            <span className="number red">9</span>
          </div>
          <div className="statistics__bar">
            <span className="dot green"></span>
            <span className="dot gray"></span>
            <span className="dot red"></span>
          </div>
          <div className="statistics__labels">
            <span className="label green">Трудоустроились</span>
            <span className="label gray">На рассмотрении</span>
            <span className="label red">Отказ</span>
          </div>
      </div>
    </div>
    );
  }
}

class InvitationStatistics extends Component {
  render() {
    const data = {
      labels: ["Принято", "Текущие запросы", "Отклонено"],
      datasets: [
        {
          data: [46, 30, 24],
          backgroundColor: ["#76c7c0", "#cccccc", "#e15b64"],
        },
      ],
    };

    return (
      <div className="statistics__card">
        <h3>Статистика по приглашениям</h3>
        <div className="chart__container">
          <Pie data={data} />
        </div>
        <p>Всего: 90</p>
      </div>
    );
  }
}

class AgentStatistics extends Component {
  render() {
    const data = {
      labels: ["2", "4", "8", "12", "16", "18", "22", "24"],
      datasets: [
        {
          label: "Прирост сотрудников за сутки",
          data: [2, 1, 4, 6, 8, 5, 3, 4],
          backgroundColor: "#e15b64",
        },
      ],
    };

    const options = {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    };

    return (
      <div className="statistics__card">
        <h3>Статистика количества агентов</h3>
        <div className="chart__container">
          <Bar data={data} options={options} />
        </div>
      </div>
    );
  }
}

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeFilter: "День",
    };
  }

  handleFilterClick = (filter) => {
    this.setState({ activeFilter: filter });
  };

  render() {
    const { activeFilter } = this.state;

    return (
      <div className="dashboard">
        <p className="news">Новости</p>
        <section className="cards">
          <div className="cards__container">
            <Card number="10" text={<>новых<br />приглашений</>} />
            <Card number="5" text={<>запросов на<br />создание<br />карточек</>} />
            <Card number="1" text={<>запрос на<br />начисление<br />квот</>} />
          </div>
          <div className="cards__container">
            <Card number="347" text={<>кандидатов в<br />базе</>} />
            <Card number="200" text={<>количество<br />офисов</>} />
          </div>
        </section>

        <section className="filters">
          {["День", "Неделя", "Месяц", "Квартал", "Год"].map((filter) => (
            <button
              key={filter}
              className={activeFilter === filter ? "active" : ""}
              onClick={() => this.handleFilterClick(filter)}
            >
              {filter}
            </button>
          ))}
        </section>

        <section className="statistics">
          <CandidateStatistics />
          <InvitationStatistics />
          <AgentStatistics />
        </section>

        <section className="invitation-stats">
          <p>Статистика приглашений по офисам</p>
          <div className="invitation-stats__search">
              <input type="text" placeholder="Поиск" />
              <img src="./src/assets/search.svg" alt="Поиск" />
            </div>
        </section>
      </div>
    );
  }
}

export default Dashboard;
