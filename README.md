# RSYSLOGVIEWER #

`rsyslogviewer` is a simple application for monitoring and search events through log collected in a database. It can be mysql-server or postgresql-server. `rsyslog` know how to write events to both of them. But in case of postgre, you have to change name of tables and fields in `log/models.py to lowercase.

## Installation and configuration ##

To install rsyslogviewer take a few steps:

1. Install python, Django, MySQL-phyton (python-psycopg2).
2. Clone [rsyslogviewer](https://github.com/exegoist/rsyslogviewer/)`git clone https://github.com/exegoist/rsyslogviewer.git` to your server.
3. Provide you credentials to connect to database in `rsyslogviewer/settings.py`. 
4. Run manage.py syncdb ( After this step, tables 'Facilities' and 'Priorities' will be created. You must populate them with data in next step)
5. Run inserts:
``` sql
   INSERT INTO `facilities` (`id`, `facility`) VALUES
(0, 'kernel'),
(1, 'user-level'),
(2, 'mail'),
(3, 'system daemons'),
(4, 'security/authorization'),
(5, 'messages generated'),
(6, 'line printer subsystem'),
(7, 'network news subsystem'),
(8, 'UUCP subsystem'),
(9, 'clock daemon'),
(10, 'security/authorization'),
(11, 'FTP daemon'),
(12, 'NTP subsystem'),
(13, 'log audit'),
(14, 'log alert'),
(15, 'clock daemon'),
(16, 'local0'),
(17, 'local1'),
(18, 'Local2'),
(19, 'local3'),
(20, 'local4'),
(21, 'local5'),
(22, 'local6'),
(23, 'local7');

    INSERT INTO `priorites` (`num`, `severity`) VALUES
(0, 'Emergency'),
(1, 'Alert'),
(4, 'Warning'),
(2, 'Critical'),
(3, 'Error'),
(5, 'Notice'),
(6, 'Informational'),
(7, 'Debug');
```
7. Configure your web-server to handle `rsyslogviewer` and fire up!
