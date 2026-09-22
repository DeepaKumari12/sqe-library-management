# Unit testing notes - verbose vs short traceback output

## pytest -v tests/

Lists every single test by its full name (file::function[params]) with
PASSED/FAILED next to it. Example:

tests/test_borrow_limit.py::test_borrow_book_edge_cases[zero_books_borrow_first] PASSED
tests/test_export_catalog.py::test_export_catalog_writes_expected_content PASSED
47 passed in 0.05s

On a failure, -v prints the full traceback including the entire body of
the failing test function up to the failing line.

## pytest --tb=short tests/

Collapses each file's results into dots (pass) and F (fail) instead of
listing every test name. Example:

tests/test_borrow_limit.py ......                                  [ 12%]
tests/test_export_catalog.py ..                                    [ 17%]
47 passed in 0.05s

On a failure, --tb=short prints only the failing line and the assertion,
skipping the rest of the function body.

## When to use each

- -v: while actively writing or debugging tests locally, since seeing
  every test name makes it easy to spot which specific case (especially
  a parametrized case) passed or failed.
- --tb=short: in CI logs or when running the whole suite quickly, since
  the output stays compact and a short traceback is usually enough to
  find the failing assertion.

## Fixture scopes used in this suite

- empty_library (scope=function, the default): a fresh Library() per
  test, because borrow_book() mutates state and tests must stay
  independent of each other.
- isbn_pool (scope=module): a read-only list of ISBNs built once per
  test file and reused, since nothing ever mutates it.
