def create_youtube_video(title, description):
	youtube_video_platform = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments":{}}
	return youtube_video_platform

title = input("What is your title? ")
description = input("what is your youtube video description? ")


new_youtube_video = create_youtube_video(title, description)
print(new_youtube_video)

def dislike(youtube_video):
	youtube_video["dislikes"] += 1
	return youtube_video

def add_comment(youtube_video):
	username = input("what is your name?")
	comment_text = input("pls give a comment")
	youtube_video["comments"][username] = comment_text
	return youtube_video

def add_likes(youtube_video):
	youtube_video["likes"] += 1
	return youtube_video

dislike(new_youtube_video)

for i in range(495):
	add_likes(new_youtube_video)

add_comment(new_youtube_video)

print(new_youtube_video)