import pytest

from library.library import Library


@pytest.fixture
def empty_library():
    """A brand-new, empty Library instance.

    scope='function' (the default): every test that requests this fixture
    gets its own fresh Library. borrow_book() mutates internal state
    (member_loans), so tests MUST NOT share an instance -- otherwise a
    loan registered in one test would still be counted in the next test,
    making tests order-dependent and non-repeatable. Function scope is the
    right choice whenever the fixture's state is cheap to build AND gets
    mutated by the test.
    """
    return Library()


@pytest.fixture(scope="module")
def isbn_pool():
    """A pool of 20 pre-generated, valid 13-digit ISBNs.

    scope='module': this data is read-only (no test ever mutates the
    list) and is treated as "expensive setup". Since nothing about it
    changes between tests, it is safe and faster to build it once per
    test module and hand every test in that module the same list.
    """
    return [f"97800000000{i:02d}" for i in range(20)]