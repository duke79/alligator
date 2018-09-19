import React, {Component} from 'react';
import style from './admin.css'
import $ from 'jquery'
import ListItem from "./list_item";

class Admin extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <ul>
                    <ListItem>Element 1</ListItem>
                    <ListItem>Element 2</ListItem>
                </ul>
            </div>
        );
    }
}

export default Admin;