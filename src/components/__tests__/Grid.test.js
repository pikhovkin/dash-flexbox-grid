import React from 'react';
import {shallow} from 'enzyme';

import Grid from '../Grid.react';

describe('Grid', () => {

    it('renders', () => {
        const component = shallow(<Grid fluid/>);
        expect(component).toBe.ok;
    });
});
