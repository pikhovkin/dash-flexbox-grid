# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Col(Component):
    """A Col component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- xs (optional)
- sm (optional)
- md (optional)
- lg (optional)
- xl (optional)
- xsOffset (number; optional)
- smOffset (number; optional)
- mdOffset (number; optional)
- lgOffset (number; optional)
- xlOffset (number; optional)
- first (optional)
- last (optional)
- className (string; optional)
- tagName (string; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, xs=Component.UNDEFINED, sm=Component.UNDEFINED, md=Component.UNDEFINED, lg=Component.UNDEFINED, xl=Component.UNDEFINED, xsOffset=Component.UNDEFINED, smOffset=Component.UNDEFINED, mdOffset=Component.UNDEFINED, lgOffset=Component.UNDEFINED, xlOffset=Component.UNDEFINED, first=Component.UNDEFINED, last=Component.UNDEFINED, className=Component.UNDEFINED, tagName=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'xs', 'sm', 'md', 'lg', 'xl', 'xsOffset', 'smOffset', 'mdOffset', 'lgOffset', 'xlOffset', 'first', 'last', 'className', 'tagName']
        self._type = 'Col'
        self._namespace = 'dash_flexbox_grid'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'xs', 'sm', 'md', 'lg', 'xl', 'xsOffset', 'smOffset', 'mdOffset', 'lgOffset', 'xlOffset', 'first', 'last', 'className', 'tagName']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Col, self).__init__(children=children, **args)
