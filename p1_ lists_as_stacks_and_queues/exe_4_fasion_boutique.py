def sum_clothes_values(stack_of_clothes, rack_capacity):

    sum_of_clothes = 0
    number_of_racks_used = 1

    while stack_of_clothes:
        current_value = stack_of_clothes.pop()
        if current_value + sum_of_clothes >= rack_capacity:
            number_of_racks_used += 1
            sum_of_clothes = current_value
        else:
            sum_of_clothes += current_value

    return number_of_racks_used


int_sequence = [int(x) for x in input().split(' ')]
rack_capacity = int(input())

print(sum_clothes_values(int_sequence, rack_capacity))

