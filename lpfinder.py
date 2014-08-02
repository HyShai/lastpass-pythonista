welcome_msg = '''This script takes 2 arguments:
1) the name of the account
2) the url to be redirected to
It works best with Launch Center Pro installed.
https://launchcenterpro.com/q9qmfg'''

import clipboard, console, keychain, sys, ui, webbrowser

try:
    _, account_name, redirect_url = sys.argv
    account_name = account_name.lower()
except ValueError:
    print(welcome_msg)
    sys.exit()

@ui.in_background
def item_selected(sender):
    acct = sender.items[sender.selected_row]['title'].split(' - ')
    pwd = keychain.get_password(acct[0],acct[1])
    clipboard.set(pwd)
    picker.close()
    webbrowser.open(redirect_url)

@ui.in_background
def info_tapped(sender):
    row = sender.items[sender.tapped_accessory_row]
    console.alert(row['title'])

services = [ (x[0] + ' - ' + x[1]) for x in keychain.get_services()
                                    if account_name in x[0].lower() ]
ds = ui.ListDataSource({'title':x,'accessory_type':'detail_button'} for x in services)
ds.action= item_selected
ds.accessory_action = info_tapped

picker = ui.load_view('lpfinder')
table = picker.subviews[0]
table.data_source = table.delegate = ds

picker.present('sheet')
