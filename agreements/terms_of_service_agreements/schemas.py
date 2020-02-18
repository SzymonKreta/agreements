import colander


class ParagraphSchema(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
    content = colander.SchemaNode(colander.String())


class TermsOfServiceSchema(colander.SequenceSchema):
    fields = ParagraphSchema()
