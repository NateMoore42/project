import Select from 'react-select';
var React = require('react');
const SKILLS = require('../data/skills');
var MAX_SELECT;

var SkillsField = React.createClass ({
  displayName: 'SkillsField',
	propTypes: {
		label: React.PropTypes.string,
		searchable: React.PropTypes.bool,
	},

	getDefaultProps () {
		return {
			label: 'Skills:',
			searchable: true,
		};
	},

	getInitialState () {
		return {
      skills: 'ALL',
			max: false,
      value: [],

			disabled: false,
			clearable: true,
			searchable: this.props.searchable,
		};
	},

  updateSkills (value) {
    console.log('Selected ' + value);
    this.setState({ value });
  },

  toggleDisabled (e) {
    MAX_SELECT = 3;
    if (this.state.value.length > MAX_SELECT) {
      this.setState({
        disabled: true
      });
    };
  },

  render() {
    var skillOptions = SKILLS[this.state.skills];

    return (
      <div className="skillsSection" id="id_skills">
        <h3 className="skillsHeading">{this.props.label}</h3>
        <Select multi
          className='skillsField'
          ref="skillsSelect"
          options={skillOptions}
          simpleValue
          clearable={this.state.clearable}
          name="skills"
          disabled={this.state.disabled}
          value={this.state.value}
          onChange={this.updateSkills}
          searchable={this.state.searchable} />
      </div>

    );
  }
});

module.exports = SkillsField;
