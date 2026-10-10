# posix-acl-explain

Parse numeric getfacl-style access entries and a captured identity, apply owner/named-user/group-union/other precedence and mask rules, and explain the effective rwx result.

## Who and why

Linux administrators reviewing why a numeric POSIX access ACL grants or denies a user's permissions. The named-user rule, union of matching groups and ACL mask can make rwx entries misleading. A reviewer needs the selected entries and effective permissions without changing the filesystem.

## Quickstart

Python 3.10+ and pip. No service, credential or runtime dependency:

```sh
git clone https://github.com/nripankadas07/posix-acl-explain.git
cd posix-acl-explain
python -m venv .venv
# Unix: source .venv/bin/activate; Windows: .venv\Scripts\activate
python -m pip install .
posix-acl-explain sample.acl identity.json
python demo.py
python -m pip install setuptools wheel
python verify.py
```

The fixtures are synthetic. CLI JSON is on stdout. Exit 0 means the operation succeeded; HLS/mbox return 1 for findings; all tools return 2 for malformed/unsupported input or IO errors. SQLite scan signals are evidence, not policy failures. PNG output must be a new file: repeating its command requires a new output filename.

Help: `posix-acl-explain --help`. See [DEMO.md](DEMO.md), [VALIDATION.md](VALIDATION.md), [RESEARCH.md](RESEARCH.md) and [SUPPORT.md](SUPPORT.md).

## Scope and limitations

Offline model only. Does not query NSS, read/change filesystem ACLs, model default-ACL inheritance, umask, path traversal, NFSv4/Windows ACLs, capabilities, root overrides, SELinux/AppArmor or filesystem flags. uid=0 is rejected. Include the user's primary group and all supplementary groups in gids. Owner and owner group come from the captured identity, not comments. Named IDs must be numeric. 64 KiB ACL/identity, 1,024 group IDs. It is an access-ACL explanation, not an authorization certificate.

No performance-superiority or complete-security claim. Use the comparable research to choose a tool suitable for your workflow.

## License

MIT; original implementation. Build-time setuptools/wheel and Python retain their upstream licenses.
