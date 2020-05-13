class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    return _is_user_in_group(user.lower(), group)


def _is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == '':
        return False

    if user in group.get_users():
        return True

    for sub_group in group.get_groups():
        result = is_user_in_group(user, sub_group)

        if result:
            return True

    return False


# User is in a group
parent = Group("parent")
child = Group("child")
siblings = Group('siblings')
sub_child = Group("subchild")

siblings.add_user('Anthony')
siblings.add_user('Greg')
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(siblings)
child.add_group(sub_child)
parent.add_group(child)
child.add_user("may")

print('-------------------- Test Case 1------------------')
# User is in group
print(is_user_in_group('sub_child_user', parent))
# print True

print('-------------------- Test Case 2------------------')
# User is not in group
print(is_user_in_group('Tommy', parent))
# print False

print('-------------------- Test Case 3------------------')
# User is in group but letters are capitalized
print(is_user_in_group('Sub_chIld_user', parent))
# print True

print('-------------------- Test Case 4------------------')
# User empty input
print(is_user_in_group('', parent))
# Print False

print('-------------------- Test Case 5------------------')
# User in child group
print(is_user_in_group('may', parent))
# Print True

print('-------------------- Test Case 6------------------')
# User in child group
print(is_user_in_group('Greg', parent))
# Print True




