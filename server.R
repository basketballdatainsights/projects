#NBA Standings as Example Shiny App for Dr. Bornn
# Author: Alex Beene

#Packages
library(XML)
library(httr)

###      Standings from basketball-reference
url <- "http://www.basketball-reference.com/leagues/NBA_2018_ratings.html"
tabs <- GET(url)
standings <- readHTMLTable(rawToChar(tabs$content), stringsAsFactors = F)

#Store as dataframe of 30 NBA teams
standings <- as.data.frame(standings)

#Store opponent
standings$opp <- ifelse(standings$ratings.Team == "Golden State Warriors", "GSW",
                        ifelse(standings$ratings.Team == "San Antonio Spurs", "SAS",
                               ifelse(standings$ratings.Team == "Houston Rockets", "HOU",
                                      ifelse(standings$ratings.Team == "Cleveland Cavaliers", "CLE", 
                                             ifelse(standings$ratings.Team == "Toronto Raptors", "TOR",
                                                    ifelse(standings$ratings.Team == "Utah Jazz", "UTA",
                                                           ifelse(standings$ratings.Team == "Los Angeles Clippers", "LAC",
                                                                  ifelse(standings$ratings.Team == "Boston Celtics", "BOS",
                                                                         ifelse(standings$ratings.Team == "Memphis Grizzlies", "MEM",
                ifelse(standings$ratings.Team == "Washington Wizards", "WAS",
                       ifelse(standings$ratings.Team == "Charlotte Hornets", "CHA",
                              ifelse(standings$ratings.Team == "Milwaukee Bucks", "MIL",
                                     ifelse(standings$ratings.Team == "Chicago Bulls", "CHI",
                                            ifelse(standings$ratings.Team == "Detroit Pistons", "DET", 
                                                   ifelse(standings$ratings.Team == "Indiana Pacers", "IND",
                                                          ifelse(standings$ratings.Team == "Denver Nuggets", "DEN",
                                                                 ifelse(standings$ratings.Team == "Atlanta Hawks", "ATL",
                                                                        ifelse(standings$ratings.Team == "Miami Heat", "MIA",
                                                                               ifelse(standings$ratings.Team == "Minnesota Timberwolves", "MIN",
              ifelse(standings$ratings.Team == "Portland Trail Blazers", "POR",
                     ifelse(standings$ratings.Team == "Dallas Mavericks", "DAL",
                            ifelse(standings$ratings.Team == "Sacramento Kings", "SAC",
                                   ifelse(standings$ratings.Team == "New Orleans Pelicans", "NOP",
                                          ifelse(standings$ratings.Team == "New York Knicks", "NYK", 
                                                 ifelse(standings$ratings.Team == "Phoenix Suns", "PHX",
                                                        ifelse(standings$ratings.Team == "Los Angeles Lakers", "LAL",
                                                               ifelse(standings$ratings.Team == "Orlando Magic", "ORL",
                                                                      ifelse(standings$ratings.Team == "Philadelphia 76ers", "PHI",
                                                                             ifelse(standings$ratings.Team == "Brooklyn Nets", "BKN",
                                                                                    ifelse(standings$ratings.Team == "Oklahoma City Thunder", "OKC",
                                                                                           "NA" #NA if one of the opponent names weren't listed
                                                                                           
                                                                                           
                                                                                   ))))))))))))))))))))))))))))))

#Store win percentage as a number
standings$ratings.W.L. <- as.numeric( as.character(standings$ratings.W.L.) ) 

standings <- transform(standings, 
                       ConfRank = ave(ratings.W.L., ratings.Conf, 
                                      FUN = function(x) rank(-x, ties.method = "first")))

standings <- transform(standings, 
                       DivRank = ave(ratings.W.L., ratings.Div, 
                                     FUN = function(x) rank(-x, ties.method = "first")))


names(standings) <- c("Rank","Team","Conf",  "Div","W",  "L",  "W-L" ,  "MOV"  ,  "ORtg" ,
                      "DRtg", "NRtg", "Adj MOV","Adj ORtg", "Adj DRtg", "Adj NRtg", "Tm","Conf Rank", "Div Rank")     


standings <- standings[,c(16,1,3,17,4,18,11,15,9,13,10,14,5,6,7,8,12)]

# Convert character variables to numeric
standings[,c(2,7:ncol(standings))] <- sapply( standings[,c(2,7:ncol(standings))], as.numeric )

shinyServer ( function(input, output) {
 
  
                                      output$standings <-  renderDataTable( 
                                        standings #Include only column headings
                                      )
  
  
}
)
