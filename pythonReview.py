title = input("What is your title? ")
description = input("what is your youtube video description? ")
num = 0
num1 = 0
def create_youtube_video(title, description):
	IshowSpeed = {"title": title, "description": description, "likes": num, "dislikes": num1, comments:{}}
	return IshowSpeed

new_youtube_video = create_youtube_video(title, description)
print(new_youtube_video)

def dislike(num1):
	num1 = num1 + 1
	return num1

def add_comment(comments):
	comments = {"username": comment_text}
	comment_text = input("pls give a comment")
	return comments

def add_likes(num):
	num = num + 495
	return num
