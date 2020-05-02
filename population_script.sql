INSERT INTO game_gametype (name) VALUES('NES');
INSERT INTO game_gametype (name) VALUES('Commodore');
INSERT INTO game_gametype (name) VALUES('Playstation Classic');
INSERT INTO game_gametype (name) VALUES('Gameboy');
INSERT INTO game_gametype (name) VALUES('Sega');
INSERT INTO game_gametype (name) VALUES('Atari');

INSERT INTO game_game (name, description, type_id, price) VALUES('Pac Man', 'Some description for Pacman', 1, 4.99);
INSERT INTO game_game (name, description, type_id, price) VALUES('Bomberman', 'Some description for Bomberman', 1, 1.99);
INSERT INTO game_game (name, description, type_id, price) VALUES('Magical tree', 'Some description for Magical tree', 5, 2.99);
INSERT INTO game_game (name, description, type_id, price) VALUES('Super Mario Bros', 'Some description for Super Mario Bros', 1, 3.99);
INSERT INTO game_game (name, description, type_id, price) VALUES('Donkey Kong', 'Some description for Donkey Kong', 6, 45.99);
INSERT INTO game_game (name, description, type_id, price) VALUES('Wonderboy', 'Some description for Wonderboy', 1, 100.99);
INSERT INTO game_game (name, description, type_id, price) VALUES('Mortal Kombat', 'Some description for Mortal Kombat', 2, 12.99);
INSERT INTO game_game (name, description, type_id, price) VALUES('Pokemon', 'Some description for Pokemon', 4, 13.99);
INSERT INTO game_game (name, description, type_id, price) VALUES('Sonic the hedgehog', 'Some description for Sonic', 5, 15.99);
INSERT INTO game_game (name, description, type_id, price) VALUES('Crash Bandicoot', 'Some description for Crash Bandicoot', 2, 15.99);
 
INSERT INTO game_gameimage (image, game_id) VALUES('https://androidapksdl.com/wp-content/uploads/2020/03/PAC-MAN-8.0.1-MODs-APK.png', 1);
INSERT INTO game_gameimage (image, game_id) VALUES('https://vignette.wikia.nocookie.net/bomberman/images/8/83/WhiteBomber_Vector01.png/', 2);
INSERT INTO game_gameimage (image, game_id) VALUES('https://media.classic-retro-games.com/51/magical_tree_remake_02.png', 3);
INSERT INTO game_gameimage (image, game_id) VALUES('https://upload.wikimedia.org/wikipedia/en/0/03/Super_Mario_Bros._box.png', 4);
INSERT INTO game_gameimage (image, game_id) VALUES('https://www.funstockretro.co.uk/news/wp-content/uploads/2018/09/donkey-kong.jpg', 5);
INSERT INTO game_gameimage (image, game_id) VALUES('https://images.igdb.com/igdb/image/upload/t_screenshot_huge/lqp1u43k8slq5egjqtzq.jpg', 6);
INSERT INTO game_gameimage (image, game_id) VALUES('https://miro.medium.com/max/436/1*yCcDd9AKlPH6mtWl9zuc-A.jpeg', 7);
INSERT INTO game_gameimage (image, game_id) VALUES('https://4.bp.blogspot.com/-KWrxAceUth4/UR-_DdGk82I/AAAAAAAAAgw/y6Bz4nCV1OY/s1600/27.png', 8);
INSERT INTO game_gameimage (image, game_id) VALUES('https://thetudedude.com/wp-content/uploads/2018/06/Sonic-the-Hedgehog-1.jpg', 9);
INSERT INTO game_gameimage (image, game_id) VALUES('https://www.lukiegames.com/assets/images/PS1/ps1_crash_bandicoot-120314.jpg', 10);

INSERT INTO user_user (email, username, password, profile_pic, has_address) VALUES('sindri@sindri.is', 'Sindri', '1234', 'https://townsquare.media/site/694/files/2019/01/GettyImages-868643608.jpg?w=980&q=75', FALSE);
INSERT INTO user_user (email, username, password, profile_pic, has_address) VALUES('hofi@sindri.is', 'Hofi', '12345', '', TRUE);
INSERT INTO user_user (email, username, password, profile_pic, has_address) VALUES('fannar@sindri.is', 'Fannar', '12347', FALSE);
INSERT INTO user_user (email, username, password, profile_pic, has_address) VALUES('fridrik@sindri.is', 'Fridrik', '12341', FALSE);

INSERT INTO user_userbilling (full_name, street_name, house_nr, postal_code, city, country, user_id) VALUES('Holmfridur Magnea Hakonardottir', 'Disaborgir', 4, 112, 'Reykjavik', 'Iceland', 2);