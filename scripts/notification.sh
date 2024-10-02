import win32com.client as win32

outlook = win32.Dispatch('Outlook.Application')
message.outlook.CreateItem(0)
message.To = 'EMAIL_NOTIFICACAO'
message.Subject = 'Github Actions'
message.Body = 'Pipeline executado!'
message.Send()