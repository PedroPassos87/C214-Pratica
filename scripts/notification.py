import win32com.client as win32

# Cria uma instância do Outlook
outlook = win32.Dispatch('Outlook.Application')
message = outlook.CreateItem(0)  # Cria um novo item de mensagem
message.To = 'EMAIL_NOTIFICACAO'  # Aqui você precisa usar a variável de ambiente
message.Subject = 'GitHub Actions'
message.Body = 'Pipeline executado!'
message.Send()