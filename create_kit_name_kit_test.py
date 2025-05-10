import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return  current_kit_body

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test1_create_kit_1_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test1_kit_name)
    positive_assert(current_kit_body)

def test2_create_kit_511_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test2_kit_name)
    positive_assert(current_kit_body)

def test3_create_kit_without_name():
    current_kit_body = get_kit_body(data.test3_kit_name)
    negative_assert_400(current_kit_body)

def test4_create_kit_512_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test4_kit_name)
    negative_assert_400(current_kit_body)

def test5_create_user_has_special_symbol_in_first_name_get_success_response():
    current_kit_body = get_kit_body(data.test5_kit_name)
    positive_assert(current_kit_body)

def test6_create_user_blank_space_between_letter_in_first_name_get_success_response():
     current_kit_body = get_kit_body(data.test6_kit_name)
     positive_assert(current_kit_body)

def test7_create_user_has_number_in_first_name_get_success_response():
    current_kit_body = get_kit_body(data.test7_kit_name)
    positive_assert(current_kit_body)

def test8_create_kit_without_name_parameter():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_400(current_kit_body)

def test9_create_kit_without_number_in_name_field():
    current_kit_body = get_kit_body(data.test9_kit_name)
    negative_assert_400(current_kit_body)