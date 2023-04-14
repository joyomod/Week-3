--  1
CREATE TABLE movie_info (
  Movie_ID INT NOT NULL AUTO_INCREMENT,
  Movie_Name VARCHAR(255) NOT NULL,
  Movie_Length INT NOT NULL,
  Age_Rating VARCHAR(10) NOT NULL,
  PRIMARY KEY (Movie_ID)
);

-- 2
CREATE TABLE screens (
  Screen_ID INT NOT NULL AUTO_INCREMENT,
  Four_K BOOLEAN NOT NULL,
  PRIMARY KEY (Screen_ID)
);

-- 3
CREATE TABLE showings (
  Showing_ID INT NOT NULL AUTO_INCREMENT,
  Movie_ID INT NOT NULL,
  Screen_ID INT NOT NULL,
  Start_Time DATETIME NOT NULL,
  Available_Seats INT NOT NULL,
  PRIMARY KEY (Showing_ID),
  FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
  FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID)
);

-- 4
SELECT movie_info.movie_name, showings.start_time FROM movie_info
INNER JOIN showings ON movie_info.movie_ID = showings.movie_ID
WHERE showings.available_seats > 0 AND showings.start_time > '12:00'
ORDER BY showings.start_time;

-- 5
SELECT movie_info.movie_name FROM movie_info
INNER JOIN showings ON movie_info.movie_ID = showings.movie_ID
GROUP BY movie_info.movie_name
ORDER BY COUNT(*) DESC
LIMIT 1;






