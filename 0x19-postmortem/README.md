On August 20th, 2024 at midnight the server access went down resulting in 504 error for anyone trying to access an e-commerce website. The website is based on wordpress tool and runs on LAMP stack.

	Timeline
00:00 PST - 500 error for anyone trying to access the website
00:05 PST - Ensuring Apache and MySQL are up and running.
00:10 PST - The website was not loading properly which on background check revealed that the server was working properly as well as the database.
00:12 PST - After quick restart to Apache server returned a status of 200 and OK while trying to curl the website.
00:18 PST - Reviewing error logs to check where the error might be coming from.
	Root Cause and Resolution
The issue was connected with a wrong file name being reffered to in the wp-settings.php file. The error was raised when trying to curl the server, wherein the server responded with 500 error. By checking the error logs it was found that no error log file was being created for the php errors and reading the default error log for apache did not result in much information regarding the premature closing of the server. Once understood that the errors for php logs were not being directed anywhere the engineer chose to review the error log setting for the php in the php.ini file and found that all error logging was turned off. Once turned on, the error logging the apache server was restarted to check if any errors were being registerd in the log. As suspected, the php log showed that a file with a .phpp extension was not found in the wp-settings.php file. This was clearly a misspelled error that resulted in the error to site access. As this was one server that the error was found in, this error might have been replicated in other servers as well. An easy fix by changing the file extension by puppet would result in the fix being made to other servers as well. A quick deployment of the puppet code replaced all misspelled file extensions with the right one and restarting of the server resulted in properly loading of the site and server.
	Corrective and Preventive Measures
All servers and sites should have error logging turned on to easily identify errors if anything goes wrong.
All servers and sites should be tested locally before deploying on a m
