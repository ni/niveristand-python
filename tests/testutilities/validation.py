import inspect
from niveristand._decorators import rt_seq_mode_id


def test_validate(testmodule):
    funcs = [n for n, f in inspect.getmembers(testmodule, inspect.isfunction) if
             getattr(f, rt_seq_mode_id, None) is not None]
    test_lists = {}
    for a in dir(testmodule):
        if (a.startswith('run_tests') or a.startswith('skip_tests') or a.startswith('transform_tests') or
                a.startswith('fail_transform_tests') or a.startswith('python_tests') or
                a.startswith('py_only_different_behavior_tests') or a.startswith('py_only_errs')):
            test_lists[a] = testmodule.__dict__.get(a)
    _validate_special_lists_are_subsets_of_overall_lists(test_lists, 'py_only_different_behavior_tests', 'run_tests')
    _validate_special_lists_are_subsets_of_overall_lists(test_lists, 'py_only_errs', 'run_tests')
    final_list = []
    for key, value in test_lists.items():
        for item in value:
            final_list.append(item[0].__name__)
    not_assigned = [f for f in funcs if f not in final_list and not f.startswith('_')]
    assert not_assigned == [], "Test " + not_assigned.__str__() + " in " + testmodule.__name__ \
                               + " is not added to any list."


def _validate_special_lists_are_subsets_of_overall_lists(test_lists, special_list_name, overall_list_name):
    if special_list_name in test_lists:
        assert set(test_lists[special_list_name]).issubset(set(test_lists[overall_list_name])), \
            special_list_name + "list is not a subset of the " + overall_list_name + " list."
