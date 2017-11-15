#Template for Shiny App

library(shiny)


fluidPage(
          tags$head(
  tags$link(rel = "shortcut icon", href = "kings.png"),
  tags$title("Kings | Standings")),
  
  titlePanel(
             
    #Overall Title and Two Images
    fluidRow(
      column(3,
             img(src = 'kings.png', height = 100, width = 100),
             align = "left"
      ),
      column(6,
             "NBA Standings", 
             align = "center",
             style = ({"vertical-align: bottom; font-size: 75px; weight: bold; color: (92, 103, 112); font-family: Assiduous"})
      ),
      column(3,
             img(src = 'nba.png', height = 70.7865, width = 100),
             align = "right"
      )
    )
  ),
  navbarPage("NBA Standings",
             
             tabPanel("Current Standings",
                      #Predictions' Tab
                      
                      fluidRow(
                        column(12,
                               dataTableOutput('standings'),
                               align = "center",
                               style = ({"vertical-align: top; font-size: 40px; color: rgb(90,45,128); font-family: Assiduous"})
                        )
                      )
                      
                     
                        )
      )
             
    )
            
