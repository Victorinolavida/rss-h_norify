from h_notify import *
import time
import pytz

default_token = '' # hypothesis api token for a user who is a member of all monitored groups
default_hook = '' # see https://YOUR_VANITY_NAME.slack.com/apps/manage/custom-integrations)


default_smtp_server = 'smtp.gmail.com' 
#default_email_sender = 'hypothesis.notifier@example.com'
default_email_sender = ''
default_email_password = ''

while True:
    try:
     

        notify_rss_group_activity(group='', groupname='', token=default_token, pickle='')

        # email recipes
        
        ########################################################################
         # MI CORREO
        ########################################################################
         

        notify_email_tag_activity(tag='', token=default_token, pickle='', smtp=default_smtp_server, sender=default_email_sender, sender_password=default_email_password, recipient='')
       


        print ( 'durmiendo.....' )
        time.sleep(60 * 30)  # wait 30 min to be polite to the hypothesis api
    except:
        print ( traceback.print_exc() )


