# Use with caution -- This saves the LastPass vault in the iOS keychain.
# Although the keychain is encrypted, I believe it is not 100% secure.
# At a minimum you probably should `keychain.set_master_password()`
 
import clipboard, console, keychain, lastpass, uuid, webbrowser

email = keychain.get_password('lastpass_email', 'lastpass') or ''
password = keychain.get_password('lastpass_master', 'lastpass') or ''
email, password = console.login_alert('LastPass login', '', email, password)
device = keychain.get_password('lastpass_uuid', 'lastpass')

try:
    vault = lastpass.Vault.open_remote(email, password, None, device)
except lastpass.LastPassIncorrectGoogleAuthenticatorCodeError as e:
    googleauth = None
    if not device:
        webbrowser.open('otpauth:')
        googleauth = console.input_alert('GoogleAuth', '', clipboard.get())
        trusted = console.alert('Trusted', 'Save this device as trusted?', 'Save', 'Don\'t Save', hide_cancel_button=True)
        if not trusted:
            device = str(uuid.uuid1())
            keychain.set_password('lastpass_uuid', 'lastpass', device)
    vault = lastpass.Vault.open_remote(email, password, googleauth, device)

for i in vault.accounts:
    print 'Importing {} - {}'.format(i.name, i.username)
    keychain.set_password(i.name, i.username, i.password)

print 'Import done'
