# args, kwargs


def named_args_example(name="", email=""):
	print(name, email)

named_args_example(email="test@gmail.com", name="Test")
named_args_example(email="test@gmail.com")
named_args_example()
named_args_example("test@gmail.com")
named_args_example("test@gmail.com", "Test")


def create_some_operation_on_warehouse(client, env, warehouse_id, token):
	# token in request
	print(f"Operation on {warehouse_id} ({client}-{env}) started")



create_some_operation_on_warehouse("E-corp", "dev", 9845, 93283)
create_some_operation_on_warehouse("E-corp", "dev", 93283, 9845)

def create_some_operation_on_warehouse(client="", env="", warehouse_id=0, token=None):
	# token in request
	print(f"Operation on {warehouse_id} ({client}-{env}) started")



create_some_operation_on_warehouse(client="E-corp", token=93283, warehouse_id=9845, env="dev")
create_some_operation_on_warehouse(client="E-corp", token=93283, env="dev")


# **KWARGS

data = {"client":"E-corp", 
 		"token":93283, 
 		"warehouse_id":9845, 
 		"env":"dev"}

create_some_operation_on_warehouse(**data)

def kwargs_example(**kwargs):
	print(kwargs)
	print(type(kwargs))


kwargs_example(**data)
kwargs_example(client="E-corp", token=93283, warehouse_id=9845, env="dev")


print({**data})
# print(**data)

# *ARGS


def args_example(*args):
	print(args)
	print(type(args))

args_example(1,2,3,4,56)
args_example("E-corp", "dev", 9845, 93283)


print(*("E-corp", "dev", 9845, 93283))