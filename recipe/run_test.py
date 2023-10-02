print("import: 'json_stream_rs_tokenizer'")
import json_stream_rs_tokenizer

# this test is very important to detect if the rust
# package was built correctly (the rust toolchain must
# be present)
print("json_stream_rs_tokenizer.rust_tokenizer_or_raise()")
json_stream_rs_tokenizer.rust_tokenizer_or_raise()