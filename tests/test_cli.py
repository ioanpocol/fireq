import textwrap
import subprocess


def check_output(cmd):
    return subprocess.check_output(cmd, shell=True).decode()


def startswith(cmd, txt):
    txt = textwrap.dedent(txt).strip()
    txt = txt % {'scopes': '{sd,sds,sdc,sdp,ntb,lb}'}
    out = check_output(cmd)
    if out.startswith('Running with sudo...\n'):
        out = out.split('\n', 1)[1]
    assert out.startswith(txt)


def test_fire_wrapper():
    startswith('./fire2 -h', (
        'usage: fire [-h] {gen-files,run,r,ci,nginx}'
    ))
    startswith('./fire2 gen-files -h', (
        'usage: fire gen-files [-h] [--dry-run]'
    ))

    startswith('./fire2 ci -h', (
        'usage: fire ci [-h] [--dry-run] [-t TARGET] %(scopes)s ref'
    ))

    startswith('./fire2 run -h', '''
    usage: fire run [-h] [--dry-run] [--scope %(scopes)s] [--dev DEV]
                    [--host HOST]
                    name
    ''')
