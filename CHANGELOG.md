# Changelog

## [v0.2.0] - 2025-10-17
+79 -50

### Added
- Added README.txt file for future documentation.
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

### Comments
- Need to alter how user interacts with information; cannot be automatic refresh, not all data is displayed.