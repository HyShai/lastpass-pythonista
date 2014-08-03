welcome_msg = '''This script takes 2 arguments:
1) the name of the account
2) the url to be redirected to
It works best with Launch Center Pro installed.
https://launchcenterpro.com/q9qmfg'''

import clipboard, console, keychain, sys, ui, webbrowser, os


try:
    _, account_name, redirect_url = sys.argv
    account_name = account_name.lower()
    # make a global to be able to access the decrypted blob in `item_selected`
    accounts_from_blob = None
except ValueError:
    print(welcome_msg)
    sys.exit()


class AccountFinder(object):
    def __init__(self, blob):
        self.accounts = get_services(blob)
        self.has_blob = (True if blob else False)

    def get_services(self, blob=None):
        if blob and os.path.isfile(blob):
            import lastpass
            email = keychain.get_password('lastpass_email', 'lastpass') or ''
            password = keychain.get_password('lastpass_master', 'lastpass') or ''
            email, password = console.login_alert('LastPass login', '', email, password)
            return [x.name, x.username, x.password
                        for x in lastpass.Vault.open_local(blob)]
        else:
            return keychain.get_services()

    def get_password(self, name, username):
        if self.has_blob:
            return next((x.password for x in self.accounts if x.name == name and x.username == username), None)
        else:
            return keychain.get_password(name, username)

    def find_matching_accounts(self, account_name):
        return [(x[0] + ' - ' + x[1]) for x in self.get_services()
                if account_name in x[0].lower()]




@ui.in_background
def item_selected(sender):
    acct = sender.items[sender.selected_row]['title'].split(' - ')
    # if using local blob
    if accounts_from_blob:
        # what's the pythonic way to do this?
        pwd = [x.password for x in accounts_from_blob if x.name.lower() == acct[0] and x.username == acct[1]][0]
    else:
        pwd = keychain.get_password(acct[0], acct[1])

    clipboard.set(pwd)
    picker.close()
    webbrowser.open(redirect_url)


@ui.in_background
def info_tapped(sender):
    row = sender.items[sender.tapped_accessory_row]
    console.alert(row['title'])


def get_services():
    if os.path.isfile('.lastpass.blob'):
        import lastpass
        email = keychain.get_password('lastpass_email', 'lastpass') or ''
        password = keychain.get_password('lastpass_master', 'lastpass') or ''
        email, password = console.login_alert('LastPass login', '', email, password)
        accounts_from_blob = lastpass.Vault.open_local('.lastpass.blob')
        # what's the pythonic way to do this?
        return [{x.name, x.username} for x in accounts_from_blob]
    else:
        return keychain.get_services()

matching_services = [(x[0] + ' - ' + x[1]) for x in get_services()
                                    if account_name in x[0].lower()]
ds = ui.ListDataSource({'title':x, 'accessory_type':'detail_button'} for x in matching_services)
ds.action = item_selected
ds.accessory_action = info_tapped

picker = ui.load_view('lpfinder')
table = picker.subviews[0]
table.data_source = table.delegate = ds

picker.present('sheet')