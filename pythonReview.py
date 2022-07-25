def create_youtube_video(title, description):
	IshowSpeed = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments":{}}
	return IshowSpeed

title = input("What is your title? ")
description = input("what is your youtube video description? ")


new_youtube_video = create_youtube_video(title, description)
print(new_youtube_video)

def dislike(IshowSpeed):
	IshowSpeed["likes"] += 1
	return IshowSpeed

def add_comment(IshowSpeed):
	username = input("what is your name?")
	comment_text = input("pls give a comment")
	IshowSpeed["comments"][username] = comment_text
	return IshowSpeed

def add_likes(IshowSpeed):
	IshowSpeed["likes"] += 1
	return IshowSpeed

print(IshowSpeed)