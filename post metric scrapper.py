from instascrape import Post
import pandas as pd 

SESSIONID = ''

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
"cookie":f'sessionid={SESSIONID};'
}

#posts_data = [post.to_dict() for post in recent_posts]
#posts_df = pd.DataFrame(posts_data)
#print(posts_df[['upload_date', 'comments', 'likes']])

class Proj:
    def __init__(self, file_name):
        self.file_name = file_name
    post_list = ''
    likes = 0
    comments = 0
    video_view_count = 0

projects = {}
projects["panic_attack"] = Proj("panic_attack.txt")
projects["panic_attack"].post_list = [
    line.rstrip('\n') for line in open(projects["panic_attack"].file_name)
]

projects["mendai"] = Proj("mendai.txt")
projects["mendai"].post_list = [
    line.rstrip('\n') for line in open(projects["mendai"].file_name)
]

for proj_name in projects:

    for post in projects[proj_name].post_list:
        proj_post = Post(post)
        proj_post.scrape(headers=headers)
    #proj_data = proj_post.to_dict()
    #posts_df = pd.DataFrame(proj_data)
        print(proj_post['likes'], proj_post['comments'], proj_post['video_view_count'])
        projects[proj_name].likes += proj_post['likes']
        projects[proj_name].comments += proj_post['comments']
        if(proj_post['video_view_count'] == proj_post['video_view_count']): #check that its not NaN
            projects[proj_name].video_view_count += proj_post['video_view_count']
    #print(proj_post['likes'])
    #print(proj_post['video_view_count'])
        #proj_post['comments']
        #print(proj_post.embed())

    print(
        proj_name,
        projects[proj_name].likes, 
        projects[proj_name].comments, 
        projects[proj_name].video_view_count
    )
