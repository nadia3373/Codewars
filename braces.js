function validBraces(braces) {
    while (braces.includes("()") || braces.includes("{}") || braces.includes("[]")) {
        if (braces.includes("()")) braces = braces.replace("()");
        if (braces.includes("{}")) braces = braces.replace("{}");
        if (braces.includes("[]")) braces = braces.replace("[]");
    };
    console.log(braces);
}

validBraces("({[({})]})");
