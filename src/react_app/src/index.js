import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

import { ApolloProvider } from 'react-apollo'
import ApolloClient, {gql} from 'apollo-boost';
import {InMemoryCache} from 'apollo-cache-inmemory'

//https://www.howtographql.com/react-apollo/1-getting-started/
//https://www.apollographql.com/docs/react/essentials/get-started.html
const client = new ApolloClient({
    uri: 'http://localhost:5000/graph',
    // cache: InMemoryCache,
    // request: operation => {
    //     operation.setContext({
    //         headers: {
    //             authorization: `Bearer ${process.env.GITHUB_PERSONAL_ACCESS_TOKEN}`,
    //         },
    //     });
    // },
});

const GET_USER_FEED = gql`
  {
  currentUser {
    feed(action: {get: {userId: 1, sortBy: [CATEGORY], sortOrder: [false], limit: 2}}) {
      title
      category
      description
      source
      pubDate
    }
  }
}
`;

// function onGraphqlResult(result){
//     console.log(result.data);
// }
//
// client
//     .query({
//         query: GET_USER_FEED,
//     })
//     .then(result => onGraphqlResult(result));

ReactDOM.render(
    <ApolloProvider client={client}>
        <App/>
    </ApolloProvider>,
    document.getElementById('root')
);
registerServiceWorker();
