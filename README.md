LastPass Pythonista
===================

Original: [lastpass-python][] (adapted for iOS - [Pythonista][])


Uses Pythonista to allow for pseudo x-callback-url functionality for LastPass. It downloads your LastPass vault and stores it in the iOS keychain. You can then use Pythonista's powerful scripting coupled with an app such as [Launch Center Pro][] to make the LastPass iOS experience much more bearable.

**Note:** This does a one-way read-only sync from LastPass - if you want to manipulate your vault in any way (delete/edit) you must use the [LastPass iOS app][] (requires a LastPass Premium subscription - $12/yr).

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

Example
=======

<a href="https://www.youtube.com/watch?v=8WmbEWjLWbY" target="_blank"><img src="http://img.youtube.com/vi/8WmbEWjLWbY/0.jpg" alt="LP Example"></a>

```python

```
Credits
=======
Credit for the reverse engineered LastPass API goes to [konomae][] who did 99.9% of the work on coding the Python version.

Credit for the adaption of PBKDF to use pbkdf2 instead of simple-pbkdf2 goes to [Ole Moritz][] (and without whom we wouldn't have the awesome Pythonista ;) )

Credit for pbkdf2.py goes to [Dwayne C. Litzenberger][]

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
  [Ole Moritz]:https://github.com/omz
  [Dwayne C. Litzenberger]:https://github.com/dlitz/python-pbkdf2
