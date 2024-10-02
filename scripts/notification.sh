sudo apt-get install mailutils
echo "Pipeline executada!" | mail -s "Github Actions" ${{vars.EMAIL}}