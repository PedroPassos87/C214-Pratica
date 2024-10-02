sudo apt-get install mailutils
echo "Pipeline executada!" | mail -s "Github Actions" ${secrets.EMAIL_NOTIFICACAO}