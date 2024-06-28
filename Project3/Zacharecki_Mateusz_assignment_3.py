
# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##### Did the war outbreak in Ukraine have an inpact on the activity on the considered websites?
##### If so, how did it influence the activity?

### Comments

def Plot1(CommentsDE, CommentsRU, CommentsUA):
    tempCommentsDE = CommentsDE
    tempCommentsDE['CreationDate'] = pd.to_datetime(tempCommentsDE['CreationDate'], format="%Y-%m-%dT%H:%M:%S.%f")
    tempCommentsDE['Month_Year'] = tempCommentsDE['CreationDate'].dt.strftime('%Y-%m')
    tempCommentsDE['Month_Year'] = pd.to_datetime(tempCommentsDE['Month_Year'], format="%Y-%m")
    tempCommentsDE = pd.DataFrame(tempCommentsDE.groupby('Month_Year').size().reset_index())
    tempCommentsDE.rename(columns={0: "Count"}, inplace=True)

    tempCommentsRU = CommentsRU
    tempCommentsRU['CreationDate'] = pd.to_datetime(tempCommentsRU['CreationDate'], format="%Y-%m-%dT%H:%M:%S.%f")
    tempCommentsRU['Month_Year'] = tempCommentsRU['CreationDate'].dt.strftime('%Y-%m')
    tempCommentsRU['Month_Year'] = pd.to_datetime(tempCommentsRU['Month_Year'], format="%Y-%m")
    tempCommentsRU = pd.DataFrame(tempCommentsRU.groupby('Month_Year').size().reset_index())
    tempCommentsRU.rename(columns={0: "Count"}, inplace=True)

    tempCommentsUA = CommentsUA
    tempCommentsUA['CreationDate'] = pd.to_datetime(tempCommentsUA['CreationDate'], format="%Y-%m-%dT%H:%M:%S.%f")
    tempCommentsUA['Month_Year'] = tempCommentsUA['CreationDate'].dt.strftime('%Y-%m')
    tempCommentsUA['Month_Year'] = pd.to_datetime(tempCommentsUA['Month_Year'], format="%Y-%m")
    tempCommentsUA = pd.DataFrame(tempCommentsUA.groupby('Month_Year').size().reset_index())
    tempCommentsUA.rename(columns={0: "Count"}, inplace=True)

    plt.figure(figsize=(14, 7))
    plt.plot(tempCommentsDE.Month_Year, tempCommentsDE.Count, label='German')
    plt.plot(tempCommentsRU.Month_Year, tempCommentsRU.Count, label='Russian')
    plt.plot(tempCommentsUA.Month_Year, tempCommentsUA.Count, label='Ukrainian')
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Number of comments')
    plt.title("Comments")
    plt.grid()

### Posts

def Plot2(PostsDE, PostsRU, PostsUA):
    tempPostsDE = PostsDE
    tempPostsDE['CreationDate'] = pd.to_datetime(tempPostsDE['CreationDate'], format="%Y-%m-%dT%H:%M:%S.%f")
    tempPostsDE['Month_Year'] = tempPostsDE['CreationDate'].dt.strftime('%Y-%m')
    tempPostsDE['Month_Year'] = pd.to_datetime(tempPostsDE['Month_Year'], format="%Y-%m")
    tempPostsDE = pd.DataFrame(tempPostsDE.groupby('Month_Year').size().reset_index())
    tempPostsDE.rename(columns={0: "Count"}, inplace=True)

    tempPostsRU = PostsRU
    tempPostsRU['CreationDate'] = pd.to_datetime(tempPostsRU['CreationDate'], format="%Y-%m-%dT%H:%M:%S.%f")
    tempPostsRU['Month_Year'] = tempPostsRU['CreationDate'].dt.strftime('%Y-%m')
    tempPostsRU['Month_Year'] = pd.to_datetime(tempPostsRU['Month_Year'], format="%Y-%m")
    tempPostsRU = pd.DataFrame(tempPostsRU.groupby('Month_Year').size().reset_index())
    tempPostsRU.rename(columns={0: "Count"}, inplace=True)

    tempPostsUA = PostsUA
    tempPostsUA['CreationDate'] = pd.to_datetime(tempPostsUA['CreationDate'], format="%Y-%m-%dT%H:%M:%S.%f")
    tempPostsUA['Month_Year'] = tempPostsUA['CreationDate'].dt.strftime('%Y-%m')
    tempPostsUA['Month_Year'] = pd.to_datetime(tempPostsUA['Month_Year'], format="%Y-%m")
    tempPostsUA = pd.DataFrame(tempPostsUA.groupby('Month_Year').size().reset_index())
    tempPostsUA.rename(columns={0: "Count"}, inplace=True)

    plt.figure(figsize=(14, 7))
    plt.plot(tempPostsDE.Month_Year, tempPostsDE.Count, label='German')
    plt.plot(tempPostsRU.Month_Year, tempPostsRU.Count, label='Russian')
    plt.plot(tempPostsUA.Month_Year, tempPostsUA.Count, label='Ukrainian')
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Number of posts')
    plt.title("Posts")
    plt.grid()

