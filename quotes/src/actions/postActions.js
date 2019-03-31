import { FETCH_QUOTES, NEW_QUOTE } from './types';

var apiURL = "http://127.0.0.1:8000/quotes/my_quotes/"

export const fetchQuotes = () => dispatch => {
	fetch(apiURL)
	.then(res => res.json())
	.then(data=> 
		dispatch({
			type: FETCH_QUOTES,
			payload: data
		})
	);
};

export const createQuote = (postData) => dispatch => {
	fetch(apiURL, {
		method: 'POST',
		headers: {
			'content-type': 'application/json'
		},
		body: JSON.stringify(postData)
	})
	.then(res => res.json())
	.then(data =>
		dispatch({
			type: NEW_QUOTE,
			payload: data
		}));
};