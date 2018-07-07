import React from 'react';
import PropTypes from 'prop-types';
import {Grid as FXGrid} from 'react-flexbox-grid';


export default class Grid extends React.Component {
    render() {
        return <FXGrid {...this.props}/>
    }
}

Grid.propTypes = {
    id: PropTypes.string,

    fluid: PropTypes.bool,
    className: PropTypes.string,
    tagName: PropTypes.string,
    children: PropTypes.node
};
