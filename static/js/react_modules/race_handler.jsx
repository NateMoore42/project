import Select from 'react-select';
var React = require('react');
var RACES = [
  { value: 'Human', label: 'Human', nodeLevel: 'HU' },
  { value: 'Elf', label: 'Elf', nodeLevel: 'EL' },
  { value: 'Half-Elf', label: 'Half-Elf', nodeLevel: 'HE' },
];

var SUBRACES = [
  { value: 'Human', label: 'Human', nodeLevel: 'HU' },
  { value: 'Human Variant', label: 'Human Variant', nodeLevel: 'HU' },
  { value: 'High Elf', label: 'High Elf', nodeLevel: 'EL' },
  { value: 'Wood Elf', label: 'Wood Elf', nodeLevel: 'EL' },
  { value: 'Half-Elf', label: 'Half-Elf', nodeLevel: 'HE' },
  { value: 'Half-Sun Elf', label: 'Half-Sun Elf', nodeLevel: 'HE' },
];

var topNodeLength = RACES.length;
var subNodeLength = SUBRACES.length;

var RaceHandler = React.createClass ({
  displayName: 'RaceHandler',
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
      raceOptions: RACES,
			subraceOptions: SUBRACES,

      topNodeLevel: RACES[0][2],
      subNodeLevel: SUBRACES[0][2],

			raceValue: RACES[0],
      subraceValue: SUBRACES[0],

			disabled: false,
			clearable: false,
			searchable: this.props.searchable,
		};
	},

  updateSubrace (newSubrace, newNode) {
    console.log('Subrace changed to ' + newSubrace);
      this.setState({
        subNodeLevel: this.state.topNodeLevel,
        subraceValue: newSubrace,
      });
  },

	updateRace (newRace, newNode) {
    var next = function(RACES, nodeLevel) {
      for (var i = 0; RACES.length; i++) {
        if (RACES[i].nodeLevel === nodeLevel) {
          return RACES[i + 1] && RACES[i + 1].value;
        }
      }
    };
    newNode = next;
    console.log('Node changed to ' + newNode);
    console.log('Level changed to ' + newRace);
  		this.setState({
        topNodeLevel: newNode,
  			raceValue: newRace,
  		});
  },

	focusRaceSelect () {
		this.refs.raceSelect.focus();
	},

  render() {

    return (
      <div className="raceSection" id="race">
          <h3 className="raceHeading">{this.props.label}</h3>
        <Select
          className='raceField'
          ref="raceSelect"
          options={this.state.raceOptions}
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
            options={this.state.subraceOptions}
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

module.exports = RaceHandler;
