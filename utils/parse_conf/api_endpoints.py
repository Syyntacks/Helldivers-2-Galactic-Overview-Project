api_endpoints = {
    #########
    ##-RAW-##
    #########
    "war_id": {
        "path": "/raw/api/WarSeason/current/WarID" # Endpoint for the current Galactic War's ID.
    },
    "war_snapshot": {
        "path": "/raw/api/WarSeason/801/Status" # Endpoint for a snapshot of the Galactic War's status.
    },
    "war_info": {
        "path": "/raw/api/Wareason/801/WarInfo" #Endpoint for the Galactic War's info.
    },
    "war_summary": {
        "path": "/raw/api/Stats/war/801/summary" # Endpoint for a summary of the Galactic War.
    },
    "news_feed": {
        "path": "/raw/api/NewsFeed/801", # Endpoint for the Galactic War's News Feed.
    },
    "mo_overview": {
        "path": "/raw/api/v2/Assignment/War/801", # Endpoint for Major Order overview.
    },
    "space_station": {
        "path": "/raw/api/v2/SpaceStation/War/801/{index}", #index= 749875195
    },

    ########
    ##-V1-##
    ########
    "war_state": {
        "path": "/api/v1/war" # Endpoint for the Galactic War state.
    },
    "major_orders": {
        "path": "/api/v1/assignments" #Endpoint for all active Major Orders.
    },
    "selected_mo": {
        "path": "/api/v1/assignments/{index}" # Endpoint for specific active Major Order.
    },
    "avail_campaigns": {
        "path": "/api/v1/campaigns" # Endpoint for all available Campaigns (playable planets).
    },
    "selected_campaigns": {
        "path": "/api/v1/campaigns/{index}" # Endpoint for specific Campaign.
    },
    "hc_dispatches": {
        "path": "/api/v1/dispatches" # Endpoint for all available High Command Dispatches.
    },
    "selected_dispatch": {
        "path": "/api/v1/dispatches/{index}" # Endpoint for specific High Command Dispatch.
    },
    "planet_info": {
        "path": "/api/v1/planets" # Endpoint for all planets in Galaxy.
    },
    "selected_planet": {
        "path": "/api/v1/planets/{index}" # Endpoint for specific planet in Galaxy.
    },
    "planet_events": {
        "path": "/api/v1/planet-events" # Endpoint for all planet events available in the Galactic War.
    },
    "steam_newsfeed": {
        "path": "/api/v1/steam" # Endpoint for Steam's newsfeed for Helldivers 2.
    },
    "selected_steam_newsfeed": {
        "path": "/api/v1/steam/{grid}" # Endpoint for selected Steam newsfeed item.
    },

    ########
    ##-V2-##
    ########
    "released_dispatches": {
        "path": "/api/v2/dispatches" # Endpoint for all released High Command Dispatches.
    },
    "selected_released_dispatches": {
        "path": "/api/v2/dispatches/{index}" # Endpoint for selected released High Command Dispatch.
    },
    "space_station": {
        "path": "/api/v2/space-stations" # Endpoint for the DSS's details.
    },
    "selected_space_station": {
        "path": "/api/v2/space-stations/{index}" # Endpoint for the DSS's details by index.
    }
}