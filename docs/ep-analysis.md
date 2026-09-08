\# Equivalence Partitioning Analysis — LibraryHub



\## 1. fine\_tier(days\_overdue)



| Class | Range | Representative Value | Expected Result |

|---|---|---|---|

| Invalid (negative) | days\_overdue < 0 | -3 | raises ValueError |

| None | 0 | 0 | 'None' |

| Low | 1-7 | 4 | 'Low' |

| Medium | 8-14 | 10 | 'Medium' |

| High | 15-30 | 20 | 'High' |

| Severe | 31+ | 45 | 'Severe' |



\## 2. Books on loan per member (Library.borrow\_book)



| Class | Range | Representative Value | Expected Result |

|---|---|---|---|

| Valid | 0-5 books | member at 3 books, borrows a 4th | loan succeeds |

| Invalid | 6+ books | member at 5 books, attempts a 6th | raises ValueError |



\## 3. ISBN field (validate\_isbn)



| Class | Description | Representative Value | Expected Result |

|---|---|---|---|

| Valid | Exactly 13 numeric digits | '9780306406157' | True |

| Empty string | No characters | '' | False |

| Too-short string | Fewer than 13 digits | '978030640615' (12 digits) | False |

| Letters/symbols | Contains non-digit characters | '97803064061X5' | False |



\## Test Run Summary

