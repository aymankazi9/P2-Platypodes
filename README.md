# P2 - Platypodes COVID-19 Project 
* Welcome to our Trimester 2 project for COVID-19. 
* With the recent rise of COVID numbers, we want users to be informed of the extent to which COVID is harming populations.
* We wanted to make a interactive tracker to make COVID-19 data accessible to all in order to keep others educated about the crisis. 
* Other websites may be a bit difficult to navigate especially when cluttered with other health news rather than purely COVID-19 news. That's why we aim to create this clean website that will show you all the COVID-19 information that you will need to know!
* Learn more about our plan in the Project Plan below.

## Run Instructions
* Paste this link into your browser window or simply click on the link.
* [Website](http://76.176.59.167)
* [Portal to an Alternate Dimension?](http://76.176.59.167/home2/)

--------

## Git Instructions
* You can learn about running this project on your IDE in this section:
* Go to Code home and click on the green "Code" button.
* Click on the clipboard next to the Git url. 
* Open up your IDE and "Run from Version Control".
* Press "Ctrl + V" or "⌘ + V" and press the blue "Clone" button at the bottom.
* Once the project is opened up, be sure to change the interpreter to any version of Python 3. 
* Run the project from wsgi.py, and you're all set!

### Project Plan
* Here is where we started, we made a plan of action and hope to follow it closely and make this a COVID-19 tracker to be recokened with.
* [Project Plan](https://docs.google.com/document/d/1MceTKLU3TJTQg3PkqIcMLYa7U4R2ov4QtojF4i7mKLc/edit)

# Mini Code and Ticket Review
### Week of 2/15 - 2/19

## Homesite Navigation Redesign: [Karam's Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53052644)
* 

## Login and Signup Backend: [Isai's Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53687851)
* 

## FAQ Redesign: [Ayman's Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53052118)
* 

## Login/Signup/Feedback Redesign: [Pragadeesh's Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53688163)
* 



### More details for each of the completed ticket items can be found detailed in the COMPLETED section on the [Scrum Board](https://github.com/aymankazi9/P2-Platypodes/projects/1#column-12515206).

### Click on this [runtime link](http://76.176.59.167) or type the following into your browser: 76.176.59.167.

------------------

# Delivery of Easter Egg and Big Ticket Items
### Week of 2/1 - 2/5

## Easter Egg Landing Page: [Link to Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53688061)
* Picked new theme colors for the Easter Egg part of our website (Alternate Dimension)
  * Theme applied with [inline CSS](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/altdimension/home2.html#L8-L13) on the landing page.
  * Class as [container-fluid](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/altdimension/home2.html#L12) used to create landing image.
* To see the landing page, visit this [page](http://76.176.59.167/home2/) on our website.

## Easter Egg Aesthetics and Navigation: [Link to Ticket 1](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53688218) and [Link to Ticket 2](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-54295074)
* A new theme was developed (revolving around CB Theme) for the Easter Egg part of our website. 
  * New navbar designed with [new templates](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/altdimension/cspreflections.html). All new templates are organized under a new [basealt.html](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/basealt.html#L16-L43)
* A new template was added with frontend theme in mind. It uses [CSS](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/altdimension/cspreflections.html#L10-L207) to add another layer of user interactivity.
  * Card style layout was used to show all the developers of the project and cards flip over to show the descriptions of "Who we are as Computer Scientists" 
  * [Linear gradients](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/altdimension/cspreflections.html#L83-L88) were used throughout this template in order to create an amount of variation to create an aesthetic website. 
* Simply click on ["Who We Are"](http://76.176.59.167/CSPReflections/) to see our Reflections as Computer Scientists in the stylized layout.

#### JavaScript and CSS Styling (Cookies): [Link to Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-54295074)
* Having an appealing website is necessary in interacting with the user. Various JS and CSS elements were used to display our new information without losing the interest of the user. 
* The team used a completely different [theme](https://github.com/aymankazi9/P2-Platypodes/blob/c4f8939fdc72581684b5af0add6bdb8ee7aa17ad/templates/basealt.html#L16-L37) to make the Easter Egg stand out. 
  * Based off of College Board color scheme; a fitting theme since the Easter Egg will contain our AP Prep material.
  * CSS were heavily used in the ["Who Are We" page](https://github.com/aymankazi9/P2-Platypodes/blob/c4f8939fdc72581684b5af0add6bdb8ee7aa17ad/templates/altdimension/cspreflections.html#L9-L208). A new gradient background with thematic colors was used, as well as the color of the font. 
* A new Cookie feature was started:
  * JavaScript and some CSS was used to make a [cookie consent banner](https://github.com/aymankazi9/P2-Platypodes/blob/c4f8939fdc72581684b5af0add6bdb8ee7aa17ad/templates/base.html#L13-L16) which gave the user an option to view the [policy](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/misc/cookies.html) as well as a button to make the banner disappear.
* A Terms of Service and Privacy page was created to notify our users: [link](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/misc/tos%26p.html)
  * A [CSS gradient](https://github.com/aymankazi9/P2-Platypodes/blob/c4f8939fdc72581684b5af0add6bdb8ee7aa17ad/templates/misc/tos%26p.html#L9-L20) was used to display the text, and match with the mian theme of the website. 
* To see our Styling and Javascript in use, a banner will pop up as soon as you enter our [wesite](http://76.176.59.167) above the navbar. To view the new theme, click on the ["hidden portal"](http://76.176.59.167/home2/). To see the other new animations click on ["Who We Are"](http://76.176.59.167/CSPReflections/) in the Easter Egg.

## Sign-Up: [Link to Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53055671)
* CSS and HTML were used to create a [sign up](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/homesite/signup.html) form for users to input their personal information.
* User inputs were then placed into [table and stored in database](https://github.com/aymankazi9/P2-Platypodes/blob/main/storesignup.py).
* A connection between the sign up html file and python file was established in [view.py](https://github.com/aymankazi9/P2-Platypodes/blob/main/view.py) by defining action and setting parameters of function from store.py as user input fields.

### More details for each of the completed ticket items can found detailed in the COMPLETED section on the [Scrum Board](https://github.com/aymankazi9/P2-Platypodes/projects/1#column-12515206).

### Click on this [runtime link](http://76.176.59.167) or type the following into your browser: 76.176.59.167.

------------------

# Delivery of Running Code and Big Ticket Items
### Week of 1/11 - 1/15

## Frontend Aesthetics and Navigation: [Link to Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53052242)
* A single theme was used throughout the website.
  * The theme was designed based off of the home page. 
  * The pages are easy to access through the Navbar at the top.
* All the informational and technical pages use the same theme.
  * The [Login](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/loginpage.html#L97-L110) and [Sign Up](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/signup.html#L28-L62) pages have custom entry boxes and buttons to fit the theme.
  * The [Feedback form](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/feedback.html#L14-L33) also has similar properties to the login/sign up pages.
  * The [FAQ page](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/FAQ.html#L15-L47) uses the same color scheme as the rest of the site.
  * The tracker pages that we have also use a similar theme, which will also be used for the rest of trackers later on.
* Simply click around the navbar of our [website](http://76.176.59.167/) to see our theme at use.

## Covid-19 Statistics Database: [Link to Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53055671)
* Our team web-scraped data from informational Covid-19 wesites through the use of APIs.
  * The [scraped data](https://github.com/aymankazi9/P2-Platypodes/blob/main/stats.py#L5-L10) is stored in our [database](https://github.com/aymankazi9/P2-Platypodes/blob/main/platypodes.db). 
  * The data will later be [formatted](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/map.html#L18-L43) and [displayed](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/map.html#L77-L114) on our tracker pages and our map.
* Visit this link to view the databse: [Database Creation](https://github.com/aymankazi9/P2-Platypodes/blob/main/stats.py) and [Database](https://github.com/aymankazi9/P2-Platypodes/blob/main/platypodes.db)

## User-Interactive Map: [Link to Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53057424)
* This is a main feature for our website. Our map will display data from all of the states and will be available with a click of a button.
  * Coordinates of each vertex are placed within the HTML <area> [tags](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/map.html#L57-L59) to define the outline of the irregular shapes.
  * Scalable vector graphics (.svg) will later be used for the same conveniece on multiple devices. [Example](https://github.com/aymankazi9/P2-Platypodes/blob/main/static/us%20map.svg)
* To see the map in action, visit the [COVID-19 Map](http://76.176.59.167/test/) on our website.

## JavaScript and CSS Styling: [Link to Ticket](https://github.com/aymankazi9/P2-Platypodes/projects/1#card-53055900)
* Incorporating JS and CSS within our HTML files will enable our team to deliver information effectively. 
  * Our group used CSS to make a single theme for the website, 1) to reduce variance between our pages and make them look complete, and 2) simplify the code while expanding its use.
  * CSS were heavily used in the [News page](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/newspage.html#L15-L44). A new gradient background with thematic colors was used, as well as the color of the font. 
  * JavaScript was used to make a [timer](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/newspage.html#L67-L96) to display the time of release.
  * Example of CSS usage in our feedback form: [link](https://github.com/aymankazi9/P2-Platypodes/blob/main/templates/feedback.html#L14-L43)
* To see our Styling and Javascript in use, click around the different pages of our [wesite](http://76.176.59.167) in the navbar. To view the Javascript at work, click on the ["News"](http://76.176.59.167/newspage/) item on our navigation bar.

### More details for each of the completed ticket items can found detailed in the COMPLETED section on the [Scrum Board](https://github.com/aymankazi9/P2-Platypodes/projects/1#column-12515206).

### Click on this [runtime link](http://76.176.59.167) or type the following into your browser: 76.176.59.167.

__________________

## Project Record

### Scrum Board
* Big Ticket items are layed out here for the fundamentals of our project that are nonegotiable.
* Some parts of the scrum board include minor bits that can be taken out if necessary. This is an easy way to track the progress and how far we are getting into the project. It can also be used to recognize lagging behind in our project and straighten up before the deadline.
* [Scrum Board](https://github.com/aymankazi9/P2-Platypodes/projects/1?fullscreen=true)

### Project Log

#### January 2021
* **01/15/21**: Deployment is complete, users can now use an external IP to access the website without having to pull from git. Runtime link is as follows: http://76.176.59.167. Paste into your browser to access.
* **01/14/21**: Aesthetics 100% complete across the website. Every page carries the website's aesthetics. As of right now, the website's frontend materials are complete. Javascript also added to the News Page to create a gradient. May be utilizing that for other pages to come. Countdown timer added to News Page for interesting "Coming Soon" notification. Updated Feedback Forms to be more insightful of user feedback rather than just storing user data. Still requires backend support to file the feedback into the database.
* **01/13/21**: Added lots of CSS to login and signup page to fix the aesthetics on those pages. Need backend support for compiling data and being able to access logins. Javascript to be added very soon.
* **01/11/21**: Employment of CSS and beginning to think about the theme of the website. Current theme settled on: Navy Blue for the borders, Cream/Black for the text, light cream for the text entries, green for highlights on the website. CSS will be applied to various parts of the website eventually to fit a theme in the website.
* **01/07/21**: Etensive work done to creating tracker pages and connecting them to the US map. 4 states are currently defined: Calfornia, Florida, Texas, and New York. Data has yet to be forwarded to the frontend files, but the aesthetic portion of the tracker pages and map page is complete.
* **01/04/21**: Map template received changes on colors and theme in general. Map template is now all of United States, California map is removed. Map template id currently dysfunctional with no <area> defined at the moment.

#### December 2020
* **12/20/20**: New file added called stats.py. Used stats.py to create a databse stemming from the web scraped data that was created through iteration. More explanation of iteration of web scraped data into lists can be explored within code comments of the project. 
* **12/18/20**: Fully functional dropdown menu (finally!). CSS colors to add aesthetic to website that matched the image. Landing Page is complete and matches vision in aesthetics. Map test, developed a map that allows users to navigate throughout the trackers by the click of a map link in a visual representation.
Note: WIP test, this is not going to be the final result let alone the final trackers. Trackers for the website will most likely consist of states in the United States rather than cities in California or other major cities.
* **12/17/20**: Model.py and Jinja calls are fixed, issue with the classes that needed to be created. Source dictionary can now be successfuly pulled into templates. 
* **12/15/20**: Website run commands moved to wsgi.py for more ergonomic and inline functions. App routes are now being recgonized, issue caused by minor typo. New templates added and are linked to navbar in base.html. No content in these templates, they only extend from base as of right now. Added templates: newspage.html, loginpage.html, aboutus.html)
* **12/14/20**: Navigation bar added, worked on backend integration to the base.html navbar. More html templates coming soon to add more pages to the website. Issues: Website isn't working, issue with app routes, must be resolved in the future
* **12/11/20**: Completed the Project Plan and have all roles assigned to group members from the scrum board. Some peripheral goals are yet to be assigned, but those are in the final parts of this project. 
* **12/10/20**: Updated README.md of this repository and worked further on expanding Project Plan and getting it closer to the completion. Worked mostly on adding Big Ticket Items to scrum board and making sure everything is staying on track
* **12/09/20**: Worked on Project Plan and formulating ideas for implementing project. We learned more about SQLAlchemy and brainstormed ideas to use that in our project for creating the databse with the scraped data.
* **12/08/20**: Created project plan document and added minor items to begin the thought process and workflow thinking for our project.
* **12/04/20**: Brainstormed more ideas about project and was approved by the teacher. Our new idea will be a COVID-19 tracker that will be in an aethetically pleasing website. The database will be automatically updated. This process of database updates is explained in further detail in our scrum board and project plan which we will begin work on next week.
* **12/03/20**: Thought about project ideas for this trimester and came up with an ASCII Database with many games, arts, animations all based on ASCII and designed to implement database workflow.
* **12/01/20**: Repository was created, README.md added. No updates to README.md file or Repository as of yet. Users added from the team in order to begin work.
