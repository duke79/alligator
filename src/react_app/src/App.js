import React, {Component} from 'react';
import style from './App.css';
import Sidebar from "./components/sidebar";
import News from "./components/news"

class App extends Component {
    render() {
        return (
            <div>
                <Sidebar/>
                <div style={{"position": "absolute", "left": "240px"}}>
                    <div style={{"margin-left": "200px"}}>
                        <h1 className={style["title"]}>Today</h1>
                        <h1 className={style["sub"]}>The insights you need</h1>
                        <div style={{"height": "36px"}}/>
                        <News/>
                    </div>
                </div>
            </div>
        );
    }
}

export default App;
