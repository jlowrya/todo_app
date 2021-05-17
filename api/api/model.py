import colander

class Todo(colander.MappingSchema):
    id = colander.SchemaNode(colander.String(), missing=colander.drop)
    done = colander.SchemaNode(colander.Boolean(), missing=False)
    title = colander.SchemaNode(colander.String(), default="")
    description = colander.SchemaNode(colander.String(), default="")

class HTTPResponse(colander.MappingSchema):
    statusCode = colander.SchemaNode(colander.Integer(), validator=lambda x : 200<=x<=600, default=200)
    body = colander.SchemaNode(colander.String())