### Users

def Plot3(UsersDE, UsersRU, UsersUA):
    tempUsersDE = UsersDE
    tempUsersDE['CreationDate'] = pd.to_datetime(tempUsersDE['CreationDate'], format="%Y-%m-%dT%H:%M:%S.%f")
    tempUsersDE['Month_Year'] = tempUsersDE['CreationDate'].dt.strftime('%Y-%m')
    tempUsersDE['Month_Year'] = pd.to_datetime(tempUsersDE['Month_Year'], format="%Y-%m")
    tempUsersDE = pd.DataFrame(tempUsersDE.groupby('Month_Year').size().reset_index())
    tempUsersDE.rename(columns={0: "Count"}, inplace=True)

    tempUsersRU = UsersRU
    tempUsersRU['CreationDate'] = pd.to_datetime(tempUsersRU['CreationDate'], format="%Y-%m-%dT%H:%M:%S.%f")
    tempUsersRU['Month_Year'] = tempUsersRU['CreationDate'].dt.strftime('%Y-%m')
    tempUsersRU['Month_Year'] = pd.to_datetime(tempUsersRU['Month_Year'], format="%Y-%m")
    tempUsersRU = pd.DataFrame(tempUsersRU.groupby('Month_Year').size().reset_index())
    tempUsersRU.rename(columns={0: "Count"}, inplace=True)

    tempUsersUA = UsersUA
    tempUsersUA['CreationDate'] = pd.to_datetime(tempUsersUA['CreationDate'], format="%Y-%m-%dT%H:%M:%S.%f")
    tempUsersUA['Month_Year'] = tempUsersUA['CreationDate'].dt.strftime('%Y-%m')
    tempUsersUA['Month_Year'] = pd.to_datetime(tempUsersUA['Month_Year'], format="%Y-%m")
    tempUsersUA = pd.DataFrame(tempUsersUA.groupby('Month_Year').size().reset_index())
    tempUsersUA.rename(columns={0: "Count"}, inplace=True)

    plt.figure(figsize=(14, 7))
    plt.plot(tempUsersDE.Month_Year, tempUsersDE.Count, label='German')
    plt.plot(tempUsersRU.Month_Year, tempUsersRU.Count, label='Russian')
    plt.plot(tempUsersUA.Month_Year, tempUsersUA.Count, label='Ukrainian')
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Number of users')
    plt.title("Users")
    plt.grid()

### Comments between 2022-02-01 and 2022-03-31

