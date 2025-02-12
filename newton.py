import os
import platform
import subprocess
import shutil
from posix import getcwd
import shlex
import typer
from click import prompt
from rich import print
from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.table import Table
from typing import List, Optional
from pathlib import Path
import select
from typing_extensions import  Annotated
from enum import Enum


ROOT_DIR = None

class PkgName(str, Enum):
    motor_driver = "motor_driver"
    odrive_can = "odrive_can"
    imu_driver = "imu_driver"
    newton = "newton"
    all = "all"



app = typer.Typer(
    help="run nt [COMMAND] --help for more information"
)
ctn_app = typer.Typer()
pkg_app = typer.Typer()


app.add_typer(ctn_app, name="ctn", help="Actions related with containers")
app.add_typer(pkg_app, name="pkg", help="Actions related with packages")

console = Console()

@pkg_app.command("clean")
def clean_workspace(
    name:Annotated[PkgName, typer.Argument(
        help="Name of the package to clean",
    )] = PkgName.all 
):
    """" Clean a ros package removes build, install and log directories"""
    if name == "all":
        console.print(f"[red]Cleaning all packages[/red]")
        try:
            for directory in ROOT_DIR.rglob('build'):
                if "venv" in str(directory):
                    continue
                if "jetson-containers" in str(directory):
                    continue
                console.print(f"[red]Cleaning package: {directory}[/red]")
                shutil.rmtree(directory)

            for directory in ROOT_DIR.rglob('install'):
                if "venv" in str(directory):
                    continue
                if "jetson-containers" in str(directory):
                    continue
                console.print(f"[red]Cleaning package: {directory}[/red]")
                shutil.rmtree(directory)


            for directory in ROOT_DIR.rglob('log'):
                if "venv" in str(directory):
                    continue
                if "jetson-containers" in str(directory):
                    continue
                console.print(f"[red]Cleaning package: {directory}[/red]")
                shutil.rmtree(directory)
        except Exception as e:
            console.print(f"[red]Error cleaning package: {str(e)}[/red]")
            return
    if name == "motor_driver":
        try:
            clean_ros_package(Path(ROOT_DIR,"core","src","motor_driver"))
        except Exception as e:
            console.print(f"[red]Error cleaning package: {str(e)}[/red]")
            return
    if name == "odrive_can":
        console.print(f"[red]Cleaning odrive_can package[/red]")
        try:
            clean_ros_package(Path(ROOT_DIR, "lib", "ros_odrive"))
        except Exception as e:
            console.print(f"[red]Error cleaning package: {str(e)}[/red]")
            return
    if name == "imu_driver":
        try:
            clean_ros_package(Path(ROOT_DIR, "core", "src", "imu"))
        except Exception as e:
            console.print(f"[red]Error cleaning package: {str(e)}[/red]")
            return


    console.print(f"[green] Successfully cleaned {name} package[/green]")


@pkg_app.command("build")
def build_package(
        name:Annotated[PkgName, typer.Argument(
            help="Name of the package to build")],
):
    """Build ros package and source"""
    if name == "motor_driver":
        pass
    elif name == "odrive_can":
        try:
            console.print("Building odrive_can")
            cmd = ["ros2", "pkg", "list"]
            process = subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            output, error = process.communicate(timeout=4)

            if "odrive_can" in str(output):
                console.print("Package already installed")
                return

            root = get_workspace_root()
            odrive_can_path = Path(root, "lib", "ros_odrive")
            if not odrive_can_path.exists():
                raise Exception(f"Could not find package: {odrive_can_path}")

            os.chdir(odrive_can_path)
            print(os.getcwd())
            cmd = ["colcon", "build", "--packages-select", "odrive_can", "--symlink-install"]
            os.execvp(cmd[0], cmd)
        except Exception as e:
            console.print(f"[red]Error building package: {str(e)}[/red]")
    elif name == "imu_driver":
        console.print("Building imu_driver")
        try:
            cmd = ["ros2", "pkg", "list"]
            process = subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            output, error = process.communicate(timeout=4)

            if "tm_imu" in str(output):
                console.print("Package already installed")
                return

            imu_driver_path = Path(ROOT_DIR, "core", "src", "imu")
            if not imu_driver_path.exists():
                raise Exception(f"Could not find package: {imu_driver_path}")

            os.chdir(imu_driver_path)
            print(os.getcwd())
            cmd = ["colcon", "build", "--packages-select", "tm_imu", "--symlink-install"]
            os.execvp(cmd[0], cmd)
        except Exception as e:
            console.print(f"[red]Error building package: {str(e)}[/red]")



@ctn_app.command("run")
def run_container(
    container: Annotated[str, typer.Argument(help="Name of the container to run")]= "onnx-ros",
):
    """Run a container with hardware access and proper ROS2 environment setup"""
    try:
        cmd = [
            "docker", "run", "-it",
            "--net=host",
            "-e", f"DISPLAY={os.getenv('DISPLAY', ':0')}",
            "-v", "/dev:/dev",
            "--device-cgroup-rule=c *:* rmw",
            "--device=/dev",
            "-v", f"{ROOT_DIR}:/home/newton/workspace", 
            "-w", "/home/newton/workspace", 
            container,
            "home/newton/workspace"
        ]
        os.execvp(cmd[0], cmd)
    except Exception as e:
        console.print(f"[red]Error building package: {str(e)}[/red]")
        
    
