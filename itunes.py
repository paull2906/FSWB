import urllib.parse
import urllib.request
import json

SEARCH_URL = "https://itunes.apple.com/search"


def search_tracks(query, limit=10):
    # ruft die iTunes Search API auf, braucht keinen API Key
    params = urllib.parse.urlencode({
        "term": query, "media": "music", "entity": "song", "limit": limit
    })
    req = urllib.request.Request(
        f"{SEARCH_URL}?{params}", headers={"User-Agent": "LiveRecords/1.0"}
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read())
    return data.get("results", [])


def format_track(item):
    # baut aus der iTunes Antwort die Felder, die wir fuer einen Song brauchen
    return {
        "itunes_id":   str(item.get("trackId", "")),
        "title":       item.get("trackName", ""),
        "artist":      item.get("artistName", ""),
        "album":       item.get("collectionName", ""),
        "preview_url": item.get("previewUrl", ""),
        "cover_url":   item.get("artworkUrl100", "").replace("100x100", "300x300"),
    }
