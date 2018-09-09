import {Component} from "react";
import React from "react";
import style from "./news.css";

function Entry({id, title, summary, visual}) {
    return <div id={id} className={style["row"]}>
        <img className={style["entry_visual"]}
             src={visual}/>
        <div className={style["entry_content"]}>
            <div className={style["entry_title"]}>
                {title}
            </div>
            <div className={style["entry_summary"]}>
                {summary}
            </div>
        </div>
    </div>;
}

function Entries({entries}) {
    return entries.map(function (entry, i) {
        return <Entry id={"entry_" + i}
                      title={entry.title}
                      summary={entry.summary}
                      visual={entry.visual}/>
    });
}

class News extends Component {
    render() {
        return <div>
            <Entries entries={this.props.entries}/>
        </div>
    }
}

News.defaultProps = {
    entries: [
        {
            title: "Study: Nike online sales surge 31 percent days after Colin Kaepernick ad released",
            summary: "Research conducted by Edison Trends revealed that Nike's online sales surged 31 percent Sunday through Tuesday, after Colin Kaepernick ad was out.",
            visual: "https://lh3.googleusercontent.com/MoTnyWgGPdu-Bg-uu5dD2lwjGb5M3IZa9uDyvf-fnj_V5_c6gWZmA3viYT04SpZZE7vfLHX2RNob6mMPODiTGqlh8g=s163"
        }
    ]
}

export default News;