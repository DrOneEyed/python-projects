Param( [String]$Att,
       [String]$subj,
       [String]$Body
    )
Function Send-EMail
{
    Param( [Parameter(`
            Mandatory=$true)]
           [String]$To,
                [Parameter(`
                Mandatory=$true)]
            [String]$From,
                [Parameter(`
                Mandatory=$true)]
            [String]$Password,
                [Parameter(`
                Mandatory=$true)]
            [String]$Subject,
                [Parameter(`
                Mandatory=$true)]
            [String]$Body,
                [Parameter(`
                Mandatory=$true)]
            [String]$attachment
            )
try
{
    $Msg = New-Object System.Net.MAil.MailMessage($From, $To, $Subject, $Body)
    $Srv ="smpt.gmail.com"
    if($attachment -ne $null)
    {
        try
        {
            $Attachments =$attachment -split("\:\:");
            ForEach($val in $Attachments)
            {
                $attch= New-Object System.Net.Mail.Attachment($val)
                $Msg.Attachments.add($attch)
            }
        }
        catch
        {
            exit 2;
        }
        $client = New-Object Net.Mail.Smtpclient($Srv,587)
        $client.EnableSsl = $true
        $client.Credentials =New-Object System.Net.NetworkCredential($From.Split("@")[0], $Password);
        $client.send($Msg)
        Remove-Variable -Name client
        Remove-Variable -Name Password
        exit 7;
    }
}
catch
    {
        exit 3;
    }
}

try
{
    Send-EMail
        -attachment $Att
        -To "Address"
        -Body $Body
        -Subject $Subj
        -password "gg"
        -From "Address from"
}
catch
{
    exit 4;
}