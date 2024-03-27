-- Imports database dump from hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM hbtn_0d_tvshows INNER JOIN tv_show_genres = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