def Plot4(CommentsDE, CommentsRU, CommentsUA):
    tempCommentsDE2 = CommentsDE
    tempCommentsDE2['CreationDate'] = pd.to_datetime(tempCommentsDE2['CreationDate'], format="%Y-%m-%d")
    tempCommentsDE2['CreationDate'] = tempCommentsDE2['CreationDate'].dt.strftime('%Y-%m-%d')
    tempCommentsDE2['CreationDate'] = pd.to_datetime(tempCommentsDE2['CreationDate'], format="%Y-%m-%d")
    tempCommentsDE2 = tempCommentsDE2.loc[(tempCommentsDE2['CreationDate'] >= '2022-02-01') &
                                          (tempCommentsDE2['CreationDate'] < '2022-04-01')]
    tempCommentsDE2 = pd.DataFrame(tempCommentsDE2.groupby('CreationDate').size().reset_index())
    tempCommentsDE2.rename(columns={0: "Count"}, inplace=True)

    tempCommentsRU2 = CommentsRU
    tempCommentsRU2['CreationDate'] = pd.to_datetime(tempCommentsRU2['CreationDate'], format="%Y-%m-%d")
    tempCommentsRU2['CreationDate'] = tempCommentsRU2['CreationDate'].dt.strftime('%Y-%m-%d')
    tempCommentsRU2['CreationDate'] = pd.to_datetime(tempCommentsRU2['CreationDate'], format="%Y-%m-%d")
    tempCommentsRU2 = tempCommentsRU2.loc[(tempCommentsRU2['CreationDate'] >= '2022-02-01') &
                                          (tempCommentsRU2['CreationDate'] < '2022-04-01')]
    tempCommentsRU2 = pd.DataFrame(tempCommentsRU2.groupby('CreationDate').size().reset_index())
    tempCommentsRU2.rename(columns={0: "Count"}, inplace=True)

    tempCommentsUA2 = CommentsUA
    tempCommentsUA2['CreationDate'] = pd.to_datetime(tempCommentsUA2['CreationDate'], format="%Y-%m-%d")
    tempCommentsUA2['CreationDate'] = tempCommentsUA2['CreationDate'].dt.strftime('%Y-%m-%d')
    tempCommentsUA2['CreationDate'] = pd.to_datetime(tempCommentsUA2['CreationDate'], format="%Y-%m-%d")
    tempCommentsUA2 = tempCommentsUA2.loc[(tempCommentsUA2['CreationDate'] >= '2022-02-01') &
                                          (tempCommentsUA2['CreationDate'] < '2022-04-01')]
    tempCommentsUA2 = pd.DataFrame(tempCommentsUA2.groupby('CreationDate').size().reset_index())
    tempCommentsUA2.rename(columns={0: "Count"}, inplace=True)

    plt.figure(figsize=(14, 7))
    plt.plot(tempCommentsDE2.CreationDate, tempCommentsDE2.Count, label='German')
    plt.plot(tempCommentsRU2.CreationDate, tempCommentsRU2.Count, label='Russian')
    plt.plot(tempCommentsUA2.CreationDate, tempCommentsUA2.Count, label='Ukrainian')
    plt.legend()
    plt.xlabel('Day')
    plt.ylabel('Number of comments between 2022-02-01 and 2022-03-31')
    plt.title("Comments")
    plt.grid()

### Posts between 2022-02-01 and 2022-03-31

def Plot5(PostsDE, PostsRU, PostsUA):
    tempPostsDE2 = PostsDE
    tempPostsDE2['CreationDate'] = pd.to_datetime(tempPostsDE2['CreationDate'], format="%Y-%m-%d")
    tempPostsDE2['CreationDate'] = tempPostsDE2['CreationDate'].dt.strftime('%Y-%m-%d')
    tempPostsDE2['CreationDate'] = pd.to_datetime(tempPostsDE2['CreationDate'], format="%Y-%m-%d")
    tempPostsDE2 = tempPostsDE2.loc[(tempPostsDE2['CreationDate'] >= '2022-02-01') &
                                    (tempPostsDE2['CreationDate'] < '2022-04-01')]
    tempPostsDE2 = pd.DataFrame(tempPostsDE2.groupby('CreationDate').size().reset_index())
    tempPostsDE2.rename(columns={0: "Count"}, inplace=True)

    tempPostsRU2 = PostsRU
    tempPostsRU2['CreationDate'] = pd.to_datetime(tempPostsRU2['CreationDate'], format="%Y-%m-%d")
    tempPostsRU2['CreationDate'] = tempPostsRU2['CreationDate'].dt.strftime('%Y-%m-%d')
    tempPostsRU2['CreationDate'] = pd.to_datetime(tempPostsRU2['CreationDate'], format="%Y-%m-%d")
    tempPostsRU2 = tempPostsRU2.loc[(tempPostsRU2['CreationDate'] >= '2022-02-01') &
                                    (tempPostsRU2['CreationDate'] < '2022-04-01')]
    tempPostsRU2 = pd.DataFrame(tempPostsRU2.groupby('CreationDate').size().reset_index())
    tempPostsRU2.rename(columns={0: "Count"}, inplace=True)

    tempPostsUA2 = PostsUA
    tempPostsUA2['CreationDate'] = pd.to_datetime(tempPostsUA2['CreationDate'], format="%Y-%m-%d")
    tempPostsUA2['CreationDate'] = tempPostsUA2['CreationDate'].dt.strftime('%Y-%m-%d')
    tempPostsUA2['CreationDate'] = pd.to_datetime(tempPostsUA2['CreationDate'], format="%Y-%m-%d")
    tempPostsUA2 = tempPostsUA2.loc[(tempPostsUA2['CreationDate'] >= '2022-02-01') &
                                    (tempPostsUA2['CreationDate'] < '2022-04-01')]
    tempPostsUA2 = pd.DataFrame(tempPostsUA2.groupby('CreationDate').size().reset_index())
    tempPostsUA2.rename(columns={0: "Count"}, inplace=True)

    plt.figure(figsize=(14, 7))
    plt.plot(tempPostsDE2.CreationDate, tempPostsDE2.Count, label='German')
    plt.plot(tempPostsRU2.CreationDate, tempPostsRU2.Count, label='Russian')
    plt.plot(tempPostsUA2.CreationDate, tempPostsUA2.Count, label='Ukrainian')
    plt.legend()
    plt.xlabel('Day')
    plt.ylabel('Number of posts between 2022-02-01 and 2022-03-31')
    plt.title("Posts")
    plt.grid()

