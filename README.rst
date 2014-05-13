LastPass Python API (adapted for iOS - Pythonista)
===================

:Original: `lastpass-python <https://github.com/konomae/lastpass-python>`_

**This is unofficial LastPass API**

Example
-------

::

    # coding: utf-8
    import lastpass

    vault = lastpass.Vault.open_remote(username, password)
    for i in vault.accounts:
        print i.id, i.username, i.password, i.url


License
-------

`The MIT License <http://opensource.org/licenses/mit-license.php>`_

