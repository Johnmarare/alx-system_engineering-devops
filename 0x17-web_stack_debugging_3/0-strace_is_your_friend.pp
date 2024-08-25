# A puppet code that fixes a wordpress site 5xx error to 200 OK
# editing the mistyped php from phpp in the /var/www/html/wp-settings.php

exec { 'fix-wordpress-server-error':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',    path    => '/usr/bin:/bin',
}
