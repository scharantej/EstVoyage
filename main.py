
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database with tourist destinations, activities, accommodations, and transportation options in Estonia
database = {
    "destinations": [
        {"name": "Tallinn", "location": "Northern Estonia", "highlights": ["Old Town", "Toompea Castle", "Kadriorg Park"]},
        {"name": "Tartu", "location": "Southern Estonia", "highlights": ["Town Hall Square", "University of Tartu", "Estonian National Museum"]},
        {"name": "Pärnu", "location": "Western Estonia", "highlights": ["Beach", "Vallikääru Waterfall", "Pärnu Museum"]}
    ],
    "activities": [
        {"name": "Hiking", "location": "Lahemaa National Park", "timings": "All year round", "cost": "Free"},
        {"name": "Canoeing", "location": "Emajõgi River", "timings": "May to September", "cost": "€20 per person"},
        {"name": "Visiting museums", "location": "Tallinn", "timings": "Varies by museum", "cost": "€5-10 per museum"}
    ],
    "accommodations": [
        {"name": "Hotel Viru", "location": "Tallinn", "amenities": ["Wi-Fi", "Restaurant", "Bar"], "price": "€100 per night"},
        {"name": "Tartu Hotel", "location": "Tartu", "amenities": ["Wi-Fi", "Breakfast included", "Parking"], "price": "€70 per night"},
        {"name": "Pärnu Beach Hostel", "location": "Pärnu", "amenities": ["Wi-Fi", "Shared kitchen", "Laundry facilities"], "price": "€20 per night"}
    ],
    "transportation": [
        {"name": "Public transportation", "options": ["Bus", "Train", "Tram"], "cost": "€2-3 per ride"},
        {"name": "Car rental", "options": ["Small car", "SUV", "Luxury car"], "cost": "€30-100 per day"},
        {"name": "Day tours", "options": ["Tallinn City Tour", "Tartu Day Trip", "Pärnu Beach Excursion"], "cost": "€50-100 per person"}
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/places_to_visit')
def places_to_visit():
    return render_template('places_to_visit.html', destinations=database['destinations'])

@app.route('/things_to_do')
def things_to_do():
    return render_template('things_to_do.html', activities=database['activities'])

@app.route('/where_to_stay')
def where_to_stay():
    return render_template('where_to_stay.html', accommodations=database['accommodations'])

@app.route('/how_to_get_around')
def how_to_get_around():
    return render_template('how_to_get_around.html', transportation=database['transportation'])

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    results = []
    for category in database:
        for item in database[category]:
            if query in item['name'] or query in item['location'] or query in item['highlights'] or query in item['amenities'] or query in item['options']:
                results.append(item)
    return render_template('search_results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
