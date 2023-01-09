import openai
from flask import Flask,request
import mysql.connector

mydb = mysql.connector.connect(
host = "127.0.0.1",
user = "root",
# password = "password",
database = "artikleai",
port=3306,
# auth_plugin='mysql_native_password'
)

app = Flask(__name__)
key = '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'


Error_Code1={
    'Error_Code': 404,
    'Message': 'Envalid Api key'
}
recarge={
    'Error_Code': 403,
    'Message': 'Recharge Your Credit'
}
openai.api_key = key

def check_api_balance(api_key):
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT apikey FROM users WHERE apikey ='{0}'".format(api_key)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    if myresult:
        api_key = myresult[0]
        mycursor = mydb.cursor(buffered=True)
        sql = "SELECT postCreditBalance FROM users WHERE apikey ='{0}'".format(api_key)
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        postCreditBalance = myresult[0]
        return postCreditBalance
    else:
        return 'No Api keys ableable'

def postCreditBalanceUpdate(post_balance,api_key,count):
    final_bal = post_balance - count
    mycursor = mydb.cursor(buffered=True)
    sql = "UPDATE users SET postCreditBalance = '{0}'  WHERE apikey = '{1}' ".format(final_bal,api_key)
    mycursor.execute(sql)
    mydb.commit()

    
### Product decription 
### url == http://127.0.0.1:5000/Product-decription?product=***&description=***&api-key=***
@app.route("/Product-decription/")
def Product_decription():
    api_key= request.args.get("api-key")
    Product =request.args.get("product")
    Description =request.args.get("description")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
        
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Product names:{Product},\nProduct description: {Description}",
        temperature=0.3,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge
    
    


### Blog Selection Writing
### url == http://127.0.0.1:5000/blog-selection-writing?keyword=***&topic=***&api-key=***
@app.route("/blog-selection-writing/")
def blog_selection_writing():
    api_key= request.args.get("api-key")
    keyword =request.args.get("keyword")
    Topic =request.args.get("topic")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"For this keyword:{keyword},\n write blog Selection Details useing this text: {Topic}",
        temperature=0.3,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge
    

### Brand name 
### url == http://127.0.0.1:5000/brand-name?description=***&api-key=***
@app.route("/brand-name/")
def brand_name():
    api_key= request.args.get("api-key")
    decription = request.args.get("description")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create a brand name For this decription:{decription}",
        temperature=0.3,
        max_tokens=5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge
   


### url == http://127.0.0.1:5000/business-idea-pitch?idea=***&api-key=***
### Business idea Pitch 
@app.route("/business-idea-pitch/")
def business_idea_pitch ():
    api_key= request.args.get("api-key")
    idea = request.args.get("idea")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Business idea Pitch useing this idea:{idea}",
        temperature=0.3,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge
 

### url == http://127.0.0.1:5000/business-ideas?interest=***&skills=***&api-key=***
### Business ideas 
@app.route("/business-ideas/")
def business_ideas ():
    api_key= request.args.get("api-key")
    Interest = request.args.get("interest")
    skills = request.args.get("skills")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Business idea based on interested in :{Interest},\n And some skills are:{skills}",
        temperature=0.3,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/call-to-action?decription=***&api-key=***
### Call To Action 
@app.route("/call-to-action/")
def call_to_action ():
    api_key= request.args.get("api-key")
    decription = request.args.get("decription")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Call To Action useing this text:{decription}",
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/cover-letter?job_role=***&job_skills=***&api-key=***
### Cover Letter
@app.route("/cover-letter/")
def cover_letter ():
    api_key= request.args.get("api-key")
    job_role = request.args.get("job_role")
    job_skills = request.args.get("job_skills")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Cover Letter useing this job role:{job_role},\n Jobs skills are:{job_skills}",
        temperature=0.3,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/email?key_points=***&api-key=***
### Email
@app.route("/email/")
def email ():
    api_key= request.args.get("api-key")
    key_points =request.args.get("key_points")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write an email useing this key points:{key_points}",
        temperature=0.3,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/twitter-ads?product_name=***&description=***&api-key=***
