SELECT users.first_name,users.last_name,users2.first_name AS friend_first_name, users2.last_name AS friend_lastname FROM Friendships.users 
LEFT JOIN Friendships.friendships ON friendships.user_id1 = users.id 
LEFT JOIN Friendships.users as users2 ON friendships.friend_id = users2.id ;