### Users between 2022-02-01 and 2022-03-31

def Plot6(UsersDE, UsersRU, UsersUA):
    tempUsersDE2 = UsersDE
    tempUsersDE2['CreationDate'] = pd.to_datetime(tempUsersDE2['CreationDate'], format="%Y-%m-%d")
    tempUsersDE2['CreationDate'] = tempUsersDE2['CreationDate'].dt.strftime('%Y-%m-%d')
    tempUsersDE2['CreationDate'] = pd.to_datetime(tempUsersDE2['CreationDate'], format="%Y-%m-%d")
    tempUsersDE2 = tempUsersDE2.loc[(tempUsersDE2['CreationDate'] >= '2022-02-01') &
                                    (tempUsersDE2['CreationDate'] < '2022-04-01')]
    tempUsersDE2 = pd.DataFrame(tempUsersDE2.groupby('CreationDate').size().reset_index())
    tempUsersDE2.rename(columns={0: "Count"}, inplace=True)

    tempUsersRU2 = UsersRU
    tempUsersRU2['CreationDate'] = pd.to_datetime(tempUsersRU2['CreationDate'], format="%Y-%m-%d")
    tempUsersRU2['CreationDate'] = tempUsersRU2['CreationDate'].dt.strftime('%Y-%m-%d')
    tempUsersRU2['CreationDate'] = pd.to_datetime(tempUsersRU2['CreationDate'], format="%Y-%m-%d")
    tempUsersRU2 = tempUsersRU2.loc[(tempUsersRU2['CreationDate'] >= '2022-02-01') &
                                    (tempUsersRU2['CreationDate'] < '2022-04-01')]
    tempUsersRU2 = pd.DataFrame(tempUsersRU2.groupby('CreationDate').size().reset_index())
    tempUsersRU2.rename(columns={0: "Count"}, inplace=True)

    tempUsersUA2 = UsersUA
    tempUsersUA2['CreationDate'] = pd.to_datetime(tempUsersUA2['CreationDate'], format="%Y-%m-%d")
    tempUsersUA2['CreationDate'] = tempUsersUA2['CreationDate'].dt.strftime('%Y-%m-%d')
    tempUsersUA2['CreationDate'] = pd.to_datetime(tempUsersUA2['CreationDate'], format="%Y-%m-%d")
    tempUsersUA2 = tempUsersUA2.loc[(tempUsersUA2['CreationDate'] >= '2022-02-01') &
                                    (tempUsersUA2['CreationDate'] < '2022-04-01')]
    tempUsersUA2 = pd.DataFrame(tempUsersUA2.groupby('CreationDate').size().reset_index())
    tempUsersUA2.rename(columns={0: "Count"}, inplace=True)

    plt.figure(figsize=(14, 7))
    plt.plot(tempUsersDE2.CreationDate, tempUsersDE2.Count, label='German')
    plt.plot(tempUsersRU2.CreationDate, tempUsersRU2.Count, label='Russian')
    plt.plot(tempUsersUA2.CreationDate, tempUsersUA2.Count, label='Ukrainian')
    plt.legend()
    plt.xlabel('Day')
    plt.ylabel('Number of users between 2022-02-01 and 2022-03-31')
    plt.title("Users")
    plt.grid()

