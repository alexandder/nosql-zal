SELECT data->>'lang' as Language, COUNT(*) as Quantity FROM subreddits GROUP BY data->>'lang' ORDER BY Quantity DESC LIMIT 10;