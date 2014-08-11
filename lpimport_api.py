# Use with caution -- This saves the LastPass vault in the iOS keychain.
# Although the keychain is encrypted, I believe it is not 100% secure.
# At a minimum you probably should `keychain.set_master_password()`

import clipboard, console, keychain, lastpass, uuid, webbrowser

email = keychain.get_password('lastpass_email', 'lastpass') or ''
password = keychain.get_password('lastpass_master', 'lastpass') or ''
email, password = console.login_alert('LastPass login', '', email, password)
device = keychain.get_password('lastpass_uuid', 'lastpass')

try:
	blob = lastpass.Vault.fetch_blob(email, password, None, device)
except lastpass.LastPassIncorrectGoogleAuthenticatorCodeError as e:
	googleauth = None
	if not device:
		console.hud_alert(message='You will now be redirected to Google Authenticator',duration=1)
		webbrowser.open('otpauth:')
		console.hud_alert(message='Enter the 2FA code',duration=5.0)
		googleauth = console.input_alert('GoogleAuth', '', clipboard.get())
		trusted = console.alert('Trusted', 'Save this device as trusted?', 'Save', 'Don\'t Save', hide_cancel_button=True)
		if not trusted:
			device = str(uuid.uuid1())
			keychain.set_password('lastpass_uuid', 'lastpass', device)
	blob = lastpass.Vault.fetch_blob(email, password, googleauth, device)

save_vault = console.alert("Save to keychain", "Would you like to save your vault to the keychain?", "Don't Save", "Save", hide_cancel_button=True)
if not save_vault:
	save_blob = console.alert("Save blob local", "Would you like to save the encrypted blob locally?", "Don't Save", "Save", hide_cancel_button=True)
	if save_blob:
		import pickle, os
		print "Saving blob to .lastpass.blob"
		FILENAME = os.path.join(os.getcwd(),'.lastpass.blob')
		pickle.dump(blob, open(FILENAME,'wb'))
		console.hud_alert('Saved blob')
else:
	try:
		# don't want both the blob and the keychain - avoids conflicts
		import os
		os.remove('./.lastpass.blob')
	except OSError:
		pass
	vault = lastpass.Vault.open(blob,email,password)
	for i in vault.accounts:
		print 'Importing {} - {}'.format(i.name, i.username)
		keychain.set_password(i.name, i.username, i.password)

	console.hud_alert('Import done')