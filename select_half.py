def selectHalf(obj='',side='x+'):
    vtxCnt = cmds.polyEvaluate(obj, v=True)
    vtxs = []
    
    for i in range(vtxCnt):
        vtxID = f'{obj}.vtx[{i}]'
        pos = cmds.xform(vtxID, q=True, t=True, os=True)
        if side == 'x+':
            if pos[0]>0.000000000001:
                vtxs.append(vtxID)
        elif side == 'x-':
            if pos[0]<0.000000000001:
                vtxs.append(vtxID)
            
    cmds.select(vtxs)
    
selectHalf('pSphere1',side='x+')