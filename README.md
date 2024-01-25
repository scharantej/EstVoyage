## Build a Travel Planner to Estonia using Flask

### HTML Files

#### 1. index.html:
- This will serve as the application's homepage.
- It includes information about Estonia as a travel destination, with images and text content promoting its attractions.
- It contains a navigation bar with links to other pages of the site.

#### 2. places_to_visit.html:
- This page lists and describes popular tourist destinations in Estonia.
- Each entry includes information like the name, location, highlights, and tips for visitors.
- Users can click on a destination to learn more about it.

#### 3. things_to_do.html:
- This page focuses on various activities and experiences travelers can explore in Estonia.
- It covers outdoor activities, cultural attractions, museums, and more.
- Entries include details such as the activity, its location, timings, and costs.

#### 4. where_to_stay.html:
- This page provides information on accommodation options in Estonia.
- It lists hotels, guesthouses, vacation rentals, and hostels, along with their amenities and prices.
- Users can search for accommodations based on location, budget, and preferences.

#### 5. how_to_get_around.html:
- This page offers insights into transportation options for exploring Estonia.
- It covers public transportation, car rentals, day tours, and airport transfers.
- It includes travel times, costs, and tips for navigating the country.

#### 6. contact.html:
- This page contains information for users to contact the application maintainers.
- It includes a contact form where users can send inquiries, feedback, or suggestions.
- It also provides an email address and phone number for direct communication.

### Routes

#### 1. @app.route('/')
- This route is mapped to the homepage (index.html).
- It displays the main page of the travel planner application.

#### 2. @app.route('/places_to_visit')
- This route is mapped to the places_to_visit.html page.
- It displays a list of popular tourist destinations in Estonia, along with their descriptions and details.

#### 3. @app.route('/things_to_do')
- This route is mapped to the things_to_do.html page.
- It displays various activities and experiences travelers can explore in Estonia, along with their details.

#### 4. @app.route('/where_to_stay')
- This route is mapped to the where_to_stay.html page.
- It displays information on accommodation options in Estonia, including hotels, guesthouses, vacation rentals, and hostels.

#### 5. @app.route('/how_to_get_around')
- This route is mapped to the how_to_get_around.html page.
- It provides insights into transportation options for exploring Estonia, including public transportation, car rentals, day tours, and airport transfers.

#### 6. @app.route('/contact')
- This route is mapped to the contact.html page.
- It displays a contact form for users to send inquiries, feedback, or suggestions.
- It also includes an email address and phone number for direct communication.

#### 7. @app.route('/search')
- This route handles a search query from the user.
- It searches through the database of tourist destinations, activities, accommodations, and transportation options in Estonia.
- It returns a list of relevant results based on the user's query.