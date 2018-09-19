import React, {Component} from 'react';
import style from "./list_item.css";
import $ from "jquery";
import classNames from "classnames";

class ListItem extends Component {
    state = {
        checked: true
    };

    componentDidMount() {
        // const selector_list_item = "." + style["list_item"];
        // $(selector_list_item).click(function () {
        //     console.log("clicked");
        //     $(this).toggleClass(style["list_item_checked"]);
        // });
    }

    render() {
        var classes = classNames({
            [style["list_item"]]: true,
            [style["list_item_checked"]]: this.state.checked
        });

        return (
            <li className={classes}
                onClick={((e) => this.toggleCheck(e))}>
                {this.props.children}
            </li>
        );
    }

    toggleCheck(e) {
        // $(e.currentTarget).toggleClass(style["list_item_checked"]);
        if (this.state.checked === true) {
            this.setState({checked: false})
        }
        else {
            this.setState({checked: true})
        }
    }
}

export default ListItem;