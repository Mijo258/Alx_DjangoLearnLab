# Django Security Implementation

This project implements several security best practices as required by the ALX curriculum.

## 1. Secure Settings (`settings.py`)
- `DEBUG` is set to `False` to prevent leakage of sensitive information.
- `ALLOWED_HOSTS` is configured to only serve the application from specific hosts.
- Additional security headers like `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, and `SECURE_CONTENT_TYPE_NOSNIFF` are enabled.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` are set to `True` to ensure cookies are only transmitted over HTTPS in a production environment.

## 2. CSRF Protection
- All forms that use the POST method include the `{% csrf_token %}` template tag to protect against Cross-Site Request Forgery attacks.

## 3. SQL Injection Prevention
- All database queries are performed using Django's ORM (e.g., `Book.objects.filter()`). This method automatically parameterizes queries, making the application safe from SQL injection vulnerabilities. No raw SQL strings are constructed from user input.

## 4. Content Security Policy (CSP)
- The `django-csp` library is used to implement a restrictive CSP. By default, content is only allowed to be loaded from the same origin (`'self'`), which helps to mitigate Cross-Site Scripting (XSS) attacks.