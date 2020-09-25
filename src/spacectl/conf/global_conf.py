import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.dirname(BASE_DIR)
DEFAULT_TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')
ASSET_DIR = os.path.join(BASE_DIR, 'asset')

HOME_DIR = str(Path.home())
CONFIG_DIR = os.path.join(HOME_DIR, '.spaceone')
TEMPLATE_DIR = os.path.join(CONFIG_DIR, 'template')
ENVIRONMENT_CONF_PATH = os.path.join(CONFIG_DIR, 'environment.yml')
ENVIRONMENT_DIR = os.path.join(CONFIG_DIR, 'environments')

DEFAULT_ENVIRONMENT = 'default'
DEFAULT_PARSER = 'spacectl.lib.parser.default.DefaultParser'

RESOURCE_ALIAS = {
    # Identity
    'domain': ['identity', 'Domain'],
    'project': ['identity', 'Project'],
    'project_group': ['identity', 'ProjectGroup'],
    'pg': ['identity', 'ProjectGroup'],
    'user': ['identity', 'User'],
    'api_key': ['identity', 'APIKey'],
    'role': ['identity', 'Role'],
    'provider': ['identity', 'Provider'],
    'service_account': ['identity', 'ServiceAccount'],
    'sa': ['identity', 'ServiceAccount'],

    # Inventory
    'server': ['inventory', 'Server'],
    'sv': ['inventory', 'Server'],
    'cloud_service': ['inventory', 'CloudService'],
    'cs': ['inventory', 'CloudService'],
    'cloud_service_type': ['inventory', 'CloudServiceType'],
    'collector': ['inventory', 'Collector'],
    'region': ['inventory', 'Region'],
    'pool': ['inventory', 'Pool'],

    # Config
    'config_map': ['config', 'ConfigMap'],
    'cm': ['config', 'ConfigMap'],

    # Plugin
    'supervisor': ['plugin', 'Supervisor'],
    'sup': ['plugin', 'Supervisor'],

    # Repository
    'repository': ['repository', 'Repository'],
    'repo': ['repository', 'Repository'],
    'plugin': ['repository', 'Plugin'],
    'schema': ['repository', 'Schema'],

    # Secret
    'secret': ['secret', 'Secret'],
}

EXCLUDE_APIS = [
    # 'identity.Domain.create',
    'identity.Domain.update',
    '*.delete'
]