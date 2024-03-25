from turbobus.injection import injectable_of
from src.beer.axioma.entities import Friend
from src.beer.axioma.repositories import FriendRepository
from src.beer.axioma.utils import parse_id


@injectable_of(FriendRepository)
class FriendRepositoryInMemory(FriendRepository):
    
    def __init__(self):
        friend1 = Friend(id=1, name='Alice')
        friend2 = Friend(id=2, name='Bob')
        friend3 = Friend(id=3, name='Charlie')

        self.__friends: dict[str, Friend] = {
            parse_id(friend1.id): friend1,
            parse_id(friend2.id): friend2,
            parse_id(friend3.id): friend3,
        }

    def save(self, friend):
        self.__friends[parse_id(friend.id)] = friend

    def get_by_id(self, friend_id):
        return self.__friends.get(parse_id(friend_id))
    
    def get_all(self) -> list[Friend]:
        return list(self.__friends.values())
