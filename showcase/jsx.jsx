import React, { Component } from 'react';

// Child component
function Greeting({ name }) {
    return <h1>Hello, {name}!</h1>;
}

// Main App component
class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: 'World',
            count: 0
        };
    }

    componentDidMount() {
        console.log('App component mounted');
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevState.count !== this.state.count) {
            console.log(`Count updated: ${this.state.count}`);
        }
    }

    handleChange = (event) => {
        this.setState({ name: event.target.value });
    };

    incrementCount = () => {
        this.setState((prevState) => ({ count: prevState.count + 1 }));
    };

    render() {
        const { name, count } = this.state;
        return (
            <div className="app">
                <Greeting name={name} />
                <input
                    type="text"
                    value={name}
                    onChange={this.handleChange}
                    placeholder="Enter your name"
                />
                <button onClick={this.incrementCount}>Click me!</button>
                <p>You clicked {count} times.</p>
            </div>
        );
    }
}

