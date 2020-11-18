-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
