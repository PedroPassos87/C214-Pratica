#!/bin/bash

RECIPIENT="$EMAIL_NOTIFICACAO"

if [ -z "$RECIPIENT" ]; then
  echo "A variável de ambiente EMAIL_NOTIFICACAO não está definida."
  exit 1
fi


echo "Pipeline executado!" | mail -s "Github Actions" "$RECIPIENT"