string = "beautiful_is_better_than_ugly\
explicit_is_better_than_implicit\
simple_is_better_than_complex\
complex_is_better_than_complicated\
flat_is_better_than_nested\
sparse_is_better_than_dense\
readability_counts\
special_cases_arent_special_enough_to_break_the_rules\
although_practicality_beats_purity\
errors_should_never_pass_silently\
unless_explicitly_silenced\
in_the_face_of_ambiguity_refuse_the_temptation_to_guess\
there_should_be_one_and_preferably_only_one_obvious_way_to_do_it\
although_that_way_may_not_be_obvious_at_first_unless_you_are_Dutch\
now_is_better_than_never\
although_never_is_often_better_than_right_now\
if_the_implementation_is_hard_to_explain_it_іs_a_bad_idea\
if_the_implementation_is_easy_to_explain_it_may_be_a_good_idea\
namespaces_are_one_honking_great_idea_lets_do_more_of_those"

x = string.count("better")
y = string.count("never")
z = string.count("is")

print(x,y,z)

print(string.upper())
print(string.lower())
print(string.replace("i","&"))