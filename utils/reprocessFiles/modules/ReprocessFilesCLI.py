import argparse
from modules.ProcessFiles import ProcessFiles

class ReprocessFilesCLI:

    def init_argparse(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            usage="%(prog)s [OPTION] [FILE]...",
            description="Passes specified json files to a URL. Records failed files in a sub folder."
        )
        parser.add_argument("-v", "--version", action="version",
                            version=f"{parser.prog} version 1.0.0")
        parser.add_argument("-f", "--folder", dest="folder", required=True,
                            help="Folder containing files to process")
        parser.add_argument("-u", "--url", dest="url", required=True,
                            default="google.com",
                            help="URL to attempt to upload to")
        return parser

    def main(self):
        parser = self.init_argparse()
        args = parser.parse_args()
        print(args)
        pf = ProcessFiles(args.folder, args.url)
        pf.processFiles()
        