# Changelog

---
## [v0.2.2.0] - 2025-10-22


### Added
- Added `or {}` to `planet_data` variables so an empty list is returned if no data can be found, rather than crashing.


### Fixed
- ==MAJOR:== Fixed planet_data_parser.py's fetching error; now correctly collects planet data. Places fetching code into a `try` statement to handle errors without crashing the program. 




---
## [v0.2.1.3] - 2025-10-22
+36 -48

### Added
- Added `planet_parser: PlanetParser()` back to `parse_major_order_data()` function.
- Redefined all three dictionaries in `planet_data_parser.py`.

### Fixed
- Altered `for` loop that handles each planet and the parsing of information.




---
## [v0.2.1.1] - 2025-10-19
+5 -3

### Added


### Fixed
- Fixed `settings.urls.get` in `api_source.py` (url to urls).
- Removed `planet_parser: PlanetParser()` from `parse_major_order_data()` function.




---
## [v0.2.1] - 2025-10-19
+126 -50

### Added
- Created `index.html` to handle web app structure.
- Added `bg-stars.jpg` to resources for web app background.
- Created `styles.css` to handle web app's formatting/design.
- Defined the home page for API (`get_root()`).


### Fixed
- Changed variable name from `datapoint_names` to `display_name` in `galaxy_stats_parser.py`.
- Reformatted `planet_data_parser.py` to align more with `galaxy_stats_parser.py`'s structure.




---
## [v0.2.0.1] - 2025-10-17
+21 -0

### Added
- Created `CHANGELOG.md` to log changes.


### Fixed
- Changed `README.txt` to `README.md`.




---
## [v0.2.0] - 2025-10-17
+79 -50

### Added
- Created README.txt file for future documentation.
- Added `load_dotenv()` in `api_source.py`.
- `main_exe.py` parses through all planet information using the `PlanetParser` class (*first 5 planets printed as an example*).
- Added `PlanetParser()` class to `major_order_parser.py` to align the dictionaries.

### Fixed
- Project now sources .env file from `Path(__file__).resolve().parent.parent / '.env'` in `settings.py`.
- Major Orders in `main_exe.py` now displays the planet's name as well as its ID.
- Time values in the `format_duration_from_seconds(total_seconds)`
- Fixed error with `settings.url` calls (*settings.url => settings.urls*) across the board in `planet_data_parser.py`.
- Reformatted all three planet-stat dictionaries; checks to see if `key.isdigit()`, ignores otherwise.
- Fixed `.get` source for `combined_data`; changed `details.get` instances to `planet_detail.get`.