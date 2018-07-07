import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Row as FXRow} from 'react-flexbox-grid';


export default class Row extends Component {
    render() {
        return <FXRow {...this.props}/>
    }
}


const ViewportSizeType = FXRow.propTypes.start;


Row.propTypes = {
    id: PropTypes.string,
  
    reverse: PropTypes.bool,
    start: ViewportSizeType,
    center: ViewportSizeType,
    end: ViewportSizeType,
    top: ViewportSizeType,
    middle: ViewportSizeType,
    bottom: ViewportSizeType,
    around: ViewportSizeType,
    between: ViewportSizeType,
    className: PropTypes.string,
    tagName: PropTypes.string,
    children: PropTypes.node
};