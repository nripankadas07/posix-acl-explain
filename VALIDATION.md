# Validation — 10 October 2026

Acceptance suite: 14 meaningful core tests, module compilation, synthetic demo, wheel build and new-venv console commands outside source. Run `python verify.py`. No competitor benchmark was performed.

Remote CI is required before LIVE; receipts are recorded in the owner's chronological index. Supported matrix: Ubuntu/Python 3.10, 3.12, 3.14. Other OS/architectures are untested. Build tools must be available to run verification; the normal install path uses pip build isolation.

Offline model only. Does not query NSS, read/change filesystem ACLs, model default-ACL inheritance, umask, path traversal, NFSv4/Windows ACLs, capabilities, root overrides, SELinux/AppArmor or filesystem flags. uid=0 is rejected. Include the user's primary group and all supplementary groups in gids. Owner and owner group come from the captured identity, not comments. Named IDs must be numeric. 64 KiB ACL/identity, 1,024 group IDs. It is an access-ACL explanation, not an authorization certificate.

Local observed result: all acceptance checks passed on Linux/Python 3.12 with setuptools 84.0.0 and wheel 0.48.0. A new wheel environment, outside-source CLI success/failure checks and the synthetic demo passed. Remote matrix and normal build-isolated installation must still be verified at the public final commit.
