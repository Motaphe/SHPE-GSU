# scraper.py
import requests
from bs4 import BeautifulSoup

# scraper.py
def scrape_scholarships_for_stage(stage):
    """
    Return demo high school scholarships data with title, description, and URL.
    """
    if stage == "highschool senior":
        return [
            {
                "title": "Gates Scholarship (Full-ride)",
                "description": "A full-ride scholarship provided by The Gates Scholarship.",
                "url": "https://www.thegatesscholarship.org/"
            },
            {
                "title": "QuestBridge (Full-ride)",
                "description": "A full-ride scholarship offered through QuestBridge.",
                "url": "https://www.questbridge.org/"
            },
            {
                "title": "Posse Foundation Leadership Scholarship (Full-tuition)",
                "description": "Covers full tuition for selected students through leadership training.",
                "url": "https://www.possefoundation.org/"
            },
            {
                "title": "Cameron Impact Scholarship (Full-tuition)",
                "description": "A full-tuition scholarship provided by Cameron Impact.",
                "url": "https://www.cameronimpact.org/"
            },
            {
                "title": "Science Ambassador Scholarship (Full-tuition)",
                "description": "A full-tuition scholarship for aspiring scientists.",
                "url": "https://www.scienceambassador.org/"
            },
            {
                "title": "Horatio Alger Scholarship Programs ($10,000-$50,000)",
                "description": "Offers financial assistance ranging from $10,000 to $50,000.",
                "url": "https://scholars.horatioalger.org/"
            },
            {
                "title": "Burger King Scholars ($1,000-$50,000)",
                "description": "Scholarship awards ranging from $1,000 to $50,000 for qualified students.",
                "url": "https://www.burgerkingscholars.com/"
            },
            {
                "title": "Jack Kent Cooke Foundation College Scholarship Program ($40,000)",
                "description": "Provides up to $40,000 to support college expenses.",
                "url": "https://www.jkcf.org/our-scholarships/college-scholarship-program/"
            },
            {
                "title": "GE-Reagan Foundation Scholarship Program ($40,000)",
                "description": "Offers scholarships of up to $40,000.",
                "url": "https://www.reaganfoundation.org/"
            },
            {
                "title": "Ron Brown Scholarship ($40,000)",
                "description": "A prestigious scholarship program offering $40,000 awards.",
                "url": "https://ronbrown.org/"
            },
            {
                "title": "Jackie Robinson Foundation Scholarship Program (Up to $30,000)",
                "description": "Provides scholarship funds up to $30,000.",
                "url": "https://www.jackierobinson.org/"
            },
            {
                "title": "Daniels Scholarship Program ($7,500-$25,000)",
                "description": "Available for residents of Colorado, New Mexico, Utah, and Wyoming with awards from $7,500 to $25,000.",
                "url": "https://www.danielsscholarship.org/"
            }
        ]
    else:
        return []
