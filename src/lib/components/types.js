import PropTypes from 'prop-types';


const ColumnSizeType = PropTypes.oneOfType([PropTypes.number, PropTypes.bool]);
const ViewportSizeType = PropTypes.oneOf(['xs', 'sm', 'md', 'lg', 'xl']);


export {
    ColumnSizeType,
    ViewportSizeType
}
