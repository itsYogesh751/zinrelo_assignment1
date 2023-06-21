from unittest import TestCase
from assignmentv2 import AcmeWine,User,Order


class testCase(TestCase):

    def test_should_return_false_for_zipcode_with_consecutive_digits_in_forward_order(self):
        user=User("","","",'23456',"")
        value=user.zipcode_not_have_consecutive_digits()
        self.assertEquals(value,False)

    def test_should_return_true_for_zipcode_with_no_consecutive_digits(self):
        user=User("","","",'13594',"")
        value=user.zipcode_not_have_consecutive_digits()
        self.assertEquals(value,True)

    def test_should_return_false_for_zipcode_with_consecutive_digits_in_reverse_order(self):
        user=User("","","","24698","")
        value=user.zipcode_not_have_consecutive_digits()
        self.assertEquals(value,False)

    def test_should_return_false_for_invalid_email_address_with_only_username(self):
        user=User("","yogeshdiwate","","","")
        value=user.is_valid_email()
        self.assertEquals(value,False)

    def test_should_return_false_for_invalid_email_address_with_only_domain_name_and_no_username(self):
        user=User("","@gmail.com","","","")
        value=user.is_valid_email()
        self.assertEquals(value,False)

    def test_should_return_false_for_invalid_email_address_with_no_dot_in_domain_name(self):
        user=User("","user@gmailcom","","","")
        value=user.is_valid_email()
        self.assertEquals(value,False)

    def test_should_return_true_for_valid_email_address(self):
        user=User("","yogeshdiwate0@gmail.com","","","")
        value=user.is_valid_email()
        self.assertEquals(value,True)


    def test_should_return_false_for_order_with_excluded_state_as_attribute(self):
        user=User("","","","","NJ")
        value=user.is_not_in_restricted_state()
        self.assertEquals(value,False)

    def test_should_return_true_for_order_with_state_that_is_not_excluded_state(self):
        user=User("","","","","SC")
        value=user.is_not_in_restricted_state()
        self.assertEquals(value,True)

    def test_should_return_true_for_birthdate_which_is_not_first_monday_of_the_month(self):
        user=User("","","10/10/1976","","")
        value=user.is_valid_birthdate()
        self.assertEquals(value,True)

    def test_should_return_false_for_birthdate_which_is_on_first_monday_of_the_month(self):
        user=User("","","11/01/2021","","")
        value=user.is_valid_birthdate()
        self.assertEquals(value,False)

    def test_should_return_true_for_age_of_user_greater_than_21(self):
        user=User("","","12/22/1976","","")
        value=user.is_valid_age("2023-02-12")
        self.assertEquals(value,True)

    def test_should_return_false_for_age_of_user_less_than_21(self):
        user=User("","","12/22/2016","","")
        value=user.is_valid_age("2023-02-12")
        self.assertEquals(value,False)

    def test_should_return_false_for_age_of_user_for_exactly_21_considering_month(self):
        user=User("","","04/22/2002","","")  
        value=user.is_valid_age("2023-03-12")
        self.assertEquals(value,False)
