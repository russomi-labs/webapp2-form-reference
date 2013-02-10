import webapp2
import logging
from webapp2_extras import jinja2
from google.appengine.ext import ndb

from wtforms import Form
from wtforms import TextField
from wtforms import BooleanField
from wtforms import validators
from wtforms.ext.appengine.ndb import model_form


class BaseHandler(webapp2.RequestHandler):
    """
    BaseHandler for all request RequestHandlers
    """
    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, context=None):
        context = context or {}

        extra_context = {
          'request': self.request,
          'uri_for': self.uri_for,
        }

        # Only override extra context stuff if it's not set by the template:
        for key, value in extra_context.items():
            if key not in context:
                context[key] = value

        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class ResourceModel(ndb.Model):
    """
    A simple Resource Model
    """
    id = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    actve = ndb.BooleanProperty()


class ResourceForm(Form):
    """
    A simple ResourceForm
    """
    id = TextField(label='Resource ID',
                   validators=[validators.required(), validators.length(max=10)],
                   description='This is the id of the resource.')
    name = TextField(label='Resource Name',
                   validators=[validators.required(), validators.length(max=10)],
                   description='This is the name of the resource.')
    description = TextField(label='Resource Description',
                   validators=[validators.required(), validators.length(max=10)],
                   description='This is the description of the resource.')
    active = BooleanField(label='Active',
                    description='This determines if the resource is active.')


class ResourceHandler(BaseHandler):
    """
    ResourceHandler Reference

    There are 7 standard methods:
        index - GET /resources/
        show - GET /resources/{id}/
        edit - GET /resources/{id}/{action}/
        new - GET /resources/new/
        create - POST /resources/
        update - POST/PUT /resources/{id}/{action}/
        delete - POST/DELETE /resources/{id}/{action}/

    """
    # @webapp2.cached_property
    # def form(self):
    #     """
    #     Reference to the WTForm object

    #     This is used to inject self.form
    #     into the template context.
    #     """
    #     # Generate a form based on the model.
    #     ResourceModelForm = model_form(ResourceModel)
    #     # create and return an instance of the form based on
    #     # the ResourceModel
    #     return ResourceModelForm

    def index(self):
        """
        Index method

        Display a list of resources

        """
        self.render_response('resource.html')

    def new(self):
        """
        New method

        Gather input to create a new resource

        """
        resource_model_form = model_form(ResourceModel)
        form = resource_model_form(self.request.POST)

        context = {
            'action': 'New',
            'form': form,
            'submit_routename': 'resource.create'
        }

        self.render_response('resource.html', context)

    def create(self):
        """
        Create method

        Create a new resource using posted data

        """
        # create form instance from the ResourceModel
        resource_model_form = model_form(ResourceModel)
        form = resource_model_form(self.request.POST)

        context = {
            'action': 'New',
            'form': form,
            'submit_routename': 'resource.create'
        }

        # since this method is only called from a post,
        # we do not need to check for request.method == "POST"
        # if self.form.validate() returns true, then save
        # the data
        if form.validate():
            logging.debug('Form Validated!')
            entity = ResourceModel()
            # push form values into model
            form.populate_obj(entity)
            # save to data store
            key = entity.put()
            # redirect to index and/or edit form with new id
            logging.debug('key={0}'.format(key))
            # redirect to the edit page for the created id
            return webapp2.redirect_to('resource.edit', id=key.id())

        # the form did not validate, redisplay with errors
        return self.render_response('resource.html', context)

    def show(self, id):
        """
        Show method

        Show a specific resource by id

        """
        context = {
            'action': 'Show',
            'id': id
         }

        self.render_response('resource.html', context)

    def edit(self, id):
        """
        Edit method

        Edit a specific resource by id

        """
        entity_id = int(id)
        resource_model_form = model_form(ResourceModel)
        entity = ResourceModel.get_by_id(entity_id)
        form = resource_model_form(self.request.POST, obj=entity)

        context = {
            'action': 'Edit',
            'id': id,
            'form': form,
            'submit_routename': 'resource.update'
         }

        self.render_response('resource.html', context)

    def update(self, id):
        """
        Update method

        Update an existing resource by id
        Uses posted data from Edit method

        """
        # create form instance from the ResourceModel
        entity_id = int(id)
        resource_model_form = model_form(ResourceModel)
        entity = ResourceModel.get_by_id(entity_id)
        form = resource_model_form(self.request.POST, obj=entity)

        context = {
            'id': id,
            'action': 'Update',
            'form': form,
            'submit_routename': 'resource.update'
        }

        # since this method is only called from a post,
        # we do not need to check for request.method == "POST"
        # if self.form.validate() returns true, then save
        # the data
        if form.validate():
            logging.debug('Form Validated!')
            # push form values into model
            form.populate_obj(entity)
            # save to data store
            key = entity.put()
            # redirect to index and/or edit form with new id
            logging.debug('key={0}'.format(key))
            # redirect to the edit page for the created id
            return webapp2.redirect_to('resource.edit', id=key.id())

        # the form did not validate, redisplay with errors
        return self.render_response('resource.html', context)

    def delete(self, id):
        """
        New method

        Delete an existing resource by id

        """
        context = {'action': 'Delete'}
        self.render_response('resource.html', context)


# Backup
# class MainHandler(BaseHandler):

#     def get(self):
#         template_values = {
#             'key': 'value'
#         }

#         self.render_response('starter-template.html', template_values)


# class TemplateHandler(BaseHandler):
#     def get(self, template_name):

#         template_values = {
#             'key': 'value'
#         }

#         self.render_response(template_name + '.html', template_values)
