### Data Processing in R and Python 2023Z
### Homework Assignment no. 2
###
### IMPORTANT
### This file should contain only solutions to tasks in the form of a functions
### definitions and comments to the code.
###
#
# Include imports here
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------#
# Task 1
# -----------------------------------------------------------------------------#

def solution_1(Posts, Users):
    Posts1 = Posts.loc[:, ['OwnerUserId']]
    Users1 = Users.loc[:, ['Id', 'Location']]

    x = Posts1.set_index('OwnerUserId').join(Users1.set_index('Id'))
    x = x.loc[x["Location"] != '']
    x = x.groupby('Location').size().reset_index() # resetting indices to get DataFrame

    x.rename(columns = {0: "Count"}, inplace = True)
    x = x.sort_values(by = 'Count', ascending = False).reset_index(drop=True).head(10) # resetting indices to get the equality
    return x

# -----------------------------------------------------------------------------#
# Task 2
# -----------------------------------------------------------------------------#

def solution_2(Posts, PostLinks):
    RelatedTab = PostLinks.groupby('RelatedPostId').size().reset_index() # resetting indices to get DataFrame
    RelatedTab.rename(columns = {'RelatedPostId': "PostId", 0: "NumLinks"}, inplace = True)
    x = RelatedTab.set_index('PostId').join(Posts.set_index('Id'))

    x = x.loc[x["PostTypeId"] == 1]
    x = x.sort_values(by = ['NumLinks', 'PostId'], ascending = [False, True]).reset_index(drop = True) # resetting indices to get the equality
    x = x.loc[:, ["Title", "NumLinks"]]

    return x

# -----------------------------------------------------------------------------#
# Task 3
# -----------------------------------------------------------------------------#

def solution_3(Posts, Users, Comments):
    CmtTotScr = Comments.loc[:, ['PostId', 'Score']]
    CmtTotScr = CmtTotScr.groupby('PostId').aggregate(np.sum).reset_index() # resetting indices to receive PostId column
    CmtTotScr.rename(columns = {'Score': "CommentsTotalScore"}, inplace = True)

    PostsBestComments = Posts.set_index('Id').join(CmtTotScr.set_index('PostId'))
    PostsBestComments = PostsBestComments.loc[PostsBestComments["PostTypeId"] == 1]
    PostsBestComments = PostsBestComments.loc[:, ['OwnerUserId', 'Title', 'CommentCount', 'ViewCount', 'CommentsTotalScore']]

    x = PostsBestComments.set_index('OwnerUserId').join(Users.set_index('Id'))
    x = x.sort_values(by = 'CommentsTotalScore', ascending = False)
    x = x.replace({'Location': {np.nan: 'None'}}) # NaN values in column SQL are called 'None', temporarily in string type in order to not delete it
    x = x.loc[:, ['Title', 'CommentCount', 'ViewCount', 'CommentsTotalScore', 'DisplayName', 'Reputation', 'Location']]

    x = x.dropna() # dropping NaN values to get equality
    x = x.replace({'Location': {'None': None}}) # correcting form of None values
    x = x.head(10).reset_index(drop = True) # resetting indices to get equality
    x = x.astype({'CommentsTotalScore': 'int64', 'Reputation': 'int64'}) # correcting type of some columns to get equality

    return x
    
# -----------------------------------------------------------------------------#
# Task 4
# -----------------------------------------------------------------------------#

def solution_4(Posts, Users):
    Answers = Posts.loc[Posts['PostTypeId'] == 2].groupby('OwnerUserId').size().reset_index() # resetting indices to get OwnerUserId column
    Answers = Answers.reindex(columns = [0, 'OwnerUserId']) # swapping columns
    Answers.rename(columns = {0: 'AnswersNumber'}, inplace = True)

    Questions = Posts.loc[Posts['PostTypeId'] == 1].groupby('OwnerUserId').size().reset_index() # resetting indices to get OwnerUserId column
    Questions = Questions.reindex(columns = [0, 'OwnerUserId']) # swapping columns
    Questions.rename(columns = {0: 'QuestionsNumber'}, inplace = True)

    PostsCounts = Answers.merge(Questions, on = 'OwnerUserId')
    PostsCounts = PostsCounts.loc[PostsCounts['AnswersNumber'] > PostsCounts['QuestionsNumber']]
    PostsCounts = PostsCounts.sort_values(by = 'AnswersNumber', ascending = False).head(5)

    x = PostsCounts.set_index('OwnerUserId').join(Users.set_index('Id'))
    x = x.loc[:, ['DisplayName', 'QuestionsNumber', 'AnswersNumber', 'Location', 'Reputation', 'UpVotes', 'DownVotes']]
    x = x.sort_values(by = 'AnswersNumber', ascending = False).reset_index(drop = True) # resetting indices to get equality

    return x
    
# -----------------------------------------------------------------------------#
# Task 5
# -----------------------------------------------------------------------------#

def solution_5(Posts):
    BestAnswers = Posts.loc[Posts['PostTypeId'] == 2].groupby('ParentId').apply(lambda group: pd.Series({
        'Id': group.loc[group['Score'].idxmax(), 'Id'],
        'ParentId': group['ParentId'].max(),
        'MaxScore': group['Score'].max()
    })).reset_index(drop = True) # this takes quite a time but I haven't come up with better solution
    BestAnswers.rename(columns = {'Score': "MaxScore"}, inplace = True)

    Questions = Posts.loc[Posts['PostTypeId'] == 1]

    Questions = Questions.set_index('Id').join(BestAnswers.set_index('ParentId'), rsuffix = '.y', lsuffix = '.x').rename(columns = {'Id': 'Id2'}).reset_index()
        # renaming Id column name to Id2 in order to reset index and get Id column that interests us
    Questions = Questions.set_index('AcceptedAnswerId').join(Posts.set_index('Id'), how = 'inner', rsuffix = '.y', lsuffix = '.x').reset_index(drop = True).reset_index()
        # double resetting indices in order to get column of new indices and then use it to merge Questions with Difference
    Difference = (Questions['MaxScore'] - Questions['Score.y']).reset_index(drop = True).reset_index()
        # double resetting indices in order to get column of new indices and then use it to merge Questions with Difference

    x = Questions.merge(Difference, on = 'index').loc[:, ['Id', 'Title.x', 'MaxScore', 'Score.y', 0]]
    x.rename(columns = {'Title.x': "Title", 'Score.y': "AcceptedScore", 0: "Difference"}, inplace = True)
    x = x.loc[x['Difference'] > 50]
    x = x.sort_values(by = ['Difference', 'Id'], ascending = [False, True]).reset_index(drop = True) # resetting indices to get equality
    x = x.astype({'Id': 'int64', 'MaxScore': 'int64', 'Difference': 'int64'}) # changing type of columns to get equality

    return x
