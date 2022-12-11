# fetch generally relevant info from project

import sys
from typing import Any


def fetch_project_info(config: dict[str, Any]) -> dict[str, Any]:
    project_info: dict[str, Any] = {
        'name': None,
        'description': None,
        'authors': None,
        'python_version': None,
        'dependencies': None,
        'license': None,
        'multi_licensed': None,
        'scripts': None,
        'docs_url': None,
        'issues_url': None,
        'source_url': None,
    }

    project_table = config.get('project')

    if not project_table:
        raise KeyError('no project table')
    project_info['name'] = project_table.get('name')
    project_info['description'] = project_table.get('description')
    project_info['authors'] = [t['name']
                               for t in project_table.get('authors')] if project_table.get('authors') else []
    project_info['python_version'] = project_table.get('requires-python')
    project_info['dependencies'] = project_table.get('dependencies')
    project_info['license'] = project_table.get('license')
    project_info['multi_licensed'] = ' OR ' in project_info['license'] if project_info['license'] else None
    project_info['scripts'] = list(project_table.get('scripts').keys()) if project_table.get('scripts') else None
    urls_table = project_table.get('urls')
    if urls_table:
        project_info['docs_url'] = urls_table.get('Documentation')
        project_info['issues_url'] = urls_table.get('Issues')
        project_info['source_url'] = urls_table.get('Source')

    return project_info


def fetch_build_info(config: dict[str, Any]) -> dict[str, Any]:
    build_info: dict[str, Any] = {
        'build_backend': None
    }

    build_system_table = config.get('build-system')
    if not build_system_table:
        raise KeyError('no build-system table')
    match build_system_table.get('build-backend'):
        case 'hatchling.build':
            build_info['build_backend'] = 'hatchling'
        case 'poetry.core.masonry.api':
            build_info['build_backend'] = 'poetry'
        case 'setuptools.build_meta':
            build_info['build_backend'] = 'setuptools'
        case _:
            build_info['build_backend'] = f'unknown ({build_system_table.get("build-backend")}'

    return build_info


def fetch_tool_info(config: dict[str, Any]) -> dict[str, Any]:
    tool_info: dict[str, Any] = {
        'type_checking': None,
        'formatting': None,
        'linting': None,
        'testing': None,
        'other_tools': None,
    }

    # not sure how to avoid type errors if i exclude table as a param here
    # i want to just use the locally defined tool_table variable...
    def check_for_tools(potential: list[str], table: dict[str, Any]):
        return [p for p in potential if table.get(p)]

    tool_table = config.get('tool')
    if not tool_table:
        raise KeyError('no tool table')
    tool_info['type_checking'] = check_for_tools(['mypy', 'pyright'], tool_table)
    tool_info['formatting'] = check_for_tools(['black', 'blue', 'autopep8', 'yapf'], tool_table)
    tool_info['linting'] = check_for_tools(['ruff', 'flake8'], tool_table)
    tool_info['testing'] = check_for_tools(['pytest', 'coverage'], tool_table)
    tool_info['other_tools'] = [o for o in tool_table.keys() if o not in tool_info['type_checking'] +
                                tool_info['formatting'] + tool_info['linting'] + tool_info['testing']]
    return tool_info


def fetch_info(config: dict[str, Any]) -> dict[str, Any]:
    # flat dict for now

    try:
        project_info = fetch_project_info(config)
        build_info = fetch_build_info(config)
        tool_info = fetch_tool_info(config)
        info = project_info | build_info | tool_info
    except KeyError as e:
        print(e)
        sys.exit(1)

    return info
