ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
ft_list[1] = "World"
mutateTuple = list(ft_tuple)
mutateTuple[1] = "Morocco"
ft_tuple = tuple(mutateTuple)
ft_set.remove("tutu!")
ft_set.update(['benguerir',])
ft_dict["Hello"] = "42Benguerir"
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)