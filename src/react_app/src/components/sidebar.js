import {Component} from "react";
import React from "react";
import style from "./sidebar.css";
import classNames from 'classnames';

function Row({name, label, isFontBold, isSelected}) {
    let label_style = {};
    if (isFontBold)
        label_style = {"font-weight": "bold"};

    var row_classes = classNames({
        [style["row"]]: true,
        [style["row_selected"]]: isSelected
    });

    return <div id={name} className={row_classes}>
        <div id={name + "_header"} className={style["row_header"]}>
            <div id={name + "_label"} style={label_style}>
                {label}
            </div>
        </div>
    </div>;
}

function Separator({label}) {
    return <div className={style["separator"]}>
        <div className={style["separator_label"]}>
            {label}
        </div>
    </div>;
}

class Sidebar extends Component {
    render() {
        return <div>
            <div className={style["sidebar"]}>
                <div style={{"height": "26px"}}/>
                <Row name="mytab"
                     label="Today"
                     isFontBold="true"
                     isSelected="true"/>
                <Row name="savedtab"
                     label="Read Later"
                     isFontBold="true"/>
                <Row name="filtertab"
                     label="Filters"
                     isFontBold="true"/>

                <Separator label="FEEDS"/>
                <Row name="all"
                     label="All"
                     isFontBold="true"/>
                <Row name="news"
                     label="News"
                     isFontBold="true"/>

                <Separator label="BOARDS"/>
                <div style={{"height": "26px"}}/>
                <Row name="integrations"
                     label="Integrations"
                     isFontBold="true"/>
                <Row name="share_collections"
                     label="Share Collections"
                     isFontBold="true"/>
                <Row name="support"
                     label="Support"
                     isFontBold="true"/>
            </div>
            <div className={style["bottom"]}>
                ADD CONTENT
            </div>
        </div>;
    }
}


export default Sidebar;