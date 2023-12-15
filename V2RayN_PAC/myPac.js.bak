var proxy = '__PROXY__'; // Replace '__PROXY__' with your actual proxy settings.

// Define rules using an object where keys are the hostnames to match,
// and the values indicate whether to use a proxy for that hostname.
var rules = {
    'DIRECT': {
        // 'example1.com': true,
        // Add more direct access rules here...
    },
    'PROXY': {
        // 'blocked1.com': true,
        // Add more proxy rules here...
    }
};

function FindProxyForURL(url, host) {
    // Check if the host should be accessed directly.
    if (rules['DIRECT'][host]) {
        return 'DIRECT';
    }

    // Check if the host should be accessed through a proxy.
    if (rules['PROXY'][host]) {
        return proxy;
    }

    // Check each host in the rules for wildcard subdomains (e.g., *.example.com).
    for (var ruleType in rules) {
        for (var ruleHost in rules[ruleType]) {
            if (host.endsWith('.' + ruleHost)) {
                return ruleType === 'DIRECT' ? 'DIRECT' : proxy;
            }
        }
    }

    // Default to direct access if no rule matches.
    return 'DIRECT';
}

// REF: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith
if (!String.prototype.endsWith) {
    String.prototype.endsWith = function(searchString, position) {
        var subjectString = this.toString();
        if (typeof position !== 'number' || !isFinite(position) || Math.floor(position) !== position || position > subjectString.length) {
            position = subjectString.length;
        }
        position -= searchString.length;
        var lastIndex = subjectString.indexOf(searchString, position);
        return lastIndex !== -1 && lastIndex === position;
  };
}