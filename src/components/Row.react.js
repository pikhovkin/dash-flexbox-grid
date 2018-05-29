import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Row as FXRow, ViewportSizeType} from 'react-flexbox-grid';


export default class Row extends Component {
    render() {
        return (
            <FXRow
                reverse={this.props.reverse}
                start={this.props.start}
                center={this.props.center}
                end={this.props.end}
                top={this.props.top}
                middle={this.props.middle}
                bottom={this.props.bottom}
                around={this.props.around}
                between={this.props.between}
                className={this.props.className}
                tagName={this.props.tagName}
                children={this.props.children}
            />
        );
    }
}

Row.propTypes = {
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