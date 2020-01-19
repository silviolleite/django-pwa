# Changelog

## 0.1.0

 - Initial release

## 1.0.0

### Added
 - Unit tests
 - Option `Oritentation` on manifest.json
 - tox.ini
 - Coverage
 
 
 ## 1.0.1
 
 ### Added
 - Add django 2 requirement
 - Use templateviews instead of own implementations
 - Add content_types
 - Update `README.md`
 - Add `PWA_APP_FETCH_URL` 
 - Add default_config in `__init__.py`
 - Add basic serviceworker
 - Add default offline page and default icons
 ### Changed
 - Updated the unit tests
 
 ## 1.0.2
 
 ### Fixed
 - Fix tox.ini to install pypandoc
 ### Added
 - The support to splash screen for iOS Meta tags `apple-touch-startup-image`
 - Meta tag `mobile-web-app-capable`
 - Meta tag `application-name`
 - Meta tag `msapplication-TileColor` and `msapplication-TileImage` for win8
 - Meta tag `rel="icon"` with default icon
 - Images for splash screen
 - Include the new images to `serviceworker.js`
 ### Changed
  - Update `CHANGELOG.md`
  - Update `README.md`
  
 ## 1.0.3
 
 ### Fixed
 - Restored support to oldest Django versions
 
 ## 1.0.4
  
  ### Fixed
  - Fix problem of multiple service workers being registered over multiple URLs
  
 ## 1.0.5
  
  ### Added
  - Updated manifest.json by adding scope parameter.
  - Updated serviceworker.js add scope dynamic parameter

 ## 1.0.7

  ### Fixed
  - Fix PWA if app is not mounted in root of webserver
  ### Added
  - Allow use of view names in PWA_APP_SCOPE, PWA_START_URL, PWA_APP_FETCH_URL and PWA_APP_ROOT
