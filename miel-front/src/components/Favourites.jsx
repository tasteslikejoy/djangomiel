import React, { Component } from "react";
import FilterSortPanel from './FilterSortPanel';
import UserCard from './UserCard';
import "./Favourites.css";

class Favourites extends Component{
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
                <UserCard />
            </div>
        </section>
        )
    }
}


export default Favourites;