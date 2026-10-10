# Synthetic demo

Run `python demo.py` to exercise the checked-in synthetic fixture, expected success/evidence and malformed input using `smoke.json`.

Installed command: `posix-acl-explain sample.acl identity.json`. Each smoke case records its exact expected exit and any essential output fields. Policies/input schemas follow the fixture files and module docstring; no private input is included.

Offline model only. Does not query NSS, read/change filesystem ACLs, model default-ACL inheritance, umask, path traversal, NFSv4/Windows ACLs, capabilities, root overrides, SELinux/AppArmor or filesystem flags. uid=0 is rejected. Include the user's primary group and all supplementary groups in gids. Owner and owner group come from the captured identity, not comments. Named IDs must be numeric. 64 KiB ACL/identity, 1,024 group IDs. It is an access-ACL explanation, not an authorization certificate.
