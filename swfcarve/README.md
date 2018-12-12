# SWFCarve

[stoQ](https://stoq-framework.readthedocs.io/en/v2/index.html) plugin that carves and decompresses SWF files from payloads

## Plugin Classes

- [Worker](https://stoq-framework.readthedocs.io/en/v2/dev/workers.html)

## Configuration

All options below may be set by:

- [plugin configuration file](https://stoq-framework.readthedocs.io/en/v2/dev/plugin_overview.html#configuration)
- [`stoq` command](https://stoq-framework.readthedocs.io/en/v2/gettingstarted.html#plugin-options)
- [`Stoq` class](https://stoq-framework.readthedocs.io/en/v2/dev/core.html?highlight=plugin_opts#using-providers)

### Options

- `swf_headers` [str]: Regex pattern to match for SWF headers (i.e., CWS or FWS)