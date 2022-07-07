from pages.FindCepPage import FindCepPage
from hamcrest import assert_that, equal_to, is_, is_not
from pages.Actions import *

EMPTY_STRING = ""

@step(u'I am on find address Home Page')
def step_impl(context):
    context.page_object = FindCepPage(context.driver)

@step(u'I type the following cep number: "{cep}"')
def step_impl(context, cep):
    context.page_object.type_in_cep_field(cep)


@when(u'I click on search button')
def step_impl(context):
    context.page_object.click_on_search_button()


@then(u'I verify that the following success message is displayed: "{message}"')
def step_impl(context, message):
    assert_that(context.page_object.get_success_message(), is_(message))
    

@then(u'I verify that all field are filled')
def step_impl(context):
    assert_that(len(context.page_object.get_public_area_type_value()) > 0)
    assert_that(len(context.page_object.get_public_area_value()) > 0)
    assert_that(len(context.page_object.get_neighborhood_value()) > 0)
    assert_that(len(context.page_object.get_city_value()) > 0)
    assert_that(len(context.page_object.get_uf_value()) > 0)
