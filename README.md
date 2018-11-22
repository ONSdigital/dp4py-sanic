dp4py-sanic
==================

# Configuration

### Environment variables

| Environment variable         | Default                   | Description
| ---------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------
| LOGGING_NAMESPACE            | CONFIG.APP.title          | Namespace to use for logging (defaults to app title)
| ENABLE_PROMETHEUS_METRICS    | false                     | Enable/disable the /metircs endpoint for prometheus.
| COLOURED_LOGGING_ENABLED     | false                     | Enable/disable coloured logging.
| PRETTY_LOGGING               | false                     | Enable/disable JSON formatting for logging.
| LOG_LEVEL                    | INFO                      | Log level (INFO, DEBUG, or ERROR)

### Install

Add to `requirements.txt` as follows:

```
git+https://github.com/ONSdigital/dp4py-sanic.git@master#egg=dp4py_sanic
```

### Licence

Copyright ©‎ 2016, Office for National Statistics (https://www.ons.gov.uk)

Released under MIT license, see [LICENSE](LICENSE.md) for details.

This software uses the fastText library, see [LICENSE](LICENSE.fastText.md) for details.
