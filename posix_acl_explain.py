"""Explain the POSIX access ACL selection and mask using numeric IDs."""
import argparse, json, pathlib, re
PERMS=re.compile(r"[r-][w-][x-]")
def parse(text):
    acl={}
    if len(text)>65536:raise ValueError("ACL exceeds 64 KiB")
    for line in text.splitlines():
        line=line.split("#",1)[0].strip()
        if not line:continue
        parts=line.split(":")
        if len(parts)!=3 or parts[0] not in ("user","group","mask","other") or not PERMS.fullmatch(parts[2]):raise ValueError("numeric access ACL entries required")
        tag,qual,p=parts
        if qual:
            if tag not in ("user","group") or not qual.isascii() or not qual.isdigit() or int(qual)>2**32-1:raise ValueError("invalid numeric qualifier")
            qual=str(int(qual))
        key=(tag,qual)
        if key in acl:raise ValueError("duplicate ACL entry")
        acl[key]={c for c in p if c!="-"}
    if not all(k in acl for k in [("user",""),("group",""),("other","")]):raise ValueError("missing base ACL entry")
    if any(k[1] for k in acl) and ("mask","") not in acl:raise ValueError("extended ACL requires mask")
    return acl
def explain(text,identity):
    if not isinstance(identity,dict) or set(identity)!={"owner_uid","owner_gid","uid","gids"}:raise ValueError("identity needs owner_uid, owner_gid, uid, gids")
    for key in ("owner_uid","owner_gid","uid"):
        if type(identity[key])!=int or not 0<=identity[key]<=2**32-1:raise ValueError("invalid ID")
    gids=identity["gids"]
    if not isinstance(gids,list) or len(gids)>1024 or any(type(x)!=int or not 0<=x<=2**32-1 for x in gids):raise ValueError("invalid supplementary/primary gids")
    if identity["uid"]==0:raise ValueError("root/capability overrides are outside this model")
    acl=parse(text);uid=str(identity["uid"]);mask=acl.get(("mask",""),set("rwx"));entries=[];masked=False
    if identity["uid"]==identity["owner_uid"]:entries=[("user","")];selection="owner"
    elif ("user",uid) in acl:entries=[("user",uid)];selection="named-user";masked=True
    else:
        groups=set(gids)
        if identity["owner_gid"] in groups:entries.append(("group",""))
        entries.extend(k for k in acl if k[0]=="group" and k[1] and int(k[1]) in groups)
        if entries:selection="group-union";masked=True
        else:selection="other";entries=[("other","")]
    raw=set().union(*(acl[k] for k in entries));effective=raw&mask if masked else raw
    def show(s):return "".join(c if c in s else "-" for c in "rwx")
    return {"selection":selection,"matched_entries":[":".join(k) for k in sorted(entries)],"raw_permissions":show(raw),"mask":show(mask) if masked else None,"effective_permissions":show(effective),"filesystem_modified":False}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("acl");p.add_argument("identity");a=p.parse_args()
    try:
        raw=pathlib.Path(a.identity).read_bytes()
        if len(raw)>65536:raise ValueError("identity exceeds 64 KiB")
        print(json.dumps(explain(pathlib.Path(a.acl).read_text(),json.loads(raw))));return 0
    except (ValueError,OSError) as e:print(json.dumps({"error":str(e)}));return 2
if __name__=="__main__":raise SystemExit(main())