##### Where are users of each website from?
##### How many of them are from countries that have these languages as an official language and how many of them are from Poland?
##### Where are top 10 users from?

### Users from countries that have German as an official language

def Plot7(UsersDE):
    droppedUsersDE = UsersDE
    droppedUsersDE.dropna(subset=['Location'], inplace=True)
    AustriaUsersDE = droppedUsersDE['Location'].str.match('Austria')
    ÖsterreichUsersDE = droppedUsersDE['Location'].str.match('Österreich')
    BelgiumUsersDE = droppedUsersDE['Location'].str.match('Belgium')
    BelgienUsersDE = droppedUsersDE['Location'].str.match('Belgien')
    LiechtensteinUsersDE = droppedUsersDE['Location'].str.match('Liechtenstein')
    LuxembourgUsersDE = droppedUsersDE['Location'].str.match('Luxembourg')
    LuxemburgUsersDE = droppedUsersDE['Location'].str.match('Luxemburg')
    GermanyUsersDE = droppedUsersDE['Location'].str.match('Germany')
    DeutschlandUsersDE = droppedUsersDE['Location'].str.match('Deutschland')
    SwitzerlandUsersDE = droppedUsersDE['Location'].str.match('Switzerland')
    SchweizUsersDE = droppedUsersDE['Location'].str.match('Schweiz')

    germanCount = sum(AustriaUsersDE == True) + sum(ÖsterreichUsersDE == True) + sum(BelgiumUsersDE == True) + \
                  sum(BelgienUsersDE == True) + sum(SwitzerlandUsersDE == True) + sum(SchweizUsersDE == True) + \
                  sum(LuxembourgUsersDE == True) + sum(LuxemburgUsersDE == True) + sum(GermanyUsersDE == True) + \
                  sum(DeutschlandUsersDE == True) + sum(LiechtensteinUsersDE == True)

    y = np.array([sum(AustriaUsersDE == True) + sum(ÖsterreichUsersDE == True), sum(BelgiumUsersDE == True) +
                  sum(BelgienUsersDE == True), sum(SwitzerlandUsersDE == True) + sum(SchweizUsersDE == True),
                  sum(LuxembourgUsersDE == True) + sum(LuxemburgUsersDE == True), sum(GermanyUsersDE == True) +
                  sum(DeutschlandUsersDE == True), sum(LiechtensteinUsersDE == True)])
    y = y * 100 / germanCount
    mylabels = ["Austria", "Belgium", "Switzerland", "Luxembourg", "Germany", "Liechtenstein"]

    plt.pie(y, labels=mylabels, autopct='%1.1f%%')
    plt.title("Users from countries that have German as an official language")
    plt.legend()
    plt.show()

### Users of german.stackexchange.com

def Plot8(UsersDE):
    droppedUsersDE = UsersDE
    droppedUsersDE.dropna(subset=['Location'], inplace=True)
    AustriaUsersDE = droppedUsersDE['Location'].str.match('Austria')
    ÖsterreichUsersDE = droppedUsersDE['Location'].str.match('Österreich')
    BelgiumUsersDE = droppedUsersDE['Location'].str.match('Belgium')
    BelgienUsersDE = droppedUsersDE['Location'].str.match('Belgien')
    LiechtensteinUsersDE = droppedUsersDE['Location'].str.match('Liechtenstein')
    LuxembourgUsersDE = droppedUsersDE['Location'].str.match('Luxembourg')
    LuxemburgUsersDE = droppedUsersDE['Location'].str.match('Luxemburg')
    GermanyUsersDE = droppedUsersDE['Location'].str.match('Germany')
    DeutschlandUsersDE = droppedUsersDE['Location'].str.match('Deutschland')
    SwitzerlandUsersDE = droppedUsersDE['Location'].str.match('Switzerland')
    SchweizUsersDE = droppedUsersDE['Location'].str.match('Schweiz')
    PolandUsersDE = droppedUsersDE['Location'].str.match('Poland')
    PolenUsersDE = droppedUsersDE['Location'].str.match('Polen')
    PolskaUsersDE = droppedUsersDE['Location'].str.match('Polska')

    germanCount = sum(AustriaUsersDE == True) + sum(ÖsterreichUsersDE == True) + sum(BelgiumUsersDE == True) + \
                  sum(BelgienUsersDE == True) + sum(SwitzerlandUsersDE == True) + sum(SchweizUsersDE == True) + \
                  sum(LuxembourgUsersDE == True) + sum(LuxemburgUsersDE == True) + sum(GermanyUsersDE == True) + \
                  sum(DeutschlandUsersDE == True) + sum(LiechtensteinUsersDE == True)

    UsersDE = pd.read_xml("UsersDE.xml")
    y = np.array([germanCount, sum(PolandUsersDE == True) + sum(PolenUsersDE == True) + sum(PolskaUsersDE == True),
                  droppedUsersDE.shape[0] - sum(PolandUsersDE == True) - sum(PolenUsersDE == True) - sum(
                      PolskaUsersDE == True) - \
                  germanCount, UsersDE.shape[0] - droppedUsersDE.shape[0]])
    y = y * 100 / UsersDE.shape[0]
    mylabels = ["German speaking countries", "Poland", "Other countries", "Na/NaN"]

    plt.pie(y, labels=mylabels, autopct='%1.1f%%')
    plt.title("Users of german.stackexchange.com")
    plt.legend()
    plt.show()

