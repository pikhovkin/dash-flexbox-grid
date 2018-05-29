import React from 'react';
import {shallow} from 'enzyme';

import Col from '../Col.react';

describe('Col', () => {

    it('renders', () => {
        const component = shallow(<Col/>);
        expect(component).toBe.ok;
    });
});
