from priv_admin import Privileges, Admin

spez = Admin("Alex", "Ohanian", 31, "San Francisco", "Los Angeles",
		"English", "German", "Spanish")

spez.describe_user()
spez.privileges.show_privileges()