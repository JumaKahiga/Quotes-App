import { FETCH_QUOTES, NEW_QUOTE } from '../actions/types';

const initialState = {
	items: [],
	item: {}
}

export default function(state = initialState, action) {
	switch(action.type) {
		case FETCH_QUOTES:
			return {
				...state,
				items: action.payload
			}
		case NEW_QUOTE:
			return {
				...state,
				item: action.payload
			}
		default:
		return state;
	}

}