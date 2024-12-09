import world
import dataloader
import model
import utils
from pprint import pprint

if world.dataset in ['ml-latest-small', 'ml-25m','ml-25m-reduced']:
    dataset = dataloader.MoviesLoader(path="../data/"+world.dataset)

print('===========config================')
pprint(world.config)
print("cores for test:", world.CORES)
print("comment:", world.comment)
print("tensorboard:", world.tensorboard)
print("LOAD:", world.LOAD)
print("Weight path:", world.PATH)
print("Test Topks:", world.topks)
print("using bpr loss")
print('===========end===================')

MODELS = {
    'mf': model.PureMF,
    'lgn': model.LightGCN
}