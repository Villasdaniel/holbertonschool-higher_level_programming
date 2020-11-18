-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
