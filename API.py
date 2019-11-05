from stackapi import StackAPI
import pandas as pd

SITE = StackAPI('stackoverflow')
SITE.page_size = 10
SITE.max_pages = 200

questions = SITE.fetch('questions',tagged='javascript;jquery;html;css;angularjs')

dict = {'Id':[],'PostTypeId':[],'AcceptedAnswerId':[],'ParentId':[],
        'CreationDate':[],'DelectionDate': [],'Score': [],'ViewCount': [],
        'Body': [],'OwnerUserId': [], 'OwnerDisplayName': [], 'LastEditorUserId': [],
        'LastEditorDisplayName': [], 'Title':[],
        'Tags':[],'AnswerCount': [], 'Answerer_Score': [], 'CommentCount': []}
NumQ = len(questions['items'])

for i in range(NumQ):
    QId = questions['items'][i]['question_id']
    answers = SITE.fetch('/questions/{ids}/answers', ids=[QId])
    NumAn = len(answers['items'])
    for j in range(NumAn):
        dict['Id'].append(QId)
        dict['PostTypeId'].append(questions['items'][i]['type_id'])
        dict['AcceptedAnswerId'].append(questions['items'][j]['answe_id'])
        dict['ParentId'].append(questions['items'][i]['parent_id'])
        dict['Tags'].append(questions['items'][i]['tags'])
        dict['CreationDate'].append(questions['items'][i]['date'])
        dict['DelectionDate'].append(questions['items'][i]['date'])
        dict['Score'].append(questions['items'][i]['score'])
        dict['ViewCount'].append(questions['items'][i]['view_count'])      
        dict['Body'].append(questions['items'][i]['body'])
        dict['OwnerUserId'].append(questions['items'][i]['owner_user_id'])
        dict['OwnerDisplayName'].append(questions['items'][i]['display_name'])
        dict['Title'].append(questions['items'][i]['title'])      
        dict['Tags'].append(answers['items'][j]['tags'])
        dict['AnswerCount'].append(answers['items'][j]['answer_count'])
        dict['Answerer_Score'].append(answers['items'][j]['answer_score'])
        dict['CommentCount'].append(answers['items'][j]['comment_count'])
                

# allPosts.tsv 
save= pd.DataFrame(dict) 
# saving the dataframe 
save.to_csv('allPosts.csv') 
# allPosts-metaData.tsv
savegraph=save.loc[:,['Id','AcceptedAnswerId']]
savegraph.to_csv('allPosts-mataData.csv') 

