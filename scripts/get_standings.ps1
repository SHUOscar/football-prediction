# Get standings for La Liga
$result = Invoke-RestMethod -Uri 'https://api.football-data.org/v4/competitions/PD/standings' -Headers @{'X-Auth-Token'='e696f25aa2a54c4bbea8bb4e7e6e671d'}
$result | ConvertTo-Json -Depth 5 | Out-File -FilePath "C:\Users\28354\.openclaw\workspace\standings.json" -Encoding UTF8
