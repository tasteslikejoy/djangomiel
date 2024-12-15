import React, { Component } from "react";
import "./FilterSortPanel.css";

class FilterDropdown extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isOpen: false,
    };
  }

  toggleDropdown = () => {
  this.setState((prevState) => {
    const isOpen = !prevState.isOpen;
    if (isOpen) {
      document.addEventListener("click", this.handleClickOutside);
    } else {
      document.removeEventListener("click", this.handleClickOutside);
    }
    return { isOpen };
  });
};

handleClickOutside = (event) => {
  if (this.dropdownRef && !this.dropdownRef.contains(event.target)) {
    this.setState({ isOpen: false });
  }
};

render() {
  const { label, options, selectedOptions, isCheckbox } = this.props;
  const { isOpen } = this.state;

  return (
    <div ref={(ref) => { this.dropdownRef = ref; }} style={{ position: "relative", display: "inline-block" }}>
      <button className="filter__button" onClick={this.toggleDropdown}>
        {label} <img className="filter__arrow" src="../src/assets/arrow.svg" alt="Раскрыть список"/>
      </button>
      {isOpen && (
        <div className="filter__dropdown open">
          {options.map((option) => (
            <div key={option} className="filter-option">
              {isCheckbox ? (
                <label>
                  <input
                    type="checkbox"
                    checked={selectedOptions.includes(option)}
                    onChange={() =>
                      selectedOptions.includes(option)
                        ? onChange(selectedOptions.filter((item) => item !== option))
                        : onChange([...selectedOptions, option])
                    }
                  />
                  {option}
                </label>
              ) : (
                <p
                  onClick={() => this.handleOptionClick(option)}
                >
                  {option}
                </p>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

}

class FilterComponent extends Component {
  render() {
    const {
      selectedAge,
      selectedCourses,
      selectedSkills,
      selectedCities,
      onFilterChange
    } = this.props;

    return (
      <div className="filter__container">
        <button className="filter__button_apply" onClick={this.handleApplyFilters}>
          <img src="../src/assets/filter.svg" alt="Применить фильтры" />
        </button>
        <FilterDropdown
          className="filter__item"
          label="Возраст кандидата"
          options={["20-25 лет", "25-30 лет", "35-40 лет", "более 40 лет"]}
          selectedOptions={selectedAge}
          onChange={(options) => onFilterChange("selectedAge", options)}
          isCheckbox={false}
        />
        <FilterDropdown
          className="filter__item"
          label="Курсы"
          options={["Базовый", "Ипотека", "Юриспруденция", "Налогообложение"]}
          selectedOptions={selectedCourses}
          onChange={(options) => onFilterChange("selectedCourses", options)}
          isCheckbox={false}
        />
        <FilterDropdown
          className="filter__item"
          label="Навыки"
          options={["Личный авто", "Коммуникабельность", "Эмоциональная стабильность"]}
          selectedOptions={selectedSkills}
          onChange={(options) => onFilterChange("selectedSkills", options)}
          isCheckbox={false}
        />
        <FilterDropdown
          className="filter__item"
          label="Город"
          options={["Барнаул", "Екатеринбург", "Москва", "Нижний Тагил"]}
          selectedOptions={selectedCities}
          onChange={(options) => onFilterChange("selectedCities", options)}
          isCheckbox={false}
        />
      </div>
    );
  }
}

// Компонент для сортировки
class SortComponent extends Component {
  render() {
    const { selectedDate, selectedPopularity, onSortChange } = this.props;

    return (
      <div className="sort__container">
        <FilterDropdown
          className="sort__item"
          label="По дате"
          options={["Сначала новые", "Сначала старые"]}
          selectedOptions={selectedDate}
          onChange={(option) => onSortChange("selectedDate", option)}
          isCheckbox={false}
        />
        <FilterDropdown
          className="sort__item"
          label="По популярности"
          options={["Больше приглашений", "Меньше приглашений"]}
          selectedOptions={selectedPopularity}
          onChange={(option) => onSortChange("selectedPopularity", option)}
          isCheckbox={false}
        />
        <button className="sort__button_apply" onClick={this.handleSort}>
          <img src="../src/assets/sort.svg" alt="Применить сортировку" />
        </button>
      </div>
    );
  }
}

class FilterSortPanel extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedAge: [],
      selectedCourses: [],
      selectedSkills: [],
      selectedCities: [],
      selectedDate: "Сначала новые",
      selectedPopularity: "Больше приглашений",
    };
  }

  handleFilterChange = (filterName, selectedOptions) => {
    this.setState({ [filterName]: selectedOptions });
  };

  handleSortChange = (sortName, selectedOption) => {
    this.setState({ [sortName]: selectedOption });
  };

  handleApplyFilters = () => {
    console.log("Примененные фильтры:", this.state);
  };

  handleSort = () => {
    console.log("Сортировка по:", this.state.selectedDate, this.state.selectedPopularity);
  };

  render() {
    const {
      selectedAge,
      selectedCourses,
      selectedSkills,
      selectedCities,
      selectedDate,
      selectedPopularity,
    } = this.state;

    return (
      <div className="filter-sort">
        
        {/* Фильтры */}
        <FilterComponent
          selectedAge={selectedAge}
          selectedCourses={selectedCourses}
          selectedSkills={selectedSkills}
          selectedCities={selectedCities}
          onFilterChange={this.handleFilterChange}
        />
        
        {/* Сортировка */}
        <SortComponent
          selectedDate={selectedDate}
          selectedPopularity={selectedPopularity}
          onSortChange={this.handleSortChange}
        />
        
        
      </div>
    );
  }
}

export default FilterSortPanel;
