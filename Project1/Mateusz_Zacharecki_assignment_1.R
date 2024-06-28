### Data Processing in R and Python 2023Z
### Homework Assignment no. 1
###
### IMPORTANT
### This file should contain only solutions to tasks in the form of a functions
### definitions and comments to the code.
###
### Report should include:
### * source() of this file at the beggining,
### * reading the data, 
### * attaching the libraries, 
### * execution time measurements (with microbenchmark),
### * and comparing the equivalence of the results,
### * interpretation of queries.

options(stringsAsFactors=FALSE)

Posts <- read.csv("Posts.csv.gz")
head(Posts)

Users <- read.csv("Users.csv.gz")
head(Users)

PostLinks <- read.csv("PostLinks.csv.gz")
head(PostLinks)

Comments <- read.csv("Comments.csv.gz")
head(Comments)

# Libraries

library(sqldf)
library(dplyr)
library(data.table)
library(compare)

# -----------------------------------------------------------------------------#
# Task 1
# -----------------------------------------------------------------------------#

sqldf_1 <- function(Posts, Users){
  # Input the solution here
  # 
  sqldf("SELECT Location, COUNT(*) AS Count
         FROM (
             SELECT Posts.OwnerUserId, Users.Id, Users.Location
             FROM Users
             JOIN Posts ON Users.Id = Posts.OwnerUserId
         )
         WHERE Location NOT IN ('')
         GROUP BY Location
         ORDER BY Count DESC
         LIMIT 10")
}

base_1 <- function(Posts, Users){
  # Input the solution here
  # 
  Posts1 <- data.frame(Posts[, c('OwnerUserId')])
  colnames(Posts1) <- "OwnerUserId"
  Users1 <- Users[, c('Id', 'Location')]
  
  x <- merge(Users1, Posts1, by.x = "Id", by.y = "OwnerUserId")
  x <- subset(x, trimws(Location) != "")
  x <- as.data.frame(table(x$Location))
  
  colnames(x) <- c("Location", "Count")
  x <- x[order(x$Count, decreasing = T), ]
  x <- x[c(1:10), ]
  
  rownames(x) <- c(1,2,3,4,5,6,7,8,9,10)
  x[['Location']] <- as.character(x[['Location']]) # without that we get integer type 
  
  return(x)
}

dplyr_1 <- function(Posts, Users){
  # Input the solution here
  # 
  # we use inner_join which corresponds sql's join
  x <- inner_join(select(Users, c("Id", "Location")), select(Posts, OwnerUserId), join_by(Id == OwnerUserId))
  x <- filter(x, Location != "")
  x <- count(x, Location)

  x <- rename(x, Count = "n")
  x <- arrange(x, desc(Count))
  x <- slice(x, 1:10)
  x <- mutate(x, Location = as.character(Location)) # without that we get integer type
  
  rownames(x) <- c(1:10)
  
  return(x)
}

data.table_1 <- function(Posts, Users){
  # Input the solution here
  # 
  # merge from data.table works quite similar as in base R
  x <- merge(data.table(Id = Users$Id, Location = Users$Location), 
             data.table(OwnerUserId = Posts$OwnerUserId), by.x = "Id", by.y = "OwnerUserId")
  x <- x[Location != ""]
  
  x <- x[, .N, by = Location][order(-N)][1:10]
  setnames(x, c("Location", "Count"))
  
  rownames(x) <- c(1:10)
  x$Location <- as.character(x$Location) # without that we get integer type
  
  return(x)
}

# -----------------------------------------------------------------------------#
# Task 2
# -----------------------------------------------------------------------------#

sqldf_2 <- function(Posts, PostLinks){
  sqldf("
    SELECT RelatedPostId AS PostId, COUNT(*) AS NumLinks
    FROM PostLinks
    GROUP BY RelatedPostId
    ") -> RelatedTab
  
  sqldf("
    SELECT Posts.Title, RelatedTab.NumLinks
    FROM RelatedTab
    JOIN Posts ON RelatedTab.PostId=Posts.Id
    WHERE Posts.PostTypeId=1
    ORDER BY NumLinks DESC
    ")    
}

base_2 <- function(Posts, PostLinks){
  # Input the solution here
  # 
  RelatedTab <- as.data.frame(table(PostLinks[, 'RelatedPostId']))
  colnames(RelatedTab) <- c("PostId", "NumLinks")
  x <- merge(RelatedTab, Posts, by.x = "PostId", by.y = "Id")
  
  x <- x[x$PostTypeId == 1, ]
  x <- x[order(x$NumLinks, decreasing = T), ]
  x <- x[, c("Title", "NumLinks")]
  
  return(x)
}

dplyr_2 <- function(Posts, PostsLinks){
  # Input the solution here
  # 
  RelatedTab <- count(PostLinks, RelatedPostId)
  RelatedTab <- rename(RelatedTab, c(PostId = "RelatedPostId", NumLinks = "n"))
  x <- inner_join(RelatedTab, Posts, join_by(PostId == Id))
  
  x <- filter(x, PostTypeId == 1)
  x <- arrange(x, desc(NumLinks))
  x <- select(x, c("Title", "NumLinks"))
  
  return(x)
}

data.table_2 <- function(Posts, PostsLinks){
  # Input the solution here
  # 
  RelatedTab <- data.table(PostLinks)
  RelatedTab <- RelatedTab[, .N, by = RelatedPostId]
  setnames(RelatedTab, c("PostId", "NumLinks"))
  x <- merge(RelatedTab, Posts, by.x = "PostId", by.y = "Id")
  
  x <- x[PostTypeId == 1][order(-NumLinks)]
  x <- x[, .(Title, NumLinks)]
  
  return(x)
}

# -----------------------------------------------------------------------------#
# Task 3
# -----------------------------------------------------------------------------#

sqldf_3 <- function(Posts, Users, Comments){
  sqldf("
        SELECT Title, CommentCount, ViewCount, CommentsTotalScore, 
               DisplayName, Reputation, Location
        FROM (
                SELECT Posts.OwnerUserId, Posts.Title, 
                       Posts.CommentCount, Posts.ViewCount, 
                       CmtTotScr.CommentsTotalScore
                FROM (
                        SELECT PostId, SUM(Score) AS CommentsTotalScore
                        FROM Comments
                        GROUP BY PostId
                     ) AS CmtTotScr
                JOIN Posts ON Posts.Id = CmtTotScr.PostId
                WHERE Posts.PostTypeId=1
            ) AS PostsBestComments
        JOIN Users ON PostsBestComments.OwnerUserId = Users.Id
        ORDER BY CommentsTotalScore DESC
    ") -> tab
  # selecting LIMIT separately will improve time 
  sqldf("SELECT * FROM tab LIMIT 10")
}

base_3 <- function(Posts, Users, Comments){
  # Input the solution here
  # 
  CmtTotScr <- Comments[, c('PostId', 'Score')]
  CmtTotScr <- aggregate(CmtTotScr[, 'Score'], CmtTotScr['PostId'],
                         sum, na.rm = T)
  colnames(CmtTotScr)[2] <- "CommentsTotalScore"
  
  PostsBestComments <- merge(Posts, CmtTotScr, by.x = "Id", by.y = "PostId")
  PostsBestComments <- PostsBestComments[PostsBestComments$PostTypeId == 1, ]
  PostsBestComments <- PostsBestComments[, c('OwnerUserId', 'Title', 
                                             'CommentCount', 'ViewCount',
                                             'CommentsTotalScore')]
  
  x <- merge(PostsBestComments, Users, by.x = "OwnerUserId", by.y = "Id")
  x <- x[order(x$CommentsTotalScore, decreasing = T), ]
  x <- x[c(1:10), ]
  x <- x[, c('Title', 'CommentCount', 'ViewCount', 'CommentsTotalScore',
             'DisplayName', 'Reputation', 'Location')]
  rownames(x) <- 1:10
  
  return(x)
}

dplyr_3 <- function(Posts, Users, Comments){
  # Input the solution here
  # 
  CmtTotScr <- select(Comments, c('PostId', 'Score'))
  CmtTotScr <- group_by(CmtTotScr, PostId)
  CmtTotScr <- summarise(CmtTotScr, CommentsTotalScore = sum(Score))
  CmtTotScr <- ungroup(CmtTotScr)
  CmtTotScr <- filter(CmtTotScr, is.na(PostId) == F) # in sql na values of PostId are omitted
  
  PostsBestComments <- inner_join(Posts, CmtTotScr, join_by(Id == PostId))
  PostsBestComments <- filter(PostsBestComments, PostTypeId == 1)
  PostsBestComments <- select(PostsBestComments, c('OwnerUserId', 'Title', 
                                                   'CommentCount', 'ViewCount',
                                                   'CommentsTotalScore'))
  
  x <- inner_join(PostsBestComments, Users, join_by(OwnerUserId == Id))
  x <- arrange(x, desc(CommentsTotalScore))
  x <- slice(x, 1:10)
  x <- select(x, c('Title', 'CommentCount', 'ViewCount', 'CommentsTotalScore',
                   'DisplayName', 'Reputation', 'Location'))
  rownames(x) <- 1:10
  
  return(x)
}

data.table_3 <- function(Posts, Users, Comments){
  # Input the solution here
  # 
  CmtTotScr <- data.table(Comments)[, .(PostId, Score)]
  CmtTotScr <- CmtTotScr[, .(CommentsTotalScore = sum(Score)), by = PostId]
  CmtTotScr <- CmtTotScr[is.na(PostId) == F] # in sql na values of PostId are omitted
  
  PostsBestComments <- merge(data.table(Posts), CmtTotScr, by.x = "Id", by.y = "PostId")
  PostsBestComments <- PostsBestComments[PostTypeId == 1]
  PostsBestComments <- PostsBestComments[, .(OwnerUserId, Title, 
                                             CommentCount, ViewCount,
                                             CommentsTotalScore)]
  
  x <- merge(PostsBestComments, Users, by.x = "OwnerUserId", by.y = "Id")
  x <- x[order(-CommentsTotalScore)][1:10]
  x <- x[, .(Title, CommentCount, ViewCount, CommentsTotalScore,
             DisplayName, Reputation, Location)]
  rownames(x) <- 1:10
  
  return(x)
}

# -----------------------------------------------------------------------------#
# Task 4
# -----------------------------------------------------------------------------#

sqldf_4 <- function(Posts, Users){
  # Input the solution here
  # 
  sqldf("SELECT DisplayName, QuestionsNumber, AnswersNumber, Location, Reputation, UpVotes, DownVotes
        FROM (
         SELECT *
            FROM (
              SELECT COUNT(*) as AnswersNumber, OwnerUserId
              FROM Posts
              WHERE PostTypeId = 2
              GROUP BY OwnerUserId
            ) AS Answers
          JOIN
          (
            SELECT COUNT(*) as QuestionsNumber, OwnerUserId
            FROM Posts
            WHERE PostTypeId = 1
            GROUP BY OwnerUserId
          ) AS Questions
          ON Answers.OwnerUserId = Questions.OwnerUserId
          WHERE AnswersNumber > QuestionsNumber
          ORDER BY AnswersNumber DESC
          LIMIT 5
        ) AS PostsCounts
        JOIN Users
        ON PostsCounts.OwnerUserId = Users.Id")
}

base_4 <- function(Posts, Users){
  # Input the solution here
  # 
  Answers <- as.data.frame(table(Posts[Posts$PostTypeId == 2, 'OwnerUserId']))
  Answers <- data.frame(Answers[, 2], Answers[, 1])
  colnames(Answers) <- c('AnswersNumber', 'OwnerUserId')
  
  Questions <- as.data.frame(table(Posts[Posts$PostTypeId == 1, 'OwnerUserId']))
  Questions <- data.frame(Questions[, 2], Questions[, 1])
  colnames(Questions) <- c('QuestionsNumber', 'OwnerUserId')
  
  PostsCounts <- merge(Answers, Questions, by = "OwnerUserId")
  PostsCounts <- PostsCounts[PostsCounts$AnswersNumber > PostsCounts$QuestionsNumber, ]
  PostsCounts <- PostsCounts[order(PostsCounts$AnswersNumber, decreasing = T), ]
  PostsCounts <- PostsCounts[c(1:5), ]
  
  x <- merge(PostsCounts, Users, by.x = "OwnerUserId", by.y = "Id")
  x <- data.frame(x[, 'DisplayName'],
                  x[, 'QuestionsNumber'],
                  x[, 'AnswersNumber'],
                  x[, 'Location'],
                  x[, 'Reputation'],
                  x[, 'UpVotes'],
                  x[, 'DownVotes'])
  colnames(x) <- c('DisplayName', 'QuestionsNumber', 'AnswersNumber', 
                   'Location', 'Reputation', 'UpVotes', 'DownVotes')
  x <- x[order(x$AnswersNumber, decreasing = T), ]
  rownames(x) <- c(1:5)
  
  return(x)
}

dplyr_4 <- function(Posts, Users){
  # Input the solution here
  # 
  Answers <- filter(Posts, PostTypeId == 2)
  Answers <- count(Answers, OwnerUserId)
  Answers <- filter(Answers, is.na(OwnerUserId) == F)
  Answers <- relocate(Answers, n)
  Answers <- rename(Answers, AnswersNumber = "n")
  
  Questions <- filter(Posts, PostTypeId == 1)
  Questions <- count(Questions, OwnerUserId)
  Questions <- filter(Questions, is.na(OwnerUserId) == F)
  Questions <- relocate(Questions, n)
  Questions <- rename(Questions, QuestionsNumber = "n")
  
  PostsCounts <- inner_join(Answers, Questions, by = "OwnerUserId")
  PostsCounts <- filter(PostsCounts, AnswersNumber > QuestionsNumber)
  PostsCounts <- arrange(PostsCounts, desc(AnswersNumber))
  PostsCounts <- slice(PostsCounts, 1:5)
  
  x <- inner_join(PostsCounts, Users, join_by("OwnerUserId" == "Id"))
  x <- select(x, c('DisplayName', 'QuestionsNumber', 'AnswersNumber', 
                   'Location', 'Reputation', 'UpVotes', 'DownVotes'))
  x <- arrange(x, desc(AnswersNumber))
  rownames(x) <- c(1:5)
  
  return(x)
}

data.table_4 <- function(Posts, Users){
  # Input the solution here
  # 
  Answers <- data.table(Posts)[PostTypeId == 2][, .N, by = OwnerUserId]
  Answers <- Answers[is.na(OwnerUserId) == F]
  setcolorder(Answers, c("N", "OwnerUserId"))
  setnames(Answers, c('AnswersNumber', 'OwnerUserId'))
  
  Questions <- data.table(Posts)[PostTypeId == 1][, .N, by = OwnerUserId]
  Questions <- Questions[is.na(OwnerUserId) == F]
  setcolorder(Questions, c("N", "OwnerUserId"))
  setnames(Questions, c('QuestionsNumber', 'OwnerUserId'))
  
  PostsCounts <- merge(Answers, Questions, by = "OwnerUserId")
  PostsCounts <- PostsCounts[AnswersNumber > QuestionsNumber]
  PostsCounts <- PostsCounts[order(-AnswersNumber)][1:5]
  
  x <- merge(PostsCounts, data.table(Users), by.x = "OwnerUserId", by.y = "Id")
  x <- x[, .(DisplayName, QuestionsNumber, AnswersNumber, 
             Location, Reputation, UpVotes, DownVotes)][order(-AnswersNumber)]
  rownames(x) <- c(1:5)
  
  return(x)
}

# -----------------------------------------------------------------------------#
# Task 2
# -----------------------------------------------------------------------------#

sqldf_5 <- function(Posts){
  # Input the solution here
  # 
  sqldf("SELECT
        Questions.Id,
        Questions.Title,
        BestAnswers.MaxScore,
        Posts.Score AS AcceptedScore,
        BestAnswers.MaxScore-Posts.Score AS Difference
        FROM (
          SELECT Id, ParentId, MAX(Score) AS MaxScore
          FROM Posts
          WHERE PostTypeId==2
          GROUP BY ParentId
        ) AS BestAnswers
        JOIN (
          SELECT * FROM Posts
          WHERE PostTypeId==1
        ) AS Questions
        ON Questions.Id=BestAnswers.ParentId
        JOIN Posts ON Questions.AcceptedAnswerId=Posts.Id
        WHERE Difference>50
        ORDER BY Difference DESC")
}

base_5 <- function(Posts){
  # Input the solution here
  # 
  BestAnswers <- merge(aggregate(Posts[, "Score"], by = Posts["ParentId"], FUN = max),
                       aggregate(Posts[, 'Id'], by = Posts["ParentId"], FUN = function(a) a[1]), by = "ParentId")
  BestAnswers <- data.frame(BestAnswers[, 3], BestAnswers[, 1], BestAnswers[, 2])
  colnames(BestAnswers) <- c("Id", "ParentId", "MaxScore")
  
  Questions <- Posts[Posts$PostTypeId == 1, ]
  
  Questions <- merge(Questions, BestAnswers, by.x = "Id", by.y = "ParentId")
  Questions <- merge(Questions, Posts, by.x = "AcceptedAnswerId", by.y = "Id")
  Difference <- Questions$MaxScore - Questions$Score.y
  x <- data.frame(Questions$Id,
                  Questions$Title.x,
                  Questions$MaxScore,
                  Questions$Score.y,
                  Difference)
  colnames(x) <- c('Id', 'Title', 'MaxScore', 'AcceptedScore', 'Difference')
  x <- x[x$Difference > 50, ]
  x <- x[order(x$Difference, decreasing = T), ]
  rownames(x) <- c(1:nrow(x))
  
  return(x)
}

dplyr_5 <- function(Posts){
  # Input the solution here
  # 
  BestAnswers <- inner_join(Posts %>% group_by(ParentId) %>%
                            summarise(MaxScore = max(Score)) %>%
                            ungroup(),
                            Posts %>% group_by(ParentId) %>%
                            summarise(Id = first(Id)) %>%
                            ungroup(),
                            by = "ParentId")
  BestAnswers <- filter(BestAnswers, is.na(ParentId) == F) # in sql na values of PostId are omitted
  
  Questions <- filter(Posts, PostTypeId == 1)
  
  Questions <- inner_join(Questions, BestAnswers, join_by(Id == ParentId))
  Questions <- inner_join(Questions, Posts, join_by(AcceptedAnswerId == Id))
  x <- mutate(Questions, Difference = MaxScore - Score.y)
  x <- select(x, c(Id, Title.x, MaxScore, Score.y, Difference))
  x <- rename(x, c(Title = Title.x, AcceptedScore = Score.y))
  x <- filter(x, Difference > 50)
  x <- arrange(x, desc(Difference))
  rownames(x) <- c(1:nrow(x))
  
  return(x)
}

data.table_5 <- function(Posts){
  # Input the solution here
  # 
  BestAnswers <- data.table(Posts)[, .(MaxScore = max(Score), Id = .I[which.max(Score)]), by = ParentId]
  BestAnswers <- BestAnswers[is.na(ParentId) == F] # in sql na values of PostId are omitted
  
  setcolorder(BestAnswers, c('Id', 'ParentId', 'MaxScore'))
  
  Questions <- data.table(Posts)[PostTypeId == 1]
  
  Questions <- merge(Questions, BestAnswers, by.x = "Id", by.y = "ParentId")
  Questions <- merge(Questions, Posts, by.x = "AcceptedAnswerId", by.y = "Id")
  Questions <- Questions[, Difference := MaxScore - Score.y]
  x <- Questions[, .(Id, Title = Title.x, MaxScore, AcceptedScore = Score.y, Difference)]
  setnames(x, c('Id', 'Title', 'MaxScore', 'AcceptedScore', 'Difference'))
  x <- x[Difference > 50][order(-Difference)]
  rownames(x) <- c(1:nrow(x))
  
  return(x)
}
