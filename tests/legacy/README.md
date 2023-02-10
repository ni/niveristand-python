## How to test the Legacy API with these tests:

1. Install **Veristand 2020 R6** or older (newer versions will fail some of the tests because the models used in them were deprecated)
2. call `pytest tests/legacy` on the `main` directory (or just `pytest` on the `tests/legacy` directory)
3. Some of the tests open Veristand if not already opened, but other tests do not, so if you are running a subtest of the tests, you'll need to have Veristand running (but nothing should be deployed).