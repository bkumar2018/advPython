import yaml

#open yaml file and print it
with open("test.yaml", "r") as f:
    try:
        data = yaml.safe_load(f)
        print(data)
        print(type(data))
    except yaml.YAMLError as e:
        print(e)
        




# with open("test.yaml", "r") as f:
#     data = yaml.safe_load(f)

# print(data)


