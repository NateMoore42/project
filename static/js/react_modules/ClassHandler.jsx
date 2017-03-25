import Select from 'react-select';
var React = require('react');
const CLASSES = require('../data/class');
const LEVELS = require('../data/levels');
var MAX_SELECT;

var classField = React.createClass ({
  displayName: 'classField',
	propTypes: {
		label: React.PropTypes.string,
	},

	getDefaultProps () {
		return {
			label: 'Class:',
			searchable: true,
		};
	},

	getInitialState () {
		return {
      classes: 'ALLCLASSES',
      levels: 'LEVELS',
      singleValue: 'Barbarian',
      value: [],

      matchPos: 'any',
      matchValue: true,
      classValue: 1,

			disabled: false,
      levelClearable: false,
			clearable: false,
      multiClearable: true,
		};
	},

  updateClassSingle (singleValue) {
    console.log('Selected ' + singleValue);
    this.setState({ singleValue });
  },

  updateClassMulti (value) {
    console.log('Selected ' + value);
      this.setState({ value });
  },

  updateLevel (classValue) {
    console.log('Level ' + classValue);
    this.setState({ classValue });
  },

  onChangeMatchStart (event) {
    this.setState({
      matchPos: event.target.checked ? 'start' : 'any'
    });
  },

  onChangeMatchValue (event) {
    this.setState({
      matchValue: event.target.checked
    });
  },

  render() {
    var classOptions = CLASSES[this.state.classes];
    var levelOptions = LEVELS[this.state.levels];
    var matchLevel = 'any';
    if (this.state.matchValue) {
      matchLevel = 'value';
    }
    return (
      <div className="classSection" id="id_class">
        <h3 className="levelheading">Level:</h3>
          <Select
            className='levelField'
            ref='levelSelect'
            name='level'
            matchPos={this.state.matchPos}
            matchLevel={matchLevel}
            onChange={this.updateLevel}
            options={levelOptions}
            simpleValue
            value={this.state.classValue}
            clearable={this.state.levelClearable}/>

        <h3 className="classHeading">{this.props.label}</h3>
        {this.state.classValue === 1 &&
          <Select
            className='classField'
            ref="classSelect"
            options={classOptions}
            simpleValue
            clearable={this.state.clearable}
            name="c_class"
            disabled={this.state.disabled}
            value={this.state.singleValue}
            onChange={this.updateClassSingle}
            searchable={this.state.searchable} />
        }
        {this.state.classValue > 1 &&
          <Select multi
            className='classField'
            ref="classSelect"
            options={classOptions}
            simpleValue
            clearable={this.state.multiClearable}
            name="c_class"
            disabled={this.state.disabled}
            value={this.state.value}
            onChange={this.updateClassMulti}
            searchable={this.state.searchable} />
        }

      </div>

    );
  }
});

module.exports = classField;
