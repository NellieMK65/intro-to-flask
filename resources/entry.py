from flask_restful import Resource


class EntryResource(Resource):
    # This will handle both single and multiple entries
    # /entries -> GETs all resources
    # /entries/<id> -> GET -> get a single entry
    def get(self, entry_id=None):
        if entry_id == None:
            # means we want to get all entries
            return []
        else:
            # get a signle entry
            return {}

    def post(self):
        return {"message": "Entry created"}

    def patch(self, entry_id):
        return {"message": "Entry updated"}

    def delete(self, entry_id):
        return {"message": "Entry deleted"}
