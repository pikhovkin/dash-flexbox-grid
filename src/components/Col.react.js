import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Col as FXCol} from 'react-flexbox-grid';


export default class Col extends Component {
    render() {
        return <FXCol {...this.props}/>
    }
}


const ColumnSizeType = FXCol.propTypes.xs;
const ViewportSizeType = FXCol.propTypes.first;


Col.propTypes = {
    xs: ColumnSizeType,
    sm: ColumnSizeType,
    md: ColumnSizeType,
    lg: ColumnSizeType,
    xl: ColumnSizeType,
    xsOffset: PropTypes.number,
    smOffset: PropTypes.number,
    mdOffset: PropTypes.number,
    lgOffset: PropTypes.number,
    xlOffset: PropTypes.number,
    first: ViewportSizeType,
    last: ViewportSizeType,
    className: PropTypes.string,
    tagName: PropTypes.string,
    children: PropTypes.node
};
