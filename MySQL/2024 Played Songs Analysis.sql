USE song;

## 1. Songs that an user has played recently

SELECT
    h.played_at,
    s.title AS song_title
FROM 
	history AS h INNER JOIN songs AS s 
    ON h.song_id = s.id
WHERE h.user_id = 1
ORDER BY h.played_at DESC 
LIMIT 20;

## 2. All albums that were released in 2024

SELECT
	al.id AS album_id, 
	al.title AS album_title,
    al.release_date AS album_release_date,
    ar.name AS artist_name
FROM 
	albums AS al INNER JOIN artists AS ar
    ON al.artist_id = ar.id
WHERE 
	year(al.release_date) = 2024
ORDER BY
	al.release_date DESC;
    
## 3. Artists who released albums in 2024 in order of the number of albums

SELECT
	ar.name AS artist_name,
    COUNT(ar.name) AS album_count
FROM
	albums AS al INNER JOIN artists AS ar
    ON al.artist_id = ar.id
WHERE 
	YEAR(al.release_date) = 2024
GROUP BY
	ar.name
ORDER BY
	album_count DESC, ar.name ASC;
    
## 4. Songs that were most popular in 2024

SELECT
	s.title AS song_title,
	COUNT(s.title) AS play_count
FROM
	songs AS s INNER JOIN history AS hi
    ON s.id = hi.song_id
WHERE
	YEAR(hi.played_at) = 2024
GROUP BY 
	s.title
ORDER BY 
	play_count DESC, song_title ASC
LIMIT 20;

## 5. New artists who a specific user found in 2024 (exclude artists in 2023)

SELECT 
	DISTINCT 
    ar.id AS artist_id,
    ar.name AS artist_name
FROM 
	history AS h INNER JOIN songs AS s 
    ON h.song_id = s.id 
	INNER JOIN albums AS al 
    ON s.album_id = al.id
	INNER JOIN artists AS ar 
    ON al.artist_id = ar.id
WHERE h.user_id = 1 
  AND YEAR(h.played_at) = 2024
  AND ar.id NOT IN (
      SELECT 
		DISTINCT 
        ar_sub.id
      FROM 
		history AS h_sub INNER JOIN songs AS s_sub
        ON h_sub.song_id = s_sub.id
		INNER JOIN albums AS al_sub 
        ON s_sub.album_id = al_sub.id
		INNER JOIN artists AS ar_sub 
        ON al_sub.artist_id = ar_sub.id
      WHERE 
		h_sub.user_id = 1 AND 
        YEAR(h_sub.played_at) < 2024
  )
ORDER BY 
	ar.name ASC;

## 6. The percentage of music listened to by a specific user for each day of the week

SELECT 
    DAYNAME(h.played_at) AS day_of_week,
    COUNT(h.id) AS play_count,
    ROUND(
        COUNT(h.id) * 100.0 / (
            SELECT 
				COUNT(*) 
            FROM 
				history AS h_total
            WHERE 
				h_total.user_id = 1
        ), 2
    ) AS percentage
FROM 
	history AS h
WHERE 
	h.user_id = 1 
GROUP BY 
	day_of_week 
ORDER BY 
	FIELD(
    day_of_week,
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
); 
