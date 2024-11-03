def find_common_participants(group1, group2, separator=','):
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    common_participants = sorted(participants1.intersection(participants2))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Testing the function with a separator different from a comma
result = find_common_participants(participants_first_group, participants_second_group, separator='; ')
print(result)
