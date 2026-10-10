# Research and candidate brief — 10 October 2026

User: Linux administrators reviewing why a numeric POSIX access ACL grants or denies a user's permissions.

Pain: The named-user rule, union of matching groups and ACL mask can make rwx entries misleading. A reviewer needs the selected entries and effective permissions without changing the filesystem.

Smallest useful capability: Parse numeric getfacl-style access entries and a captured identity, apply owner/named-user/group-union/other precedence and mask rules, and explain the effective rwx result.

Demand is **inferred** from the workflow and established alternatives, not a verified request for this project. No invented users, adoption or growth promise.

Queries: `posix acl sort:stars`, GitHub repository search with stars qualifier, bounded first five results plus named relevant established comparables. Connector coverage and relevance selection are limited; this is not an exhaustive ranking. Highest-star relevant comparable **among those inspected**: [ehmicky/unix-permissions](https://github.com/ehmicky/unix-permissions) (145 stars). Stars are research context, not technical performance.

| Exact comparable | Observed stars | Last push UTC | API license metadata |
| --- | ---: | --- | --- |
| [ehmicky/unix-permissions](https://github.com/ehmicky/unix-permissions) | 145 | 2026-08-28T17:00:57Z | Apache-2.0 |
| [iustin/pylibacl](https://github.com/iustin/pylibacl) | 21 | 2025-09-14T17:32:04Z | LGPL-2.1 |
| [voxpupuli/puppet-posix_acl](https://github.com/voxpupuli/puppet-posix_acl) | 17 | 2026-10-04T20:50:41Z | Apache-2.0 |

Observed 10 October 2026 via GitHub repository metadata, current README and first five open issues. Missing README/license metadata is unavailable rather than evidence of absent support; NOASSERTION requires manual license review before any reuse. No reuse occurred. Archived status is preserved in raw research evidence; grafov/m3u8's README identifies its successor and suspended support.

Fair comparison: established alternatives have broader parsing, client, GUI, optimization, binding or management workflows and should be considered first. This tool offers the bounded offline workflow in the capability above, a Python source installation, synthetic example and exact failure exits. Its zero runtime dependencies do not establish better reliability or support. Installation and time-to-first-result were measured only for our examples; competitor installations and equivalent workloads were not benchmarked. We make no absence or superiority claim. Compare the stated scope/limitations with each alternative's current docs before selecting it.

Portfolio differentiation: portable-tree checks filesystem portability; no owned tool explains ACL precedence or group masks. No repository permissions are changed. The other four daily projects use different data, algorithms and users (video windows, mail graphs, SQL plans, PNG bytes, numeric ACLs); they are not subdivisions of one product.

Acceptance: the documented example produces its expected evidence; meaningful malformed inputs fail; original core behavior/regressions pass 14 tests; installed console command works outside source; remote CI runs Python 3.10, 3.12 and 3.14. Public existence without these checks is not a verified launch.

Discovery: posix-acl and linux topics; named-user denial and group-union examples.

Limits: Offline model only. Does not query NSS, read/change filesystem ACLs, model default-ACL inheritance, umask, path traversal, NFSv4/Windows ACLs, capabilities, root overrides, SELinux/AppArmor or filesystem flags. uid=0 is rejected. Include the user's primary group and all supplementary groups in gids. Owner and owner group come from the captured identity, not comments. Named IDs must be numeric. 64 KiB ACL/identity, 1,024 group IDs. It is an access-ACL explanation, not an authorization certificate.

## Workflow comparison

unix-permissions is a JavaScript library/CLI around Unix permission representations and mode manipulation. pylibacl is a Python extension binding libacl for real operating-system ACL operations; puppet-posix_acl manages ACL state through Puppet. Those have different installation requirements and broader integration/management workflows. This pure-Python CLI explains a captured numeric access ACL without touching a filesystem or NSS. Its model omits several OS authorization layers, so its portability and small install cannot establish effective access on a live system. Compare libacl/getfacl on the target host for actual administration.

Evidence observed between 06:12 and 06:22 UTC, 10 October 2026. Repository metadata is a snapshot; push time is activity evidence, not a support guarantee.
