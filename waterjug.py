facts = [["plant", "mango"], ["eating", "mango"], ["seed", "sprouts"]]
is_changed = True


def assert_facts(fact):
    global facts
    global is_changed

    if fact not in facts:
        facts.append(fact)
        is_changed = True


while is_changed:
    is_changed = False
    for x in facts:
        if x[0] == "seed":
            assert_facts(["plant", x[1]])
        if x[0] == "plant":
            assert_facts(["fruit", x[1]])
            if ["eating", x[1]] in facts:
                assert_facts(["human", x[1]])

print(facts)



