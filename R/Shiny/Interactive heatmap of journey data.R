library(shiny)
library(shinydashboard)
library(ggplot2)
library(ggmap)
library(magrittr)
library(sp)
library(chron)

# Set the working directory
#setwd("/Users/charles.powell/Documents/Projects/TFGM/")

sampleData <- read.csv("journey_data.csv", header=TRUE)
names(sampleData) <- c('count','lon','lat','date','hour')

sampleData$Longitude <- round(as.numeric(sampleData$lon), 3)
sampleData$Latitude <- round(as.numeric(sampleData$lat), 3)

sampleData$date <- as.Date(sampleData$date, format = "%d/%m/%y")
sampleData$convertedDate <- as.numeric(as.POSIXct(sampleData$date))

dateRangeList <- seq(min(sampleData$date), max(sampleData$date), by="days")
wkends <- dateRangeList[is.weekend(dateRangeList)]
wkdays <- as.Date(setdiff(dateRangeList, wkends), origin = "1970-01-01")
wkends <- as.numeric(as.POSIXct(wkends))
wkdays <- as.numeric(as.POSIXct(wkdays))
wkendIndex <- c(which(sampleData$convertedDate %in% wkends))
wkdayIndex <- c(which(sampleData$convertedDate %in% wkdays))


ui <- dashboardPage(skin="green",
                    dashboardHeader(
                      title = "Transport for Greater Manchester", titleWidth = 350
                    ),
                    dashboardSidebar(width = 300,
                                     dateRangeInput(inputId = "inputdate", label="Select the date range", 
                                                    start = "2016-07-23", end = "2016-10-23", min = "2016-07-23", max = "2016-10-24",
                                                    format = "dd-mm-yyyy", startview = "month", weekstart = 0, language = "en", 
                                                    separator = "to", width = NULL),
                                     checkboxGroupInput(inputId="weekend", label="Weekdays or Weekends", choices = c("Weekdays", "Weekends"), 
                                                        selected = c("Weekdays", "Weekends"), inline = TRUE, width = "100%"),
                                     
                                     sliderInput(inputId = "time_range", label="Select a time of day:", animate = animationOptions(interval = 15000, loop = FALSE), min = 0, max = 24, value = c(7, 12)),
                                     
                                     
                                     verbatimTextOutput("info", placeholder = FALSE)

                    ),
                    
                    dashboardBody(
                      tags$style(type = "text/css", "#map {height: calc(100vh - 80px) !important;}"), 
                      plotOutput("mymap", height = 600, width = 700, click = "plot_click", 
                                 dblclick = "plot_dblclick", brush = brushOpts(id = "plot_brush", resetOnNew = TRUE))
                      
                      )
)

server <- function(input, output, session) {
  
  ranges <- reactiveValues(x = NULL, y = NULL)
  
  output$info <- renderText({
    
    xy_range_str <- function(e) {
      if(is.null(e)) return("Draw a box on the map and\ndouble click it to zoom in on it.\nDouble click again to zoom out.")
      paste0("xmin = ", round(e$xmin, 5), "\nxmax = ", round(e$xmax, 5), 
             "\nymin = ", round(e$ymin, 5), "\nymax = ", round(e$ymax, 5))
    }
    
    paste0(xy_range_str(input$plot_brush))
    
  })
  
  observeEvent(input$plot_dblclick, {
    brush <- input$plot_brush
    if (!is.null(brush)) {
      ranges$x <- c(brush$xmin, brush$xmax)
      ranges$y <- c(brush$ymin, brush$ymax)
      
    } else {
      ranges$x <- NULL
      ranges$y <- NULL
    }
  })
  
  output$mymap <- renderPlot({
    
    dateseq = seq(as.Date(input$inputdate[1]), as.Date(input$inputdate[2]), by="days")
    
    dateseq1 = as.POSIXct(dateseq)
    dateseq1 = as.numeric(dateseq1)
    dateindex = c(which(sampleData$convertedDate %in% dateseq1))
    
    hourindex = c(which(sampleData$hour %in% c(input$time_range[1]:(input$time_range[2]-1))))
    
    comidx = intersect(hourindex,dateindex)
    comidx_wkend = intersect(comidx, wkendIndex)
    comidx_wkday = intersect(comidx, wkdayIndex)
    
    if(input$weekend == c("Weekdays", "Weekends")){
      trimmedData <- sampleData[comidx,]
    } else if(input$weekend == "Weekends"){
      trimmedData <- sampleData[comidx_wkend,]
    } else if(input$weekend == "Weekdays"){
      trimmedData <- sampleData[comidx_wkday,]}
    
    #trimmedData <- sampleData[comidx,]
    
    eyeballs <- as.data.frame(table(trimmedData$Longitude, trimmedData$Latitude))
    names(eyeballs) <- c('Longitude', 'Latitude', 'Frequency')
    eyeballs$Longitude <- as.numeric(as.character(eyeballs$Longitude))
    eyeballs$Latitude <- as.numeric(as.character(eyeballs$Latitude))
    eyeballs <- subset(eyeballs, Frequency > 0)
    
    mancMap <- get_googlemap(center = c(-2.2426, 53.4808), zoom = 13, maptype = "terrain", 
                             style = 'feature:poi|element:labels|visibility:off&style=feature:administrative|element:labels|visibility:off' )
    
    ggmap(mancMap) + geom_tile(data = eyeballs, aes(x = Longitude, y = Latitude, alpha = Frequency), 
      fill = "blue") + theme(axis.title.y = element_blank(), axis.title.x = element_blank()) +
      coord_cartesian(xlim = ranges$x, ylim = ranges$y)
    
  })
  
}

runApp(shinyApp(ui, server), launch.browser = TRUE)
