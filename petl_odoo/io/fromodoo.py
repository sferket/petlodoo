from petl.util.base import Table
from numpy.ma.core import ids

def fromodoo(source, model, domain=None, fields=None, batch=100):
    return OdooView(source, model, domain, fields,batch)

class OdooView(Table):
    _source = None
    _model = None
    _domain = []
    _fields = []
    _batch = None
    
    def __init__(self, source, model, domain=None, fields=None, batch=None):
        self._source = source
        self._model = model
        self._batch = batch
        if domain: 
            self._domain = domain
        if fields:
            self._fields = fields
    
    def __iter__(self):
        if len(self._fields) == 0:
            f_id =  self._source.execute('ir.model', 'search_read', [('model', '=', self._model)], ['id'])[0]['id']
            self._fields = [ x['name'] for x in self._source.execute('ir.model.fields', 'search_read', [('model_id', '=', f_id)], ['name']) ]
        if 'id' not in self._fields:
            self._fields += ['id']
        if '.id' not in self._fields:
            self._fields += ['.id']
        yield self._fields
        ids = self._source.execute(self._model, 'search', self._domain)
        for s in [ids[x:x+self._batch] for x in xrange(0, len(ids), self._batch)]:
            for rec in self._source.execute(self._model, 'export_data', s, self._fields, True)['datas']:
                yield rec
