from Routes.health import health
from Routes.v1Description import v1_description
from Routes.v2Description import v2_description
from Routes.v1Vision import v1_vision
from Routes.v2Vision import v2_vision


def health_route(event, context):
  return health(event, context)

def v1_description_route(event, context):
  return v1_description(event, context)

def v2_description_route(event, context):
  return v2_description(event, context)

def v1_vision_route(event, context):
  return v1_vision(event)

def v2_vision_route(event, context):
  return v2_vision(event)
