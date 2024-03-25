from turbobus.injection import injectable_of
from src.beer.axioma.entities import Beer
from src.beer.axioma.repositories import BeerRepository
from src.beer.axioma.utils import parse_id


@injectable_of(BeerRepository)
class BeerRepositoryInMemory(BeerRepository):

    def __init__(self):
        beer1 = Beer(id=1, name='Heineken', price=5.0)
        beer2 = Beer(id=2, name='Stella Artois', price=4.5)
        beer3 = Beer(id=3, name='Redds', price=4.5)

        self.__beers: dict[str, Beer] = {
            parse_id(beer1.id): beer1,
            parse_id(beer2.id): beer2,
            parse_id(beer3.id): beer3,
        }

    def save(self, beer):
        self.__beers[parse_id(beer.id)] = beer

    def get_by_id(self, beer_id):
        return self.__beers.get(parse_id(beer_id))
    
    def get_all(self) -> list[Beer]:
        return list(self.__beers.values())
