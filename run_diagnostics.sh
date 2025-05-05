echo -e "\nRunning diagnostics...\n"

echo -e "\nTesting nginx configuration file [sudo nginx -t]..."
sudo nginx -t

echo -e "\nFinding nginx log files from the last 1 day..."
find /var/log/nginx/ -maxdepth 1 -mtime -1 -printf "%T+ %p\n" | sort
echo -e "Note: NGINX maintains two main types of logs:\n  Access Logs – Capture details of all incoming requests\n  Error Logs – Record server-side errors and issues"

echo -e "\nPrinting tails of nginx access.log and error.log files..."
echo -e "\n  /var/log/nginx/access.log:"
tail -n 5 /var/log/nginx/access.log
echo -e "\n  /var/log/nginx/error.log:"
tail -n 5 /var/log/nginx/error.log

echo -e "\nChecking systemd status of gunicorn [sudo systemctl status gunicorn]..."
sudo systemctl status --no-pager gunicorn

echo -e "\nSearching for gunicorn processes [ps aux | grep gunicorn]..."
ps aux | grep gunicorn

echo -e "\nChecking gunicorn logs [sudo journalctl -e -u gunicorn | tail]..."
sudo journalctl -e -u gunicorn | tail -n 5

echo -e "\nChecking systemd status of PostgreSQL database [sudo systemctl status postgresql]..."
sudo systemctl status --no-pager postgresql

echo -e "done."


