import React, { Component } from "react";
import FilterSortPanel from './FilterSortPanel';
import UserCard from './UserCard';
import "./Candidates.css";

class Candidates extends Component{
    render() {
        return(
        <section className="content">
            <FilterSortPanel />
            <div className="cards">
                <UserCard />
                <UserCard />
                <UserCard />
                <UserCard />
                <UserCard />
                <UserCard />
            </div>
        </section>
        )
    }
}

export default Candidates;