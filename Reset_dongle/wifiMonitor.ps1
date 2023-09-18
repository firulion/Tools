PowerShell -Command {exit} -WindowStyle Hidden	
    write "Script Wi-Fi Monitor"
	for (;;)

	{
		Start-Sleep -s 5
		$Stamp = (Get-Date).toString("yyyy/MM/dd HH:mm:ss")
		# Hostname 
		$env:computername
		write-Host "$Stamp"
		$ServerName = "www.google.com"

		if (test-Connection $ServerName -Count 2 -Quiet ) { 
			# write-Host "$ServerName success " -ForegroundColor Green
			Start-Sleep -s 5
		} 
		else{
			Write-Warning "$ServerName failed"
			Start-Sleep -s 2
			Disable-PnPDevice -InstanceID 'USB\VID_2357&PID_0109\00E04C000001' -A;
			Start-Sleep -s 30
			Enable-PnPDevice -InstanceID 'USB\VID_2357&PID_0109\00E04C000001' -A;
			Start-Sleep -s 30
			Start-Transcript -Append "C:\Script_wifi\$(gc env:computername).txt"
		}  
		cls			
	}