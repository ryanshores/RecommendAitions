
SYSTEM_PROMPT = """
You are a content recommendation engine.
Only recommend from the provided list.
Do not invent movies or shows.
Rank results based on user preferences.
Explain briefly why each recommendation fits.
"""

def build_prompt(titles, user_profile):
    title_list = [
        {
            'title': t.get('title') or t.get('name'),
            'overview': t.get('overview'),
            'genres': t.get('genre_ids'),
            'release_date': (t.get('release_date') or t.get('first_air_date')),
            'vote_average': t.get('vote_average'),
            'vote_count': t.get('vote_count'),
            'popularity': t.get('popularity'),
        }
        for t in titles
    ]

    return f"""
User Preferences: {user_profile}

Title List: {title_list}

Return top {user_profile["max_results"]} recommendations.
"""