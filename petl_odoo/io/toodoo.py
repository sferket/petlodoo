    
def toodoo(tbl, source, model,batch=100, tracking_disable=False):
    it = iter(tbl)
    header = next(it)
    
    cnt = 0
    recs = []
    el = next(it, None)
    while el:
        recs += [el] 
        cnt += 1
        el = next(it, None)
        if (not el) or (cnt >= batch):
            ret = source.execute(model, 'load', header, recs, {'context': {'tracking_disable' : tracking_disable}} )
            print ret
            cnt = 0
            recs = []
