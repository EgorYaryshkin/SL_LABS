1. whoami >> files/1_info.txt
  lab4_report pwd >> files/1_info.txt
  lab4_report uname -a >> files/1_info.txt 
2. echo "Text" > ~/secret.txt
3. chmod go-rw ~/secret.txt
4. cat ~/secret.txt > files/secret_backup.md
5. chmod 755 files/secret_backup.md
6. mv ~/secret.txt files/
7. sudo chown root files/secret_backup.md
8. ls /etc/host* > files/8_etc_hosts.txt
9. find /var/log/ -type f -mtime -7 > files/9_recent_logs.txt
10. sudo useradd -m -s /bin/bash auditor
11. sudo usermod -aG sudo auditor
12. sudo passwd auditor
13. echo "audit report" > /home/auditor/audit_report.txt
chmod a+rw /home/auditor/audit_report.txt
14. exit
sudo cp /home/auditor/audit_report.txt files/14_audit_report.txt
15. sudo userdel -r auditor
16. cat /etc/passwd > files/16_users.txt
17. sudo grep -rl "localhost" /etc/ > files/17_localhost_files.txt
18. find /usr/bin/ -type f -executable -user root > files/18_root_binaries.txt
19. find ~/ -type f -size +1M > files/19_large_files.txt
20. mkdir -p test_search
echo "port=8080" > test_search/data1.conf
echo "debug=true" > test_search/data2.conf
touch test_search/readme.txt
21. grep -rlE "port|debug" test_search/ > files/21_config_files.txt
22. find test_search/ -type f -empty -delete 
23. sleep 1h &
24. ps -u $(whoami) > files/24_my_processes.txt
25. pkill sleep
26. htop
27. ps aux | grep systemd > files/27_systemd_processes.txt
28. sudo tail -20 /var/log/syslog > files/28_syslog_tail.txt
29. grep -i "failed" /var/log/auth.log > files/29_failed_logins.txt
30. grep -i "failed" /var/log/auth.log > files/29_failed_logins.txt
31. ss -tuln > files/31_open_ports.txt
32. tar -czf lab4_files_backup.tar.gz files/
33. rm -rf files/
  lab4_report tar -xzf lab4_files_backup.tar.gz 
34. cp -r lab4_report lab4_final
35. rm -rf lab4_final
36. tree lab4_report/ > lab4_report/files/36_tree.txt
37. mkdir -p Lab04
38
