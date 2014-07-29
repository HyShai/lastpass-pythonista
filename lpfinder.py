# this takes 2 arguments
# 1) the name of the account
# 2) the url to be redirected to
# best if used with Launch Center Pro
# https://launchcenterpro.com/fm4lxb

from sys import argv
import keychain
import webbrowser
import ui
import clipboard
import console
services = keychain.get_services()

@ui.in_background
def item_selected(sender):
	acct = sender.items[sender.selected_row]['title'].split(' - ')
	pwd = keychain.get_password(acct[0],acct[1])
	clipboard.set(pwd)
	picker.close()
	webbrowser.open(argv[2])

@ui.in_background
def info_tapped(sender):
	row = sender.items[sender.tapped_accessory_row]
	console.alert(row['title'])
ds = ui.ListDataSource({'title':(x[0] +' - '+ x[1]),'accessory_type':'detail_button'} for x in services if argv[1].lower() in x[0].lower())
ds.action= item_selected
ds.accessory_action = info_tapped

picker = ui.load_view('lpfinder')
table = picker.subviews[0]
table.data_source = ds
table.delegate = ds

picker.present('sheet')