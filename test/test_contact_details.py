import re


def test_details_on_home_page(app):
   contact_from_home_page = app.contact.get_contact_list()[0]
   contact_from_edit_page = app.contact.get_contact_into_from_edit_page(0)
   assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
   assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
   assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
   assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)
   assert contact_from_home_page.email == contact_from_edit_page.email
   assert contact_from_home_page.email2 == contact_from_edit_page.email2
   assert contact_from_home_page.email3 == contact_from_edit_page.email3
   assert contact_from_home_page.firstname == contact_from_edit_page.firstname
   assert contact_from_home_page.lastname == contact_from_edit_page.lastname
   assert contact_from_home_page.address == contact_from_edit_page.address


def test_deatails_on_contact_view_page(app):
   contact_from_edit_page = app.contact.get_contact_into_from_edit_page(0)
   email = contact_from_edit_page.email
   email2 = contact_from_edit_page.email2
   email3 = contact_from_edit_page.email3
   split_email = email.split("@")
   merge_email = email + " (www." +split_email[1] + ")"
   split_email2 = email2.split("@")
   merge_email2 = email2 + " (www." + split_email2[1] + ")"
   split_email3 = email3.split("@")
   merge_email3 = email3 + " (www." + split_email3[1] + ")"
   merge_emails = merge_email + "\n" + merge_email2 + "\n" + merge_email3

   merge_Datails_From_Edit = contact_from_edit_page.firstname + " " + contact_from_edit_page.lastname + "\n" + \
                          contact_from_edit_page.address + "\n\n" + "H: " +clear(contact_from_edit_page.homephone) + "\n" + \
                          "M: " + clear(contact_from_edit_page.mobilephone) + "\n" + "W: " +clear(contact_from_edit_page.workphone) + "\n\n" + merge_emails +\
                          "\n\n\n\n" + "P: " +clear(contact_from_edit_page.secondaryphone)
   textDetails = app.contact.get_contact_text_from_view_page(0)
   assert textDetails == merge_Datails_From_Edit


def clear(s):
    return re.sub("[() -]", "", s)

