from flask_restx import Namespace, Resource

from project.container import favorite_movie_service, user_service
from project.setup.api.models import favorite_movie_schema
from project.setup.api.parsers import page_parser
from project.tools.security import login_required

api = Namespace('favorites', description="Любимые фильмы")


@api.route('/movies/')
class FavoriteMoviesView(Resource):

    @api.expect(page_parser)
    @api.marshal_with(favorite_movie_schema, as_list=True, code=200, description='OK')
    @login_required
    def get(self, token_data):
        """
        Get all favourite movies.
        """
        user = user_service.get(token_data)
        return favorite_movie_service.get_all_by_user_id(user.id, **page_parser.parse_args())


@api.route('/movies/<int:movie_id>/')
class FavoriteMovieView(Resource):

    @api.marshal_with(favorite_movie_schema, code=200, description='OK')
    @login_required
    def get(self, movie_id, token_data):
        """
        Get one favourite movie.
        """
        user = user_service.get(token_data)
        return favorite_movie_service.get_item((user.id, movie_id,))

    @login_required
    def post(self, movie_id, token_data):
        print("!!!!!!", token_data, movie_id, "!!!!!!")
        user = user_service.get(token_data)
        print("!!!!!!", user.id, movie_id, "!!!!!!")
        favorite_movie_service.create({
            "user_id": user.id,
            "movie_id": movie_id
        })
        return "OK", 201, {"Location": f"/movies/{movie_id}"}

    @login_required
    def delete(self, movie_id, token_data):
        user = user_service.get(token_data)
        favorite_movie_service.delete((user.id, movie_id,))
        return "OK", 204
