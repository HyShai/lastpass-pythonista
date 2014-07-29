LastPass Pythonista
===================

Original: [lastpass-python][] (adapted for iOS - [Pythonista][])


Uses Pythonista to allow for pseudo x-callback-url functionality for LastPass. It downloads your LastPass vault and stores it in the iOS keychain. You can then use Pythonista's powerful scripting coupled with an app such as [Launch Center Pro][] to make the LastPass iOS experience much more bearable. See example below.

**Note:** This only does a one-way read-only sync from LastPass - if you want to manipulate your vault in any way (delete/edit) you must still use the [LastPass iOS app][] (requires a LastPass Premium subscription - $12/yr).

**Note:** It stores your accounts in the iOS keychain (*not* the iCloud keychain). Although the keychain is encrypted, there may be ways to access it from other apps. Please weigh your risks before using this.

### Installation:

* Download the zip of this repo and sync it to Dropbox. Download it to Pythonista using [DropboxFilePicker][] or [DropboxSync][].

Or
* `git clone` the repo directly into Pythonista using [Shellista][]

### Usage:

1. Import your accounts by running `lpimport_api.py`
2. To use it in an x-callback-url manner call `lpfinder.py` which takes 2 arguments - `account_name` and `redirect_url`
3. Use `lpimport_api.py` to manually update your accounts (read-only)

An example LaunchCenterPro action is here: https://launchcenterpro.com/fm4lxb

Example
=======

![LP Example](https://dl.dropboxusercontent.com/u/15694301/lppy.gif)

```python
import lastpass

vault = lastpass.Vault.open_remote(username, password)
for i in vault.accounts:
    print(i.id, i.username, i.password, i.url)
```
Credits
=======
Credit for the reverse engineered LastPass API goes to [konomae][] who did 99.9% of the work on coding the Python version.

License
=======

[The MIT License][]

  [Pythonista]: https://itunes.apple.com/us/app/pythonista/id528579881
  [lastpass-python]: https://github.com/konomae/lastpass-python
  [The MIT License]: http://opensource.org/licenses/mit-license.php
  [Launch Center Pro]: https://itunes.apple.com/us/app/launch-center-pro/id532016360?mt=8&uo=4&at=11l6hc&ct=fnd
  [LastPass iOS app]:https://itunes.apple.com/us/app/lastpass-for-premium-customers/id324613447?mt=8&uo=4&at=11l6hc&ct=fnd
  [DropboxFilePicker]:https://gist.github.com/omz/fb180c58c94526e2c40b
  [DropboxSync]:https://gist.github.com/sidewinder42/8631794
  [Shellista]:https://github.com/transistor1/shellista
  [konomae]:https://github.com/konomae