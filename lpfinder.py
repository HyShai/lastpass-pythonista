welcome_msg = '''This script takes 2 arguments:
1) the name of the account
2) the url to be redirected to
It works best with Launch Center Pro installed.
https://launchcenterpro.com/q9qmfg'''

import clipboard, console, keychain, sys, ui, webbrowser, os


try:
    _, account_name, redirect_url = sys.argv
    account_name = account_name.lower()

except ValueError:
    print(welcome_msg)
    sys.exit()


class AccountFinder(object):
    def __init__(self, blob=None):
        self.accounts = self.get_services(blob)
        self.has_blob = (True if blob else False)

    def get_services(self, blob=None):
        if blob and os.path.isfile(blob):
            import lastpass
            email = keychain.get_password('lastpass_email', 'lastpass')
            password = keychain.get_password('lastpass_master', 'lastpass') or ''
            email, password = console.login_alert('LastPass login', '', email, password)
            vault = lastpass.Vault.open_local(blob, email, password)
            return [(x.name, x.username, x.password) for x in vault.accounts]
        else:
            return keychain.get_services()

    def get_password(self, name, username):
        if self.has_blob:
            return next((x[2] for x in self.accounts if x[0] == name and x[1] == username), None)
        else:
            return keychain.get_password(name, username)

    def find_matching_accounts(self, account_name):
        return [(x[0] + ' - ' + x[1]) for x in self.accounts
            if account_name in x[0].lower()]


@ui.in_background
def item_selected(sender):
    acct = sender.items[sender.selected_row]['title'].split(' - ')
    pwd = account_finder.get_password(acct[0], acct[1])
    clipboard.set(pwd)
    account_finder_view.close()
    webbrowser.open(redirect_url)


@ui.in_background
def info_tapped(sender):
    row = sender.items[sender.tapped_accessory_row]
    console.alert(row['title'])


def make_tableview():
    tv = ui.TableView()
    tv.flex = 'WH'
    tv.name = 'tableview'
    return tv


def make_list(account_finder, account_name):
    ds = ui.ListDataSource({'title': x, 'accessory_type': 'detail_button'} for x in account_finder.find_matching_accounts(account_name))
    ds.action = item_selected
    ds.accessory_action = info_tapped
    return ds

FILENAME = os.path.join(os.getcwd(), '.lastpass.blob')
account_finder = AccountFinder(blob=FILENAME if os.path.exists(FILENAME)else None)
account_finder_view = ui.View()
account_finder_view.add_subview(make_tableview())

account_finder_view['tableview'].data_source = account_finder_view['tableview'].delegate = make_list(account_finder, account_name)

account_finder_view.present('fullscreen')