### Users from countries that have Russian as an official language

def Plot9(UsersRU):
    droppedUsersRU = UsersRU
    droppedUsersRU.dropna(subset=['Location'], inplace=True)
    RussiaUsersRU = droppedUsersRU['Location'].str.match('Russia')
    РоссияUsersRU = droppedUsersRU['Location'].str.match('Россия')
    BelarusUsersRU = droppedUsersRU['Location'].str.match('Belarus')
    БелоруссияUsersRU = droppedUsersRU['Location'].str.match('Белоруссия')
    БеларусьUsersRU = droppedUsersRU['Location'].str.match('Беларусь')
    KazakhstanUsersRU = droppedUsersRU['Location'].str.match('Kazakhstan')
    КазахстанUsersRU = droppedUsersRU['Location'].str.match('Казахстан')
    KyrgyzstanUsersRU = droppedUsersRU['Location'].str.match('Kyrgyzstan')
    КиргизияUsersRU = droppedUsersRU['Location'].str.match('Киргизия')

    russianCount = sum(RussiaUsersRU == True) + sum(РоссияUsersRU == True) + sum(BelarusUsersRU == True) + \
                   sum(БелоруссияUsersRU == True) + sum(БеларусьUsersRU == True) + sum(KazakhstanUsersRU == True) + \
                   sum(КазахстанUsersRU == True) + sum(KyrgyzstanUsersRU == True) + sum(КиргизияUsersRU == True)

    y = np.array([sum(RussiaUsersRU == True) + sum(РоссияUsersRU == True), sum(BelarusUsersRU == True) +
                  sum(БелоруссияUsersRU == True) + sum(БеларусьUsersRU == True), sum(KazakhstanUsersRU == True) +
                  sum(КазахстанUsersRU == True), sum(KyrgyzstanUsersRU == True) + sum(КиргизияUsersRU == True)])
    y = y * 100 / russianCount
    mylabels = ["Russia", "Belarus", "Kazakhstan", "Kyrgyzstan"]

    plt.pie(y, labels=mylabels, autopct='%1.1f%%')
    plt.title("Users from countries that have Russian as an official language")
    plt.legend()
    plt.show()

### Users of russian.stackexchange.com

