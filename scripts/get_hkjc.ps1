$response = Invoke-WebRequest -Uri 'https://bet.hkjc.com/ch/football/odds/odds_all.aspx' -UserAgent 'Mozilla/5.0' -TimeoutSec 30
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Write-Output $response.Content
