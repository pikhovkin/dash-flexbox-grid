# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Grid(Component):
    """A Grid component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- fluid (boolean; optional)
- className (string; optional)
- tagName (string; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, fluid=Component.UNDEFINED, className=Component.UNDEFINED, tagName=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'fluid', 'className', 'tagName']
        self._type = 'Grid'
        self._namespace = 'dash_flexbox_grid'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'fluid', 'className', 'tagName']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Grid, self).__init__(children=children, **args)
