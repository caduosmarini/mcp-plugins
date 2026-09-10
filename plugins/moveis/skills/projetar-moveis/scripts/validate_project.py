"""Validate the minimal furniture source contract (stdlib only; not engineering approval)."""
import argparse
import json
import math


def validate(data):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
    def number(v):
        return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)
    require(data.get('units') == 'mm', 'units must be mm')
    require(bool(data.get('revision')), 'revision missing')
    parts = data.get('parts', [])
    require(bool(parts), 'parts empty')
    ids = [p['id'] for p in parts]
    require(len(ids) == len(set(ids)), 'duplicate part ID')
    by_id = {p['id']: p for p in parts}
    for p in parts:
        name = p['id']
        require(len(p['finished']) == len(p['raw']) == 2, name+': expected L,D')
        require(all(number(v) and v > 0 for v in p['finished']+p['raw']+[p['thickness']]), name+': invalid dimension')
        e = p['edges']
        require(set(e) == {'L0','L1','D0','D1'}, name+': four edge keys required')
        require(all(number(v) and v >= 0 for v in e.values()), name+': invalid band thickness')
        expected = [p['finished'][0]-e['L0']-e['L1'], p['finished'][1]-e['D0']-e['D1']]
        require(all(abs(a-b) < 1e-6 for a,b in zip(p['raw'], expected)), name+': edge deduction mismatch')
    sheets = data.get('sheets', [])
    sheet_ids = [s['id'] for s in sheets]
    require(len(sheet_ids) == len(set(sheet_ids)), 'duplicate sheet ID')
    placed = []
    for s in sheets:
        L,D = s['size']; trim,kerf=s['trim'],s['kerf']
        require(all(number(v) for v in [L,D,trim,kerf]) and L>2*trim and D>2*trim and trim>=0 and kerf>=0, str(s['id'])+': invalid sheet')
        rects=[]
        for a in s['placements']:
            pid=a['id']; placed.append(pid)
            require(pid in by_id, 'unknown placement '+pid)
            if pid not in by_id:
                continue
            p=by_id[pid]; w,h=p['raw']
            if a.get('rotated',False):
                require(p.get('rotation_allowed',True), pid+': forbidden rotation')
                w,h=h,w
            x,y=a['x'],a['y']
            require(number(x) and number(y),pid+': invalid position')
            require(x>=trim-1e-6 and y>=trim-1e-6 and x+w<=L-trim+1e-6 and y+h<=D-trim+1e-6,pid+': outside usable sheet')
            for bid,bx,by,bw,bh in rects:
                separate = x+w+kerf<=bx+1e-6 or bx+bw+kerf<=x+1e-6 or y+h+kerf<=by+1e-6 or by+bh+kerf<=y+1e-6
                require(separate,pid+'/'+bid+': overlap or insufficient kerf')
            rects.append((pid,x,y,w,h))
    require(sorted(placed)==sorted(ids), 'each physical part must be placed exactly once')
    passes=data.get('passes',[])
    require(bool(passes),'passes missing; geometry does not prove cutting sequence')
    require(len({p['id'] for p in passes})==len(passes),'duplicate pass ID')
    for p in passes:
        require(p['sheet_id'] in sheet_ids,'pass refers to unknown sheet')
    return errors


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project')
    args=parser.parse_args()
    try:
        with open(args.project,encoding='utf-8') as f:
            errors=validate(json.load(f))
    except (KeyError, TypeError, ValueError, OSError) as exc:
        errors=['Invalid source: '+str(exc)]
    print(json.dumps({'valid':not errors,'errors':errors,'scope':'dimensions, bands, placement, kerf, IDs; not cutting feasibility or structural/electrical approval'},ensure_ascii=False,indent=2))
    return bool(errors)


if __name__=='__main__':
    raise SystemExit(main())
