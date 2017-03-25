import Select from 'react-select';
var React = require('react');
const BACKGROUNDS = require('../data/backgrounds');

var BackgroundField = React.createClass ({
  displayName: 'BackgroundField',
	propTypes: {
		label: React.PropTypes.string,
		searchable: React.PropTypes.bool,
	},

	getDefaultProps () {
		return {
			label: 'Background:',
			searchable: true,
		};
	},

	getInitialState () {
		return {
      expansion: 'ALL',
			backgroundLevel: 'Acolyte',
			backgroundValue: 'Acolyte',

			disabled: false,
			clearable: false,
			searchable: this.props.searchable,
		};
	},

	switchLevel (e) {
		var newLevel = e.target.value;
		console.log('Level changed to ' + newLevel);
		this.setState({
			raceLevel: newLevel,
		});
	},

	updateBackground (newBackground) {
		console.log('Background changed to ' + newBackground);
    console.log('Level changed to ' + newBackground);
  	this.setState({
  		backgroundValue: newBackground,
      backgroundLevel: newBackground,
  	});
  },

	focusRaceSelect () {
		this.refs.raceSelect.focus();
	},

  render() {
    var backgroundOptions = BACKGROUNDS[this.state.expansion];

    return (
      <div className="backgroundSection" id="background">
          <h3 className="backgroundHeading">{this.props.label}</h3>
        <Select
          className='backgroundField'
          ref="backgroundSelect"
          options={backgroundOptions}
          simpleValue
          clearable={this.state.clearable}
          name="background"
          value={this.state.backgroundValue}
          onChange={this.updateBackground}
          searchable={this.state.searchable} />
      </div>

    );
  }
});

module.exports = BackgroundField;
