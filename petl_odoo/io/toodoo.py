


def toodoo(tbl, source, model,batch=100, tracking_disable=False):
    header = tbl.pop(0)
    t = 0
    
    while t*batch<len(tbl):
        #print '%s - %s' % (t*batch,batch)
        #print table2
        ret = source.execute(model, 'load', header, tbl[t*batch:(t+1)*batch], {'context': {'tracking_disable' : tracking_disable}} )
        print ret
        t += 1
    
    