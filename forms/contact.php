<?php
$to = "me@example.com";
$from = $_POST['email'] ; 

$headers = "From: " .  $_POST['name'];

$subject = $_POST['subject'];
$body = "FeedBack:  " .$_POST['message'];
if( filter_var($_POST['email'], FILTER_VALIDATE_EMAIL) )
{
if (mail($to, $subject, $body, $headers, "-f " . $from))
{
echo 'Your Feedback from (' . $_POST['email'] . ') email has been sent wait for reply !';
}
else
{
echo 'There was a problem with your e-mail (' . $_POST['email'] . ')';
}
}
?>


