import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Col as FXCol, ColumnSizeType, ViewportSizeType} from 'react-flexbox-grid';


export default class Col extends Component {
    render() {
        return (
            <FXCol
                xs={this.props.xs}
                sm={this.props.sm}
                md={this.props.md}
                lg={this.props.lg}
                xl={this.props.xl}
                xsOffset={this.props.xsOffset}
                smOffset={this.props.smOffset}
                mdOffset={this.props.mdOffset}
                lgOffset={this.props.lgOffset}
                xlOffset={this.props.xlOffset}
                first={this.props.first}
                last={this.props.last}
                className={this.props.className}
                tagName={this.props.tagName}
                children={this.props.children}
            />
        );
    }
}

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
