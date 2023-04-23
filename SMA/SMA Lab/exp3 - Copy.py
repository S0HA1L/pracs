from instagramy import InstagramUser
user = InstagramUser("Myntra")
print(f"Username: {user.fullname}")
print(f"Biography: {user.biography}")
print(f"Verified User: {user.is_verified}")
print(f"Website: {user.website}")
print(f"Followers: {user.number_of_followers}")
print(f"Following: {user.number_of_followings}")
print(f"No. Of Posts: {user.number_of_posts}")
posts = user.posts
print(posts[0])
instaPosts = []
for i in range(10):
    post = {}
    post["Likes"] = posts[i].likes
    post["Comments"] = posts[i].comments
    post["post_source"] = posts[i].post_source
    post["post_url"] = posts[i].post_url
    post["time"] = posts[i].taken_at_timestamp
    instaPosts.append(post)
insta_df = pd.DataFrame(instaPosts)
insta_df.info()
print(insta_df.isna())
print(f"Latest posts:\n {insta_df}")