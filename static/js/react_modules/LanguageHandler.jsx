import Select from 'react-select';
var React = require('react');
const LANGUAGES = require('../data/languages');
var MAX_SELECT;

var LanguageField = React.createClass ({
  displayName: 'LanguageField',
	propTypes: {
		label: React.PropTypes.string,
		searchable: React.PropTypes.bool,
	},

	getDefaultProps () {
		return {
			label: 'Languages:',
			searchable: true,
		};
	},

	getInitialState () {
		return {
      languages: 'ALL',
      langDisabled: false,
			max: false,
      value: [],

			disabled: false,
			clearable: true,
			searchable: this.props.searchable,
		};
	},

  updateLanguages (value) {
    console.log('Selected language ' + value);
    this.setState({ value });
  },

  toggleDisabled (e) {
    this.setState({ disabled: e.target.checked})
  },

  toggleLanguage (e) {
    let langDisabled = e.target.checked;
    this.setState({
      langDisabled: langDisabled,
      commonLanguages: langDisabled ? 'ALL' : 'LANGUAGESDISABLED',
    });
  },

  render() {
    var languageOptions = LANGUAGES[this.state.languages];

    return (
      <div className="languageSection" id="id_language">
        <h3 className="languageHeading">{this.props.label}</h3>
        <Select multi
          className='LanguageField'
          ref="LanguageSelect"
          options={languageOptions}
          simpleValue
          clearable={this.state.clearable}
          name="language"
          disabled={this.state.disabled}
          value={this.state.value}
          onChange={this.updateLanguages}
          searchable={this.state.searchable} />
      </div>

    );
  }
});

module.exports = LanguageField;
