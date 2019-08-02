# Quick start

<pre>
foo = {
        "foo": {
          "bar": "foo bar"
        }
      }

assert DictDig(subject).dig("foo.bar") == "foo bar"
</pre>

List
<pre>
foo = {
        "foo": [
        "apple",
          "orange", [
            "banana", "pineapple"
          ]
        ]
      }

assert DictDig(subject).dig("foo[2][0]") == "banana"
</pre>
