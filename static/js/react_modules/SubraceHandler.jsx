import Select from 'react-select';
var React = require('react');
const SUBRACES = require('../data/subraces');

var SubraceField = React.createClass ({
  displayName: 'SubraceField',
	propTypes: {
		label: React.PropTypes.string,
		searchable: React.PropTypes.bool,
	},

	getDefaultProps () {
		return {
			label: null,
			searchable: false,
		};
	},

	getInitialState () {
      return {
        expansion: 'ALL',
        disabled: true,
        searchable: this.props.searchable,
        selectValue: null,
        clearable: false,
      };
	},

	switchExpansions (e) {
		var newExpansion = e.target.value;
		console.log('Expansion changed to ' + newExpansion);
		this.setState({
			expansion: newExpansion,
			selectValue: null
		});
	},

	updateValue (newValue) {
		console.log('Subrace changed to ' + newValue);
		this.setState({
			selectValue: newValue
		});
	},

  render() {
    var options = SUBRACES[this.state.expansion];
      return (
        <div className="race-section">
          <h3 className="race-heading">{this.props.label}</h3>
          <Select
            options={options}
            simpleValue
            clearable={this.state.clearable}
            name="subrace"
            classID="id_subrace"
            disabled={this.state.disabled}
            value={this.state.selectValue}
            onChange={this.updateValue}
            searchable={this.state.searchable} />
        </div>
      );
    }
});

module.exports = SubraceField;
