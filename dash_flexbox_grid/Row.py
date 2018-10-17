# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Row(Component):
    """A Row component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- reverse (boolean; optional)
- start (optional)
- center (optional)
- end (optional)
- top (optional)
- middle (optional)
- bottom (optional)
- around (optional)
- between (optional)
- className (string; optional)
- tagName (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, reverse=Component.UNDEFINED, start=Component.UNDEFINED, center=Component.UNDEFINED, end=Component.UNDEFINED, top=Component.UNDEFINED, middle=Component.UNDEFINED, bottom=Component.UNDEFINED, around=Component.UNDEFINED, between=Component.UNDEFINED, className=Component.UNDEFINED, tagName=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'reverse', 'start', 'center', 'end', 'top', 'middle', 'bottom', 'around', 'between', 'className', 'tagName']
        self._type = 'Row'
        self._namespace = 'dash_flexbox_grid'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'id', 'reverse', 'start', 'center', 'end', 'top', 'middle', 'bottom', 'around', 'between', 'className', 'tagName']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Row, self).__init__(children=children, **args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('Row(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Row(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
