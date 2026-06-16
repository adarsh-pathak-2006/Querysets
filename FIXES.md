# Fixes made

## App wiring
- Removed the duplicate `admin/` route from `core/urls.py` so the admin namespace is only defined once in the project URLconf.
- Added `LOGIN_URL`, `LOGIN_REDIRECT_URL`, and `LOGOUT_REDIRECT_URL` in `Django/settings.py` so `LoginRequiredMixin` and auth redirects resolve correctly.
- Normalized `STATIC_URL` to `/static/` and added a placeholder `static/` directory so Django's staticfiles check no longer warns.

## Authentication flow
- Fixed the registration logic in `core/views.py` so a new user is created when the username does not already exist.
- Added form validation feedback for missing fields, mismatched passwords, and duplicate usernames.
- Logged users in immediately after successful registration so the new account can reach the protected home page.
- Added invalid-login feedback instead of silently redirecting back to the login page.
- Redirected already-authenticated users away from the login and register pages.

## Templates
- Added error message rendering to `templates/login.html` and `templates/register.html`.
- Set the home page title in `templates/home.html`.
