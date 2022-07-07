from pages.Actions import *

@given(u'I open the application')
def step_impl(context):
    context.page_object = HomeActions(context.driver)
    context.page_object.open_application(context.base_url)
