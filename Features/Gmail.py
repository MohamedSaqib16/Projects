import imapclient
import pyzmail

# connect to the Thunderbird mailbox
imap_obj = imapclient.IMAPClient('imap.example.com')

# login with credentials
imap_obj.login('username', 'password')

# select a folder (e.g. inbox)
imap_obj.select_folder('INBOX')

# search for email messages
msg_ids = imap_obj.search(['ALL'])

# fetch email messages
for msg_id in msg_ids:
    raw_msg = imap_obj.fetch([msg_id], ['BODY[]', 'FLAGS'])
    msg = pyzmail.PyzMessage.factory(raw_msg[msg_id][b'BODY[]'])
    # print the subject and sender of the message
    print('Subject: ', msg.get_subject())
    print('From: ', msg.get_addresses('from')[0])
    print('----')

# logout from the mailbox
imap_obj.logout()