@ctn_app.command("build")
def build_container(
        name: str = typer.Argument(..., help="Name of the container to build"),
        cache: bool = typer.Option(False, help="Use cache when building the container"),
        build_args: Optional[List[str]] = typer.Option(None, "--build-arg", help="Build arguments in format KEY=VALUE")
):
    """Build a container package"""
    try:
        cmd = ["docker", "build"]
        if build_args:
            for arg in build_args:
              cmd.extend(["--build-arg", arg])
        if not cache:
            cmd.append("--no-cache")

        # pass in build arguments
        

        default_args = {
            "USERNAME":"newton",
            "ROOT": f"{str(get_workspace_root())}",
            "HAS_CUDA": str(has_cuda())
        }

        for key, value in default_args.items():
            cmd.extend(["--build-arg", f"{key}={value}"])
            
        workspace_root = get_workspace_root()
        arch = platform.machine()

        if arch == "aarch64":
          docker_file_name = "Dockerfile.aarch_64"
          console.print("Docker", docker_file_name)
        elif arch == "x86_64":
          docker_file_name = "Dockerfile.x86_64"
        else:
          raise Exception(f"Unsupported architecture: {arch}")
        path_to_dockerfile = Path(workspace_root, "docker/", docker_file_name)


        if not path_to_dockerfile.exists():
            raise Exception(f"Could not find Dockerfile: {path_to_dockerfile}")

        
        tag=f"{name}:{arch}"
        cmd.extend(["-t", name])
        cmd.extend(["-t", tag])
        
        # context
        docker_context = str(Path(workspace_root, "docker/"))
        cmd.extend(["-f", str(path_to_dockerfile)])
        cmd.append(docker_context)

        console.print(f"[yellow]Running command: {' '.join(cmd)}[/yellow]")
        process = subprocess.Popen(
            cmd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            cwd=workspace_root
        )
        while True:
            ready, _, _ = select.select([process.stdout, process.stderr], [], [], 1)  # Timeout of 1s
            for stream in ready:
                line = stream.readline().strip()
                if line:
                    console.print(line)

            exit_condition = process.poll() is not None
            if exit_condition:
                break
            # if error:
            #     console.print(f"[red]{error.strip()}[/red]")
        
            # console.print(f"{output.strip()}")
        return_code = process.poll()
        if return_code != 0:
            raise Exception(f"Error building container: {process.stderr.read()}")
        else:
            console.print(f"[green]Successfully built container: {name}[/green]")


    except Exception as e:
        console.print(f"[red]Error building package: {str(e)}[/red]")



app.command()
def set_root_dir(
    root_dir: str = typer.Argument(
        default=os.getcwd(),
        help="Root directory for the workspace"
    )

):
    """Set the root directory for the workspace"""
    global ROOT_DIR
    ROOT_DIR = root_dir
    print(f"Setting root directory to {ROOT_DIR}")
@app.command()
def test(
    test_type: str = typer.Option("unit", help="Test type [unit/integration/all]"),
    hardware: bool = typer.Option(False, help="Run hardware tests")
):
    """Run platform tests"""
    print(f"Running {test_type} tests...")
    # Test logic here

def get_workspace_root() -> Path:
    """Get the workspace root directory"""
    if 'WORKSPACE_ROOT' in os.environ:
        return Path(os.environ['WORKSPACE_ROOT'])

    # Look for workspace marker file in current or parent directories
    current = Path.cwd()
    while current != current.parent:
        if (current / '.workspace').exists():
            return current
        current = current.parent

    # Default to current directory
    return Path.cwd()



def is_package_installed(package_name: str) -> bool:
    """Check if a package is installed"""
    try:
        subprocess.check_output(["dpkg", "-s", package_name])
        return True
    except subprocess.CalledProcessError:
        return False

def has_cuda():
    return 1

def source_bash_file(path):
    """Source a bash file and return the new environment"""
    command = f'source {path} && env'
    pipe = subprocess.Popen(['/bin/bash', '-c', command], stdout=subprocess.PIPE)
    output = pipe.communicate()[0].decode()
    env = {}
    for line in output.splitlines():
        try:
            key, value = line.split('=', 1)
            env[key] = value
        except ValueError:
            continue

    return env

def clean_ros_package(path: Path):
    """Clean a ros package removes build, install and log directories"""
    try:
        if not path.exists():
            raise Exception(f"Could not find package: {path}")
        shutil.rmtree(Path(path, "build"))
        shutil.rmtree(Path(path, "install"))
        shutil.rmtree(Path(path, "log"))
    except Exception as e:
        console.print(f"[red]Error cleaning package: {str(e)}[/red]")
@app.command()
def info(
        package_name: str = typer.Argument(..., help="Name of the package to get info about")
):
    """Get detailed information about a package"""
    try:

        table = Table(title=f"Package Information: {package_name}")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")

        for key, value in info.items():
            if isinstance(value, (list, dict)):
                value = str(value)
            table.add_row(str(key), str(value))

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error getting package info: {str(e)}[/red]")
if __name__ == "__main__":
    ROOT_DIR = get_workspace_root()
    app()