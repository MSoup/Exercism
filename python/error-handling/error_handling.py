def handle_error_by_throwing_exception():
  raise Exception("Error")
  


def handle_error_by_returning_none(input_data):
  return None


def handle_error_by_returning_tuple(input_data):
  return (input_data)


def filelike_objects_are_closed_on_exception(filelike_object):
  if filelike_object.is_open:
    filelike_object.close()

