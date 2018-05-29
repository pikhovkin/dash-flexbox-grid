import React from 'react';
import {shallow} from 'enzyme';

import Row from '../Row.react';

describe('Row', () => {

    it('renders', () => {
        const component = shallow(<Row/>);
        expect(component).toBe.ok;
    });
});
