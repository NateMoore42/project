import Select from 'react-select';
var React = require('react');
const RACES = require('../data/races');
const SUBRACES = require('../data/subraces');
const LANGUAGES = require('../data/languages');

var RaceField = React.createClass ({
  displayName: 'RaceField',
	propTypes: {
		label: React.PropTypes.string,
		searchable: React.PropTypes.bool,
	},

	getDefaultProps () {
		return {
			label: 'Races:',
			searchable: true,
		};
	},

	getInitialState () {
		return {
      expansion: 'ALL',
			raceLevel: 'Human',
			raceValue: 'Human',
      subraceValue: null,

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

  updateSubrace (newSubrace, e) {
    console.log('Subrace changed to ' + newSubrace);
    this.setState({
      subraceValue: newSubrace,
    });
  },

	updateRace (newRace) {
    console.log('Level changed to ' + newRace);
      if (newRace === 'Half-Orc') {
        this.setState({
          raceValue: newRace,
          raceLevel: 'HalfOrc',
        });
      } else if (newRace === 'Half-Elf') {
        this.setState({
          raceValue: newRace,
          raceLevel: 'HalfElf',
        });
      } else if (newRace === "Yuan-Ti Pureblood") {
        this.setState({
          raceValue: newRace,
          raceLevel: 'YuanTiPureblood',
        });
      } else {
  		this.setState({
  			raceValue: newRace,
        raceLevel: newRace,
  		});
  	};
  },

	focusRaceSelect () {
		this.refs.raceSelect.focus();
	},

  render() {
    var raceOptions = RACES[this.state.expansion];
    var subraceOptions = SUBRACES[this.state.raceLevel];

    return (
      <div className="raceSection" id="race">
          <h3 className="raceHeading">{this.props.label}</h3>
        <Select
          className='raceField'
          ref="raceSelect"
          options={raceOptions}
          simpleValue
          clearable={this.state.clearable}
          name="race"
          value={this.state.raceValue}
          onChange={this.updateRace}
          searchable={this.state.searchable} />
          <h3 className='subrace-heading'>Subrace:</h3>
          <Select
            className='raceField'
            ref="subraceSelect"
            options={subraceOptions}
            simpleValue
            clearable={this.state.clearable}
            name="subrace"
            disabled={this.state.disabled}
            value={this.state.subraceValue}
            onChange={this.updateSubrace}
            searchable={this.state.searchable} />
      </div>

    );
  }
});

module.exports = RaceField;
