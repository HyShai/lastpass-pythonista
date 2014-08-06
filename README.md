LastPass Pythonista
===================

**Original**: [lastpass-python][] (adapted for iOS - [Pythonista][])


Uses Pythonista to allow for pseudo x-callback-url functionality for LastPass. It downloads your LastPass vault and stores it in [Pythonista's keychain][]. You can then use Pythonista's powerful scripting coupled with an app such as [Launch Center Pro][] to make the LastPass iOS experience much more bearable.

**Note:** This does a one-way read-only sync from LastPass using an __unofficial__ API - if you want to manipulate your vault in any way (delete/edit) you must use the [LastPass iOS app][] (requires a LastPass Premium subscription - $12/yr).

There are 2 ways to import your accounts:

1. save the encrypted blob locally
2. save your accounts to the `keychain`

The advantage to using the encrypted blob is that you account are not saved to the `keychain`. Although the `keychain` is encrypted, there *may* be ways to access it from other apps. Please weigh the risks before using this. 

The advantage to using the `keychain` is that it is a bit faster and you are not prompted for the lastpass master credentials each time that the blob is opened. You should set [`keychain.set_master_password`][] for additional security.

By default `lpfinder.py` will look for `.lastpass.blob` first and fallback to the `keychain`. If you want to use the `keychain`, run the import again and choose "Save to keychain" when prompted. If you want to switch to the blob run the import again and choose "Don't Save to keychain".

See below for more.

### Installation:

* Using [filedownloader.py][], download and extract the zip of this repo:
    * Set URL to `https://codeload.github.com/HyShai/lastpass-pythonista/zip/master`.
    * Tap "Download"
    * When the Extract File alert appears, tap "OK".

Or

* Using <a href="https://github.com/transistor1/shellista">Shellista</a>, type the following commands:<br>
    `mkdir lastpass`<br>
    `cd lastpass`<br>
    `git clone https://github.com/HyShai/lastpass-pythonista.git`

Or

* Download the zip of this repo and sync to Dropbox.
* Download it to Pythonista using [DropboxFilePicker][] or [DropboxSync][].
* Unzip it using [Shellista][].

### Usage:

1. Import your accounts by running `lpimport_api.py`
2. To use it in an x-callback-url manner run `lpfinder.py` which takes 2 arguments - `account_name` and `redirect_url`
3. Tap the account for which you want the password 
4. The password will be copied to the clipboard and you will be redirected to the url/app that you passed in
4. Use `lpimport_api.py` to manually update your accounts (read-only)

If you want to use the encrypted blob, you can optionally save your lastpass master credentials to the `keychain` for convenience - **though this entails the same risk as above**. 

* Save your email as service=lastpass_email, account=lastpass, password={{your-email}}. 
* Save your password as service=lastpass_master, account=lastpass, password={{your-password}}. 
The names of the service and account are definite - see [lpfinder.py][] if you want to change them. See [keychain.set_password][]

An example Launch Center Pro action is here: https://launchcenterpro.com/q9qmfg 

Example
=======

<a href="https://www.youtube.com/watch?v=8WmbEWjLWbY" target="_blank"><img src="http://img.youtube.com/vi/8WmbEWjLWbY/0.jpg" alt="LP Example"></a> Tap this image to see how it works.

```python

```
Credits
=======

Credit for the vast majority of the reverse engineered LastPass API goes to [Dmitry Yakimenko][]

Credit for the Python version of the API goes to [konomae][]

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
  [Pythonista's keychain]:http://omz-software.com/pythonista/docs/ios/keychain.html
  [Dmitry Yakimenko]:https://github.com/detunized
  [filedownloader.py]:https://gist.github.com/elliospizzaman/89edf288a15fde45682a
  [keychain.set_password]:http://omz-software.com/pythonista/docs/ios/keychain.html#keychain.set_password
  [lpfinder.py]:https://github.com/HyShai/lastpass-pythonista/blob/master/lpfinder.py#L27
  [`keychain.set_master_password`]:http://omz-software.com/pythonista/docs/ios/keychain.html#keychain.set_master_password