def Plot10(UsersRU):
    droppedUsersRU = UsersRU
    droppedUsersRU.dropna(subset=['Location'], inplace=True)
    RussiaUsersRU = droppedUsersRU['Location'].str.match('Russia')
    РоссияUsersRU = droppedUsersRU['Location'].str.match('Россия')
    BelarusUsersRU = droppedUsersRU['Location'].str.match('Belarus')
    БелоруссияUsersRU = droppedUsersRU['Location'].str.match('Белоруссия')
    БеларусьUsersRU = droppedUsersRU['Location'].str.match('Беларусь')
    KazakhstanUsersRU = droppedUsersRU['Location'].str.match('Kazakhstan')
    КазахстанUsersRU = droppedUsersRU['Location'].str.match('Казахстан')
    KyrgyzstanUsersRU = droppedUsersRU['Location'].str.match('Kyrgyzstan')
    КиргизияUsersRU = droppedUsersRU['Location'].str.match('Киргизия')
    PolandUsersRU = droppedUsersRU['Location'].str.match('Poland')
    ПольшаUsersRU = droppedUsersRU['Location'].str.match('Польша')
    PolskaUsersRU = droppedUsersRU['Location'].str.match('Polska')

    russianCount = sum(RussiaUsersRU == True) + sum(РоссияUsersRU == True) + sum(BelarusUsersRU == True) + \
                   sum(БелоруссияUsersRU == True) + sum(БеларусьUsersRU == True) + sum(KazakhstanUsersRU == True) + \
                   sum(КазахстанUsersRU == True) + sum(KyrgyzstanUsersRU == True) + sum(КиргизияUsersRU == True)

    UsersRU = pd.read_xml("UsersRU.xml")
    y = np.array([russianCount, sum(PolandUsersRU == True) + sum(ПольшаUsersRU == True) + sum(PolskaUsersRU == True),
                  droppedUsersRU.shape[0] - sum(PolandUsersRU == True) - sum(ПольшаUsersRU == True) - sum(
                      PolskaUsersRU == True) - \
                  russianCount, UsersRU.shape[0] - droppedUsersRU.shape[0]])
    y = y * 100 / UsersRU.shape[0]
    mylabels = ["Russian speaking countries", "Poland", "Other countries", "Na/NaN"]

    plt.pie(y, labels=mylabels, autopct='%1.1f%%')
    plt.title("Users of russian.stackexchange.com")
    plt.legend()
    plt.show()

### Users of ukrainian.stackexchange.com

def Plot11(UsersUA):
    droppedUsersUA = UsersUA
    droppedUsersUA.dropna(subset=['Location'], inplace=True)
    UkraineUsersUA = droppedUsersUA['Location'].str.match('Ukraine')
    УкраїнаUsersUA = droppedUsersUA['Location'].str.match('Україна')
    PolandUsersUA = droppedUsersUA['Location'].str.match('Poland')
    ПольщаUsersUA = droppedUsersUA['Location'].str.match('Польща')
    PolskaUsersUA = droppedUsersUA['Location'].str.match('Polska')

    UsersUA = pd.read_xml("UsersUA.xml")
    y = np.array([sum(UkraineUsersUA == True) + sum(УкраїнаUsersUA == True), sum(PolandUsersUA == True) +
                  sum(ПольщаUsersUA == True) + sum(PolskaUsersUA == True),
                  droppedUsersUA.shape[0] - sum(PolandUsersUA == True) - sum(ПольщаUsersUA == True) - sum(
                      PolskaUsersUA == True) -
                  sum(UkraineUsersUA == True) - sum(УкраїнаUsersUA == True),
                  UsersUA.shape[0] - droppedUsersUA.shape[0]])
    y = y * 100 / UsersUA.shape[0]
    mylabels = ["Ukraine", "Poland", "Other countries", "Na/NaN"]

    plt.pie(y, labels=mylabels, autopct='%1.1f%%')
    plt.title("Users of ukrainian.stackexchange.com")
    plt.legend()
    plt.show()

### Users from Poland of the considered stackexchange.com websites

def Plot12(UsersDE, UsersRU, UsersUA):
    droppedUsersDE = UsersDE
    droppedUsersDE.dropna(subset=['Location'], inplace=True)
    droppedUsersRU = UsersRU
    droppedUsersRU.dropna(subset=['Location'], inplace=True)
    droppedUsersUA = UsersUA
    droppedUsersUA.dropna(subset=['Location'], inplace=True)

    PolandUsersDE = droppedUsersDE['Location'].str.match('Poland')
    PolenUsersDE = droppedUsersDE['Location'].str.match('Polen')
    PolskaUsersDE = droppedUsersDE['Location'].str.match('Polska')
    PolandUsersRU = droppedUsersRU['Location'].str.match('Poland')
    ПольшаUsersRU = droppedUsersRU['Location'].str.match('Польша')
    PolskaUsersRU = droppedUsersRU['Location'].str.match('Polska')
    PolandUsersUA = droppedUsersUA['Location'].str.match('Poland')
    ПольщаUsersUA = droppedUsersUA['Location'].str.match('Польща')
    PolskaUsersUA = droppedUsersUA['Location'].str.match('Polska')

    y = np.array([sum(PolandUsersDE == True) + sum(PolenUsersDE == True) + sum(PolskaUsersDE == True),
                  sum(PolandUsersRU == True) + sum(ПольшаUsersRU == True) + sum(PolskaUsersRU == True),
                  sum(PolandUsersUA == True) + sum(ПольщаUsersUA == True) + sum(PolskaUsersUA == True)])
    mylabels = ["German", "Russian", "Ukrainian"]

    plt.bar(mylabels, y, color='green', width=0.4)
    plt.title("Users from Poland of the considered stackexchange.com websites")
    plt.grid()

