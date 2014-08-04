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
            email = keychain.get_password('lastpass_email', 'lastpass') or ''
            password = keychain.get_password('lastpass_master', 'lastpass') or ''
            email, password = console.login_alert('LastPass login', '', email, password)
            return [(x.name, x.username, x.password) for x in lastpass.Vault.open_local(blob)]
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


class AccountFinderView (ui.View):
    def __init__(self):
        FILENAME = os.path.join(os.getcwd(), '.lastpass.blob')
        self.AccountFinder = AccountFinder(blob=FILENAME if os.path.exists(FILENAME)else None)
        ds = ui.ListDataSource({'title':x, 'accessory_type':'detail_button'} for x in self.AccountFinder.find_matching_accounts(account_name))
        ds.action = self.item_selected
        ds.accessory_action = self.info_tapped
        tv = ui.TableView()
        tv.frame = self.bounds
        tv.flex = 'WH'
        tv.data_source = tv.delegate = ds

        self.add_subview(tv)

    @ui.in_background
    def item_selected(self, sender):
        acct = sender.items[sender.selected_row]['title'].split(' - ')
        self.close()
        # there's a bug here - keychain.master_password hangs the ui even though @ui.in_background
        pwd = self.AccountFinder.get_password(acct[0], acct[1])    
        clipboard.set(pwd)
        webbrowser.open(redirect_url)

    @ui.in_background
    def info_tapped(self, sender):
        row = sender.items[sender.tapped_accessory_row]
        console.alert(row['title'])


account_finder_view = AccountFinderView()
account_finder_view.present('sheet')
