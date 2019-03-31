import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { fetchQuotes } from '../actions/postActions';


class Quotes extends Component {
	componentWillMount() {
		this.props.fetchQuotes();
	}

	componentWillReceiveProps(nextProps) {
		if(nextProps.newQuote){
			this.props.quotes.unshift(nextProps.newQuote);
		}

	}

	render() {
		const quoteItems = this.props.quotes.map(quote =>(
			<div key>{ quote.id }
				<h3>{ quote.author }</h3>
				<p>{ quote.quote }</p>
				<h5>Posted { quote.posted } ago</h5>
			</div>
			))
		console.log(quoteItems);
		return(
		<div>
			<h1>Quotes</h1>
			{ quoteItems }
		</div>
		)
	}
}

Quotes.propTypes = {
	fetchQuotes: PropTypes.func.isRequired,
	quotes: PropTypes.array.isRequired,
	newQuote: PropTypes.object
};

const mapStateToProps = state => ({
	quotes: state.quotes.items,
	newQuote: state.quotes.item

});

export default connect(mapStateToProps, { fetchQuotes })(Quotes);