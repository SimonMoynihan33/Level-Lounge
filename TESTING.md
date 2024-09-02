## Bugs

### Bug 01
- Issue: `django.core.exceptions.ImproperlyConfigured: allauth.account.middleware.AccountMiddleware must be added to settings.MIDDLEWARE`.
- Cause: Django Allauth expected a specific middleware, `allauth.account.middleware.AccountMiddleware` to be added to 'MIDDLEWARE' settings.
- Fix: Add `'allauth.account.middleware.AccountMiddleware',`

### Bug 02
- Issue: 
```
ERRORS:
level_lounge.UserProfile.profile_picture: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
```