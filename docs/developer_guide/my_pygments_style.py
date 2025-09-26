# filepath: /d:/Development/simple-cloud-kit-oss/simple-cloud-kit/core-docs/docs/my_pygments_style.py

from pygments.style import Style
from pygments.token import (
    Token,
    Comment,
    Keyword,
    Name,
    String,
    Error,
    Number,
    Operator,
    Generic,
    Whitespace,
)


class MyCustomStyle(Style):
    background_color = "#444"
    default_style = ""

    styles = {
        Token: "#f8f8f2",
        Whitespace: "#f8f8f2",
        Comment: "italic #6272a4",
        Comment.Preproc: "noitalic #ff79c6",
        Keyword: "bold #ff79c6",
        Keyword.Pseudo: "nobold",
        Keyword.Type: "nobold #8be9fd",
        Operator: "#ff79c6",
        Operator.Word: "bold #ff79c6",
        Name.Builtin: "#8be9fd",
        Name.Function: "#50fa7b",
        Name.Class: "bold #50fa7b",
        Name.Namespace: "bold #50fa7b",
        Name.Exception: "bold #ffb86c",
        Name.Variable: "#f8f8f2",
        Name.Constant: "#bd93f9",
        Name.Label: "#ff79c6",
        Name.Entity: "bold #f8f8f2",
        Name.Attribute: "#50fa7b",
        Name.Tag: "bold #ff79c6",
        Name.Decorator: "#50fa7b",
        String: "#f1fa8c",
        String.Doc: "italic",
        Number: "#bd93f9",
        Generic.Heading: "bold #f8f8f2",
        Generic.Subheading: "bold #f8f8f2",
        Generic.Deleted: "#ff5555",
        Generic.Inserted: "#50fa7b",
        Generic.Error: "#ff5555",
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Prompt: "#ff79c6",
        Generic.Output: "#f8f8f2",
        Generic.Traceback: "#ff5555",
        Error: "border:#ff5555",
    }
