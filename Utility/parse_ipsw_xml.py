from typing import Tuple


def decompose_build_to_abc_parts(build_str: str) -> Tuple[str, str, str]:
    for i, char in enumerate(build_str):
        if char.isalpha():
            return build_str[:i], char, build_str[i + 1:]
    return build_str, '', ''


def decompose_build_part_c(build_part_c: str) -> Tuple[str, str]:
    if build_part_c and build_part_c[-1].isalpha():
        return build_part_c[:-1], build_part_c[-1]
    return build_part_c[-3:] if len(build_part_c) > 3 else build_part_c, '0'


def compare_build(build1: str, build2: str) -> str:
    def compare_build_part_c(build_1_part_c: str, build_2_part_c: str) -> bool:
        build_1_part_c_list = decompose_build_part_c(build_1_part_c)
        build_2_part_c_list = decompose_build_part_c(build_2_part_c)
        if build_1_part_c_list[0] != build_2_part_c_list[0]:
            return True if int(build_1_part_c_list[0]) > int(build_2_part_c_list[0]) else False
        else:
            return True if build_1_part_c_list[1] > build_2_part_c_list[1] else False

    build1_part_a, build1_part_b, build1_part_c = decompose_build_to_abc_parts(build1)
    build2_part_a, build2_part_b, build2_part_c = decompose_build_to_abc_parts(build2)
    if build1_part_a != build2_part_a:
        return build1 if int(build1_part_a) > int(build2_part_a) else build2
    else:
        if build1_part_b != build2_part_b:
            return build1 if build1_part_b > build2_part_b else build2
        else:
            if build1_part_c != build2_part_c:
                bool_is_later = compare_build_part_c(build1_part_c, build2_part_c)
                return build1 if bool_is_later else build2


def get_latest_build(build_list: tuple[str]) -> str:
    len_build_list = len(build_list)
    if len_build_list == 0:
        return 'error: empty list'
    elif len_build_list == 1:
        return build_list[0]
    else:
        temp_max = build_list[0]
        for temp_version in build_list[1:]:
            temp_max = compare_build(temp_max, temp_version)
        return temp_max
