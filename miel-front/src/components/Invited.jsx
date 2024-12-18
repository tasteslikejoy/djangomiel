import React, { Component } from "react";
import FilterSortPanel from './FilterSortPanel';
import UserCard from './UserCard';
import "./Invited.css";

class Invited extends Component{
    render() {
        return(
        <section className="content">
            <FilterSortPanel />
            <div className="cards">
            </div>
        </section>
        )
    }
}


export default Invited  ;