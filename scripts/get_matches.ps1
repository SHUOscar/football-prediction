$headers = @{'X-Auth-Token' = 'e696f25aa2a54c4bbea8bb4e7e6e671d'}
$url = 'https://api.football-data.org/v4/matches?dateFrom=2026-02-28&dateTo=2026-02-28'
Invoke-RestMethod -Uri $url -Headers $headers
