import React from 'react';
import ReactDOM from 'react-dom';
import Select from 'react-select';
import 'react-select/dist/react-select.css';

import Class from './react_modules/ClassHandler';
import Races from './react_modules/RaceHandler';
import Backgrounds from './react_modules/BackgroundHandler';
import Skills from './react_modules/SkillsHandler';
import Languages from './react_modules/LanguageHandler';

ReactDOM.render (
  <div className="reactCreationForm">
    <Races label="Race:" searchable />
    <Class label="Class:" searchable />
    <Backgrounds label="Background:" searchable />
    <Languages label="Languages:" searchable />
    <Skills label="Skills:" searchable />
  </div>,
  document.getElementById('react')
);
