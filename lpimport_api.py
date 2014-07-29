# this saves the LastPass vault to the iOS keychain
# from my understanding - although the keychain is encrypted
# it is not 100% secure
# so use with caution
# at a minimum you should `keychain.set_master_password()`

import lastpass
import keychain
import console
import webbrowser
import uuid
import clipboard

def xstr(s):
    return '' if s is None else str(s)

email = xstr(keychain.get_password('lastpass_email', 'lastpass'))

password = xstr(keychain.get_password('lastpass_master', 'lastpass'))

email,password = console.login_alert('LastPass login', '', email, password)

device = keychain.get_password('lastpass_uuid', 'lastpass')

try:
    vault = lastpass.Vault.open_remote(email, password, None, device)
    
except lastpass.LastPassIncorrectGoogleAuthenticatorCodeError as e:

    googleauth = None
    if device is None:
        webbrowser.open('otpauth:')
        googleauth = console.input_alert('GoogleAuth', '', clipboard.get())
        trusted = console.alert('Trusted', 'Save this device as trusted?', 'Save', 'Don\'t Save', hide_cancel_button=True)
        if trusted == 0:
            device = str(uuid.uuid1())
            keychain.set_password('lastpass_uuid', 'lastpass', device)

    vault = lastpass.Vault.open_remote(email, password, googleauth, device)

for i in vault.accounts:
    print 'Importing {} - {}'.format(i.name, i.username)
    keychain.set_password(i.name, i.username, i.password)

print 'Import done'