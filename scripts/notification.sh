#!/bin/bash

# Verifica se a variável de ambiente EMAIL_NOTIFICACAO está definida
if [ -z "$EMAIL_NOTIFICACAO" ]; then
    echo "Erro: A variável de ambiente EMAIL_NOTIFICACAO não está definida."
    exit 1
fi

# Executa o script Python para enviar o e-mail
python3 -c "
import win32com.client as win32

# Cria uma instância do Outlook
outlook = win32.Dispatch('Outlook.Application')
message = outlook.CreateItem(0)  # Cria um novo item de mensagem
message.To = '$EMAIL_NOTIFICACAO'  # Usa a variável de ambiente
message.Subject = 'GitHub Actions'
message.Body = 'Pipeline executado!'
message.Send()
"
