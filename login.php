<?php
if(isset($_POST['password'])) {
    $password = $_POST['password'];

    if($password == '123456') {
        header('Location: https://example.com/');
        exit();
    } else {
        header('Location: login.html');
        exit();
    }
} else {
    header('Location: login.html');
    exit();
}
?>
