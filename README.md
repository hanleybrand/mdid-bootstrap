
## Installation

mdid-bootstrap is a little unusual as an MDID extension as it need to 

```python
# apps listed here will be added to the list of installed apps
INSTALLED_APPS = (
    'rooibos.apps.mdid_bootstrap',
)

additional_settings = [
    'rooibos.apps.mdid_bootstrap.settings'
]

# BOOTSTRAP_THEME = ''
BOOTSTRAP_THEME = 'flatly'

EXPOSE_TO_CONTEXT += ('BOOTSTRAP_THEME',)


```