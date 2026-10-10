import unittest
from posix_acl_explain import explain,parse
BASE="user::rwx\ngroup::r--\nother::---\n";EXT=BASE+"user:42:rwx\ngroup:10:-w-\ngroup:20:--x\nmask::rw-\n"
def who(uid=50,gids=()):return {"owner_uid":1,"owner_gid":2,"uid":uid,"gids":list(gids)}
class Contract(unittest.TestCase):
    def test_owner_unmasked(self):self.assertEqual(explain(EXT,who(1))["effective_permissions"],"rwx")
    def test_named_user_mask(self):self.assertEqual(explain(EXT,who(42))["effective_permissions"],"rw-")
    def test_named_precedes_groups(self):
        text=BASE+"user:42:---\ngroup:10:rwx\nmask::rwx\n";self.assertEqual(explain(text,who(42,[10]))["effective_permissions"],"---")
    def test_group_union(self):self.assertEqual(explain(EXT,who(50,[2,10,20]))["raw_permissions"],"rwx");self.assertEqual(explain(EXT,who(50,[2,10,20]))["effective_permissions"],"rw-")
    def test_group_denial_no_fallback(self):self.assertEqual(explain("user::rwx\ngroup::---\nother::rwx",who(50,[2]))["effective_permissions"],"---")
    def test_other(self):self.assertEqual(explain(BASE,who())["selection"],"other")
    def test_group_minimal(self):self.assertEqual(explain(BASE,who(50,[2]))["effective_permissions"],"r--")
    def test_extended_requires_mask(self):
        with self.assertRaises(ValueError):parse(BASE+"user:42:rwx")
    def test_duplicate_canonical_id(self):
        with self.assertRaises(ValueError):parse(EXT+"user:042:r--")
    def test_named_qualifier_rejected(self):
        with self.assertRaises(ValueError):parse(BASE+"user:alice:rwx")
    def test_root_unsupported(self):
        with self.assertRaises(ValueError):explain(BASE,who(0))
    def test_default_unsupported(self):
        with self.assertRaises(ValueError):parse("default:user::rwx")
    def test_invalid_bool_ids(self):
        with self.assertRaises(ValueError):explain(BASE,who(True))
    def test_comments(self):self.assertEqual(parse("# file: private\n"+BASE),parse(BASE))
