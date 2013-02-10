from webapp2_extras.routes import RedirectRoute

# RedirectRoute(template,
# handler=None,
# name=None,
# defaults=None,
# build_only=False,
# handler_method=None,
# methods=None,
# schemes=None,
# redirect_to=None,
# redirect_to_name=None,
# strict_slash=False)

_routes = [

    # index of resources / collection of resources
    RedirectRoute('/resources/',
        handler='handlers.ResourceHandler',
        name='resource.index',
        defaults=None,
        handler_method='index',
        methods='GET',
        schemes=None,
        redirect_to=None,
        redirect_to_name=None,
        strict_slash=True),

    # display input to create a new resource
    # HTML Form Handler
    RedirectRoute('/resources/new/',
        handler='handlers.ResourceHandler',
        name='resource.new',
        defaults=None,
        handler_method='new',
        methods='GET',
        schemes=None,
        redirect_to=None,
        redirect_to_name=None,
        strict_slash=True),

    # display an existing resource
    RedirectRoute('/resources/<id>/',
        handler='handlers.ResourceHandler',
        name='resource.show',
        defaults=None,
        handler_method='show',
        methods='GET',
        schemes=None,
        redirect_to=None,
        redirect_to_name=None,
        strict_slash=True),

    # create a new resource via POST
    RedirectRoute('/resources/',
        handler='handlers.ResourceHandler',
        name='resource.create',
        defaults=None,
        handler_method='create',
        methods='POST',
        schemes=None,
        redirect_to=None,
        redirect_to_name=None,
        strict_slash=True),

    # edit an existing resource
    # HTML Form Handler
    RedirectRoute('/resources/<id>/edit/',
        handler='handlers.ResourceHandler',
        name='resource.edit',
        defaults=None,
        handler_method='edit',
        methods='GET',
        schemes=None,
        redirect_to=None,
        redirect_to_name=None,
        strict_slash=True),

    # POST/PUT updates to an existing resource
    # HTML Form Handler
    RedirectRoute('/resources/<id>/update/',
        handler='handlers.ResourceHandler',
        name='resource.update',
        defaults=None,
        handler_method='update',
        methods='POST',
        schemes=None,
        redirect_to=None,
        redirect_to_name=None,
        strict_slash=True),

    # PUT updates to an existing resource
    # RESTful API Handler
    RedirectRoute('/resources/<id>/',
        handler='handlers.ResourceHandler',
        name='resource.update.api',
        defaults=None,
        handler_method='update',
        methods='PUT',
        schemes=None,
        redirect_to=None,
        redirect_to_name=None,
        strict_slash=True),

    # POST /delete to delete an existing resource
    # HTML Form Handler
    RedirectRoute('/resources/<id>/delete/',
        handler='handlers.ResourceHandler',
        name='resource.delete',
        defaults=None,
        handler_method='delete',
        methods='POST',
        schemes=None,
        redirect_to=None,
        redirect_to_name=None,
        strict_slash=True),

    # DELETE an existing resource
    # RESTful API Handler
    RedirectRoute('/resources/<id>/',
        handler='handlers.ResourceHandler',
        name='resource.delete.api',
        defaults=None,
        handler_method='delete',
        methods='DELETE',
        schemes=None,
        redirect_to=None,
        redirect_to_name=None,
        strict_slash=True),

    ]


def get_routes():
    return _routes


def add_routes(app):
    for r in _routes:
        app.router.add(r)



# Notes on route design
# ---------------------
# MVC
# Controller/Action/id

# webapp
# GET/POST

# Create
# POST /participants/create
# create_participant
# POST /api/participants

# Read
# GET /participants/<id>
# get_participant(id)
# GET /api/participants/<id>

# Update
# POST /participants/<id>/update
# update_participant(id)
# PUT /api/participants/<id>

# Delete
# POST /participants/<id>/delete
# delete_participant(id)
# DELETE /api/participants/<id>

################################

# REST
# /resource/state/<id>
# /user/profile/1
# GET, POST, PUT, DELETE

# Create
# POST /participants

# Read
# GET /participants/<id>

# Update
# PUT /participants/<id>

# Delete
# DELETE /participants/<id>

