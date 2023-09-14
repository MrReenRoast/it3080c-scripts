function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}
function getUSER{
    (Get-LocalUser).Name | Select-String "Administrator"
}
function getHOST{
    hostname
}
function getDATE{
    Get-Date -Format "dddd MM/dd/yyyy"
}
$IP = getIP
$USER = getUSER
$HOSTNAME = getHOST
$VERSION = $HOST.Version.Major
$DATE = getDATE
$BODY = Write-Host("This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. PowerShell Version $VERSION. Today's Date is $DATE.")
Send-MailMessage -To "roferr@mail.uc.edu" -From "somesoobstuufwithreasons@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSsl -Credential (Get-Credential)