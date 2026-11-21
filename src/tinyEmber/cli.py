"""CLI entry point for tinyEmber."""

import sys
import yaml
from pathlib import Path
from typing import Optional

import click
from rich.console import Console

console = Console()


@click.command()
@click.option("--input", "-i", type=click.Path(exists=True), help="Input file path")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option("--config", "-c", type=click.Path(exists=True), default=None, help="Config file (YAML)")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.version_option(version="1.9.3")
def main(input: Optional[str], output: Optional[str], config: Optional[str], verbose: bool):
    """tinyEmber -- process files with style."""
    cfg = {}
    if config:
        with open(config) as f:
            cfg = yaml.safe_load(f) or {}

    if verbose:
        console.print(f"[bold blue]tinyEmber[/] v1.9.3")
        console.print(f"Config: {cfg}")

    if not input:
        click.echo(main.get_help(click.Context(main)))
        sys.exit(0)

    data = Path(input).read_text()
    processed = _process(data, cfg)

    if output:
        Path(output).write_text(processed, encoding="utf-8")
        console.print(f"[green]OK[/] Output written to {output}")
    else:
        console.print(processed)


def _process(data: str, cfg: dict) -> str:
    """Core processing logic."""
    lines = data.strip().splitlines()
    result = []
    for i, line in enumerate(lines):
        if cfg.get("trim", True):
            line = line.strip()
        if cfg.get("uppercase", False):
            line = line.upper()
        result.append(f"{i+1:04d} | {line}")
    return chr(10).join(result)


if __name__ == "__main__":
    main()