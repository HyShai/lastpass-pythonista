LastPass Pythonista
===================

Original: [lastpass-python][] (adapted for iOS - [Pythonista][])


Uses Pythonista to allow for pseudo x-callback-url functionality for LastPass. It downloads your LastPass vault and stores it in the iOS keychain. You can then use Pythonista's powerful scripting coupled with an app such as [Launch Center Pro][] to make the LastPass iOS experience much more bearable.

**Note:** This only does a one-way read-only sync from LastPass - if you want to manipulate your vault in any way (delete/edit) you must still use the [LastPass iOS app][] (requires a LastPass Premium subscription - $12/yr).

**Note:** It stores your accounts in the iOS keychain (*not* the iCloud keychain). Although the keychain is encrypted, there may be ways to access it from other apps. Please weigh the risks before using this.

### Installation:

* Download the zip of this repo and sync it to Dropbox. Download it to Pythonista using [DropboxFilePicker][] or [DropboxSync][].

Or
* `git clone https://github.com/HyShai/lastpass-pythonista.git` directly into Pythonista using [Shellista][]

### Usage:

1. Import your accounts by running `lpimport_api.py`
2. To use it in an x-callback-url manner run `lpfinder.py` which takes 2 arguments - `account_name` and `redirect_url`
3. Tap the account for which you want the password 
4. The password will be copied to the clipboard and you will be redirected to the url/app that you passed in
4. Use `lpimport_api.py` to manually update your accounts (read-only)

An example LaunchCenterPro action is here: https://launchcenterpro.com/q9qmfg 
(this assumes `lpfinder.py` is in your root folder)

Example
=======

[![LP Example](http://img.youtube.com/vi/8WmbEWjLWbY/0.jpg)](https://www.youtube.com/watch?v=8WmbEWjLWbY)

```python

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