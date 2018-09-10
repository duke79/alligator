import {Component} from "react";
import React from "react";
import style from "./news.css";

import {Query} from "react-apollo";
import gql from "graphql-tag";

function Entry({id, title, summary, visual, link}) {
    return <a href={link}>
        {/*<div id={id} className={style["row"]} onClick={() => window.location = link}>*/}
        <div id={id} className={style["row"]}>
            <img className={style["entry_visual"]}
                 src={visual[0]}/>
            <div className={style["entry_content"]}>
                <div className={style["entry_title"]}>
                    {title}
                </div>
                <div className={style["entry_summary"]}>
                    {summary}
                </div>
            </div>
        </div>
    </a>
}

const Entries = () => (
    <Query
        query={gql`
          {
          currentUser {
            feed(action: {get: {userId: 1, sortBy: [CATEGORY], sortOrder: [false], limit: 40}}) {
              title
              category
              description
              mediaContent
              link
            }
          }
        }
   `}>
        {({loading, error, data}) => {
            if (loading) return <p>Loading...</p>;
            if (error) return <p>Error :(</p>;

            return data.currentUser.feed.map(({
                                                  title,
                                                  category,
                                                  description,
                                                  mediaContent,
                                                  link
                                              }, i) => (
                <Entry id={"entry_" + i}
                       title={title}
                       summary={description}
                       visual={mediaContent}
                       link={link}/>
            ));
        }}
    </Query>
);

class News extends Component {
    render() {
        return <div>
            <Entries/>
        </div>
    }
}

export default News;