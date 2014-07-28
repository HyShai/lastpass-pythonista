LastPass Pythonista
===================

Original: [lastpass-python][] (adapted for iOS - [Pythonista][])

**This uses an unofficial LastPass API**

It can be used as a replacement for the official LastPass iOS app that they charge $12 a year to use (LastPass Premium). This also adds pseudo x-callback-url support.

It stores your accounts on the iOS keychain. (While the keychain is encrypted, there may be ways to access it from other apps. So use it at your own risk!)


### Usage:

1. Import your accounts by running `lpimport_api.py`
2. Use `lpfinder.py` which takes 2 arguments - `account_name` and `redirect_url` - to use LastPass in an x-callback-url manner.
2. Use `lpimport_api.py` to manually update your accounts (read-only)


Example
=======

```python
import lastpass

vault = lastpass.Vault.open_remote(username, password)
for i in vault.accounts:
    print(i.id, i.username, i.password, i.url)
```

License
=======

[The MIT License][]

  [Pythonista]: https://itunes.apple.com/us/app/pythonista/id528579881
  [lastpass-python]: https://github.com/konomae/lastpass-python
  [The MIT License]: http://opensource.org/licenses/mit-license.php