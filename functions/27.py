# task in russian here --- https://stepik.org/lesson/511854/step/9?unit=504046
# using included function zip for parallel iteration 
# generator of zip object will  have dimension of smallest included list 
# in our case all lists are equal
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
z = list(zip(capitals, countries, population))
for i in z:
    print(f'{i[0]} is the capital of {i[1]}, population equal {i[2]} people.')