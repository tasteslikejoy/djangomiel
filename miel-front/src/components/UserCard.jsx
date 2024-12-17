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
          { name: 'Базовый-стажер', progress: 100, startDate: '01.01.2024', endDate: '31.12.2024', points: 80 },
          { name: 'Документооборот', progress: 100, startDate: '01.01.2023', endDate: '31.12.2023', points: 100 },
          { name: 'Юриспруденция', progress: 70, startDate: '01.03.2024', endDate: '30.09.2024', points: null },
          { name: 'Менеджмент', progress: 100, startDate: '01.02.2024', endDate: '31.08.2024', points: 95 },
          { name: 'Финансовый учет', progress: 80, startDate: '01.04.2024', endDate: '31.10.2024', points: null },
          { name: 'Проектирование', progress: 40, startDate: '01.06.2024', endDate: '31.12.2024', points: null },
          { name: 'Кадровое дело', progress: 90, startDate: '01.07.2024', endDate: '31.12.2024', points: null },
          { name: 'Экономика', progress: 75, startDate: '01.09.2024', endDate: '28.02.2025', points: null },
          { name: 'Маркетинг', progress: 85, startDate: '01.10.2024', endDate: '31.12.2025', points: null },
        ]
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
            <p>{age} года <span>г. {city}</span></p>
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
              <div className="course-header">
                <span className="course-name">
                  курс "{course.name}"
                </span>
                {course.progress === 100 && course.points !== null && (
                  <div className="course-total">
                    <img className="course-medal" src="../src/assets/medal.svg" alt="Медаль"/>
                    <span className="course-points">{course.points}/100<br />баллов</span>
                  </div>
                )}
              </div>
              <div className="progress-bar">
                <div
                  className="progress-fill"
                  style={{ width: `${course.progress}%` }}
                ></div>
              </div>
              <div className="course-dates">
                <p>{course.startDate} г.</p>
                <p>{course.endDate} г.</p>
              </div>
            </div>
          ))}
        </div>

        <div className="show-more">
          {!allCoursesVisible ? (
            <button onClick={this.handleShowMore} className="show-more-button open">
              Еще 3 курса 
              <img className="filter__arrow" src="../src/assets/arrow.svg" alt="Раскрыть список"/>
            </button>
          ) : (
            <button onClick={this.handleHideCourses} className="show-more-button close">
              Скрыть курсы
              <img className="filter__arrow" src="../src/assets/arrow.svg" alt="Скрыть список"/>
            </button>
          )}
        </div>

        <div className="buttons">
          <button className="favorites-button"><img src="../src/assets/heart.svg" alt="В избранное"/>
          {/* <button className="favorites-button"><img src="../src/assets/click.gif" alt="В избранное" width='24px' height='24px'/> */}
          В Избранное</button>
          <button className="invite-button">Пригласить</button>
        </div>

        <div className="footer">создан {creationDate}</div>
      </div>
    );
  }
}

export default UserCard;