### Twitter Ads
@app.route("/twitter-ads/")
def twitter_ads ():
    api_key= request.args.get("api-key")
    product_name = request.args.get("product_name")
    Description =request.args.get("description")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create twitter ads description for this product:{product_name},\n Use this description:{Description}",
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/facebook-ads?product_name=***&description=***&api-key=***
### Facebook ads
@app.route("/facebook-ads/")
def facebook_ads ():
    api_key= request.args.get("api-key")
    product_name = request.args.get("product_name")
    Description = request.args.get("description")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create facebook ads description for this product:{product_name},\n Use this description:{Description}",
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/linkedin_ads?product-name=***&description=***&api-key=***
### linkedin Ads
@app.route("/linkedin-ads/")
def linkedin_ads ():
    api_key= request.args.get("api-key")
    product_name = request.args.get("product_name")
    Description = request.args.get("description")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create linkedin ads description for this product:{product_name},\n Use this description:{Description}",
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge

### url == http://127.0.0.1:5000/google-search-ads?product_name=***&description=***&api-key=***
### Google Search Ads
@app.route("/google-search-ads/")
def google_search_ads ():
    api_key= request.args.get("api-key")
    product_name = request.args.get("product_name")
    Description = request.args.get("description")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Google Search ads description for this product:{product_name},\n Use this description:{Description}",
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/interview-questions?interview_bio=***&interview_context=***&api-key=***
### Interview Questions 
@app.route("/interview-questions/")
def interview_questions  ():
    api_key= request.args.get("api-key")
    Interview_bio = request.args.get("interview_bio")
    Interview_context = request.args.get("interview_context")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Interview Questions, interviewer bio is:{Interview_bio},\n Use this Interview context:{Interview_context}",
        temperature=0.3,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/job-description?Job_role=***&api-key=***
### Job Description
@app.route("/job-description/")
def job_description  ():
    api_key= request.args.get("api-key")
    Job_role  =request.args.get("Job_role")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Job Description and Job role is:{Job_role}",
        temperature=0.3,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/post-caption-ideas?Post_topic=***&api-key=***
### Post & Caption Ideas 
@app.route("/post-caption-ideas/")
def post_caption_ideas  ():
    api_key= request.args.get("api-key")
    Post_topic=request.args.get("Post_topic")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Post & Caption Ideas for this post:{Post_topic}",
        temperature=0.3,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge

### url == http://127.0.0.1:5000/profile-bio?about_you=***&api-key=***
### Profile Bio 
@app.route("/profile-bio/")
def profile_bio():
    api_key= request.args.get("api-key")
    About_you= request.args.get("about_you")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Profile Bio for this text:{About_you}",
        temperature=0.3,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/question-answer?topic_description=***&api-key=***
### Question & Answer 
@app.route("/question-answer/")
def question_answer():
    api_key= request.args.get("api-key")
    Topic_description= request.args.get("topic_description")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Question & Answer for this text:{Topic_description}",
        temperature=0.3,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/seo-meta-description?page_meta_title=***&api-key=***
### SEO Meta Description
@app.route("/seo-meta-description/")
def seo_meta_description():
    api_key= request.args.get("api-key")
    Page_meta_title= request.args.get("page_meta_title")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create SEO Meta Description for Page meta title:{Page_meta_title}",
        temperature=0.3,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/seo_meta-title?target_keywords=***&api-key=***
### SEO Meta Title
@app.route("/seo_meta-title/")
def seo_meta_title():
    api_key= request.args.get("api-key")
    Target_keywords= request.args.get("target_keywords")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create SEO Meta Title for Target keywords:{Target_keywords}",
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/story-plot?story_Idea=***&api-key=***
### Story Plot
@app.route("/story-plot/")
def story_plot():
    api_key= request.args.get("api-key")
    Story_Idea=request.args.get("story_Idea")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Story Plot and  Story Idea is:{Story_Idea}",
        temperature=0.3,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/tagline-headline?description=***&api-key=***
