# default material used in documenation
DefaultMaterial = (0.7, 0.7, 0.7, 1)




# Material for cutting plane
CuttingPlaneMaterial = (0, 0, 0, 0.15)




# materials used in documentation
Materials = (
    (0.8, 0.6, 0.6),
    (0.6, 0.8, 0.6),
    (0.6, 0.6, 0.8),
    (0.8, 0.8, 0.6),
    (0.8, 0.6, 0.8),
    (0.6, 0.8, 0.8),
    (0.8, 0.7, 0.6),
    (0.7, 0.8, 0.6)
)




# color generator
def colorGenerator (requiredColorCount):
    return Materials




# get material by index
def getMaterial (index):
    return Materials[index % len (Materials)]
