JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "POS Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "POS Header",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "POST Brand",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "Welcome to 3DShop",
    # Copyright on the footer
    "copyright": "Juan Delgado",
    # "search_model": ["product.Products",],
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [{"model": "auth.user"}],
    "order_with_respect_to": [
        "auth",
        "product",
        "product.Products",
        "product.ProductImages",
    ],
    # ICons
    # Icons that are used when one is not manually specified
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "product.Products": "fa-solid fa-boxes-stacked",
        "product.ProductImages": "fa-solid fa-image",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    
    
}
