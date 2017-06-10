from petl.util.base import Table

def fromodoo(source, model, domain=None, fields=None):
    return OdooView(source, model, domain, fields)

class OdooView(Table):
    _source = None
    _model = None
    _domain = []
    _fields = []
    
    def __init__(self, source, model, domain=None, fields=None):
        self._source = source
        self._model = model
        if domain: 
            self._domain = domain
        if fields:
            self._fields = fields
        
    def __iter__(self):
        recs = self._source.execute(self._model, 'search_read', self._domain, self._fields)
        if len(recs) > 0 :
            fields = recs[0].keys()
            yield fields 
            for rec in recs:
                yield [ rec[k] for k in fields  ]
        else:
            if (len(self._fields) == 0):
                yield ['id']
            else:
                yield self._fields 