### Tagline & Headline 
@app.route("/tagline-headline/")
def tagline_headline ():
    api_key= request.args.get("api-key")
    Description=request.args.get("description")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Tagline & Headline and Description is :{Description}",
        temperature=0.3,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/testimonial-review?name=***&review_title=***&api-key=***
### Testimonial & Review
@app.route("/testimonial-review/")
def testimonial_review():
    api_key= request.args.get("api-key")
    Name= request.args.get("name")
    Review_Title = request.args.get("review_title")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Testimonial & Review for :{Name},\n Review Title is :{Review_Title}" ,
        temperature=0.3,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/video-channel-description?Channel_purpose=***&api-key=***
### Video Channel Description ## Channel purpose
@app.route("/video-channel-description/")
def video_channel_description():
    api_key= request.args.get("api-key")
    Channel_purpose= request.args.get("Channel_purpose")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Video Channel Description for Channel purpose:{Channel_purpose}" ,
        temperature=0.3,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/video-description?video_title=***&api-key=***
### Video Description
@app.route("/video-description/")
def video_description():
    api_key= request.args.get("api-key")
    Video_title= request.args.get("video_title")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Video Description and Video title is:{Video_title}" ,
        temperature=0.3,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


### url == http://127.0.0.1:5000/video-idea?keywords=***&api-key=***
### Video Idea
@app.route("/video-idea/")
def video_idea():
    api_key= request.args.get("api-key")
    Keywords=request.args.get("keywords")
    post_balance = check_api_balance(api_key)
    try:
        post_balance = int(post_balance)
    except:
        post_balance = post_balance
        return Error_Code1
    if post_balance >= 1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create Video Idea for this keyword:{Keywords}" ,
        temperature=0.3,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        result = response['choices'][0]['text']
        result = result.replace("\n", "<br>")
        count = len(result.split())
        postCreditBalanceUpdate(post_balance,api_key,count)
        return result
    else:
        return recarge


if __name__ == "__main__":
    app.run(debug=True)
    
# http://127.0.0.1:5000/Product-decription?product=***&description=***&api-key=***
# http://127.0.0.1:5000/blog-selection-writing?keyword=***&topic=***&api-key=***
# http://127.0.0.1:5000/brand-name?description=***&api-key=***
# http://127.0.0.1:5000/business-idea-pitch?idea=***&api-key=***
# http://127.0.0.1:5000/business-ideas?interest=***&skills=***&api-key=***
# http://127.0.0.1:5000/call-to-action?decription=***&api-key=***
# http://127.0.0.1:5000/cover-letter?job_role=***&job_skills=***&api-key=***
# http://127.0.0.1:5000/email?key_points=***&api-key=***
# http://127.0.0.1:5000/twitter-ads?product_name=***&description=***&api-key=***
# http://127.0.0.1:5000/facebook-ads?product_name=***&description=***&api-key=***
# http://127.0.0.1:5000/linkedin-ads?product_name=***&description=***&api-key=***
# http://127.0.0.1:5000/google-search-ads?product_name=***&description=***&api-key=***
# http://127.0.0.1:5000/interview-questions?interview_bio=***&interview_context=***&api-key=***
# http://127.0.0.1:5000/job-description?Job_role=***&api-key=***
# http://127.0.0.1:5000/post-caption-ideas?Post_topic=***&api-key=***
# http://127.0.0.1:5000/profile-bio?about_you=***&api-key=***
# http://127.0.0.1:5000/question-answer?topic_description=***&api-key=***
# http://127.0.0.1:5000/seo-meta-description?page_meta_title=***&api-key=***
# http://127.0.0.1:5000/seo-meta-title?target_keywords=***&api-key=***
# http://127.0.0.1:5000/story-plot?story_Idea=***&api-key=***
# http://127.0.0.1:5000/tagline-headline?description=***&api-key=***
# http://127.0.0.1:5000/testimonial-review?name=***&review_title=***&api-key=***
# http://127.0.0.1:5000/video-channel-description?Channel_purpose=***&api-key=***
# http://127.0.0.1:5000/video-description?video_title=***&api-key=***
# http://127.0.0.1:5000/video-idea?keywords=***&api-key=***