### Declared locations of top 10 users of german.stackexchange.com (considering number of posts)

def Table1(PostsDE, UsersDE):
    Posts1DE = PostsDE.loc[:, ['OwnerUserId']]
    Users1DE = UsersDE.loc[:, ['Id', 'Location']]

    xDE = Posts1DE.set_index('OwnerUserId').join(Users1DE.set_index('Id'))
    xDE = xDE.loc[xDE["Location"] != '']
    xDE = xDE.groupby('Location').size().reset_index()  # resetting indices to get DataFrame

    xDE.rename(columns={0: "Count"}, inplace=True)
    xDE = xDE.sort_values(by='Count', ascending=False).reset_index(drop=True).head(10)

    return xDE

### Declared locations of top 10 users of german.stackexchange.com (considering number of posts)

def Plot13(xDE):
    xDE = xDE.sort_values(by='Count', ascending=True)

    plt.figure(figsize=(16, 9))
    plt.barh(xDE.Location, xDE.Count, color='maroon')
    for i, v in enumerate(xDE.Count):
        plt.text(v + 25, i, str(v), color='black', fontweight='bold')
    plt.title("Declared locations of top 10 users of german.stackexchange.com (considering number of posts)")

### Declared locations of top 10 users of russian.stackexchange.com (considering number of posts)

def Table2(PostsRU, UsersRU):
    Posts1RU = PostsRU.loc[:, ['OwnerUserId']]
    Users1RU = UsersRU.loc[:, ['Id', 'Location']]

    xRU = Posts1RU.set_index('OwnerUserId').join(Users1RU.set_index('Id'))
    xRU = xRU.loc[xRU["Location"] != '']
    xRU = xRU.groupby('Location').size().reset_index()  # resetting indices to get DataFrame

    xRU.rename(columns={0: "Count"}, inplace=True)
    xRU = xRU.sort_values(by='Count', ascending=False).reset_index(drop=True).head(10)

    return xRU

### Declared locations of top 10 users of russian.stackexchange.com (considering number of posts)

def Plot14(xRU):
    xRU = xRU.sort_values(by='Count', ascending=True)

    plt.figure(figsize=(16, 9))
    plt.barh(xRU.Location, xRU.Count, color='maroon')
    for i, v in enumerate(xRU.Count):
        plt.text(v + 10, i, str(v), color='black', fontweight='bold')
    plt.title("Declared locations of top 10 users of russian.stackexchange.com (considering number of posts)")

### Declared locations of top 10 users of ukrainian.stackexchange.com (considering number of posts)

def Table3(PostsUA, UsersUA):
    Posts1UA = PostsUA.loc[:, ['OwnerUserId']]
    Users1UA = UsersUA.loc[:, ['Id', 'Location']]

    xUA = Posts1UA.set_index('OwnerUserId').join(Users1UA.set_index('Id'))
    xUA = xUA.loc[xUA["Location"] != '']
    xUA = xUA.groupby('Location').size().reset_index()  # resetting indices to get DataFrame

    xUA.rename(columns={0: "Count"}, inplace=True)
    xUA = xUA.sort_values(by='Count', ascending=False).reset_index(drop=True).head(10)

    return xUA

### Declared locations of top 10 users of ukrainian.stackexchange.com (considering number of posts)

def Plot15(xUA):
    xUA = xUA.sort_values(by='Count', ascending=True)

    plt.figure(figsize=(16, 9))
    plt.barh(xUA.Location, xUA.Count, color='maroon')
    for i, v in enumerate(xUA.Count):
        plt.text(v + 5, i, str(v), color='black', fontweight='bold')
    plt.title("Declared locations of top 10 users of ukrainian.stackexchange.com (considering number of posts)")
