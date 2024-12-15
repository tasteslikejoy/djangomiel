import React, { Component } from 'react';
import './UserCard.css';

class UserCard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      visibleCount: 3,
      allCoursesVisible: false,
      userData: {
        name: 'Иванов Иван',
        age: 42,
        city: 'Москва',
        resumeLink: 'https://example.com/resume',
        tags: [
          'Личный авто',
          'Коммуникабельность',
          'Английский язык',
          'Навыки',
          'Самопрезентация',
          'Собранность',
          'Обучаемость',
          'Неконфликтность',
        ],
        objectsCount: 3,
        clientsCount: 1,
        creationDate: '20.05.2024',
        invitations: 4,
        courses: [
          { name: 'Базовый-стажер', progress: 50 },
          { name: 'Документооборот', progress: 100 },
          { name: 'Юриспруденция', progress: 70 },
          { name: 'Менеджмент', progress: 60 },
          { name: 'Финансовый учет', progress: 80 },
          { name: 'Проектирование', progress: 40 },
          { name: 'Кадровое дело', progress: 90 },
          { name: 'Экономика', progress: 75 },
          { name: 'Маркетинг', progress: 85 },
        ],
      },
    };
  }

  handleShowMore = () => {
    const { visibleCount, userData } = this.state;
    const totalCourses = userData.courses.length;

    if (visibleCount + 3 >= totalCourses) {
      this.setState({
        visibleCount: totalCourses,
        allCoursesVisible: true,
      });
    } else {
      this.setState((prevState) => ({
        visibleCount: prevState.visibleCount + 3,
      }));
    }
  };

  handleHideCourses = () => {
    this.setState({
      visibleCount: 3,
      allCoursesVisible: false,
    });
  };

  render() {
    const { userData, visibleCount, allCoursesVisible } = this.state;
    const { name, age, city, resumeLink, tags, courses, invitations, objectsCount, clientsCount, creationDate } = userData;

    return (
      <div className="user-card">
        <div className="user-info">
          <div className="user-header">
            <h2><strong>{name}</strong></h2>
            <span>{age} года г. {city}</span>
          </div>
          <div className="user-about">
            <span>{invitations} приглашения</span>
            <a href={resumeLink} className="resume-link" target="_blank">Ссылка на резюме</a>
          </div>
        </div>

        <div className="tags">
          {tags.map((tag, index) => (
            <span key={index} className="tag">{tag}</span>
          ))}
        </div>

        <div className="stats">
          <div>Объекты: <span className="stat-number">{objectsCount}</span></div>
          <div>Клиенты: <span className="stat-number">{clientsCount}</span></div>
        </div>

        <div className="courses">
          {courses.slice(0, visibleCount).map((course, index) => (
            <div key={index} className="course">
              <span className="course-name">курс "{course.name}"</span>
              <div className="progress-bar">
                <div
                  className="progress-fill"
                  style={{ width: `${course.progress}%` }}
                ></div>
              </div>
            </div>
          ))}
        </div>

        <div className="show-more">
          {!allCoursesVisible ? (
            <button onClick={this.handleShowMore} className="show-more-button">
              Еще 3 курса 
              <img className="filter__arrow" src="../src/assets/arrow.svg" alt="Раскрыть список"/>
            </button>
          ) : (
            <button onClick={this.handleHideCourses} className="show-more-button">
              Скрыть курсы
              <img className="filter__arrow" src="../src/assets/arrow.svg" alt="Раскрыть список"/>
            </button>
          )}
        </div>

        <div className="buttons">
          <button className="favorites-button">В избранное</button>
          <button className="invite-button">Пригласить</button>
        </div>

        <div className="footer">Создан {creationDate}</div>
      </div>
    );
  }
}

export default UserCard;

