import subprocess
import os

ROOTDIR = os.path.dirname(__file__)
#from config import OUTPUTDIR
OUTPUTDIR = f"{ROOTDIR}/output/"
from src.utils import get_file_location, parse_input, write_to_latexfile

class FileWriter:
	
	def __init__(self,filepath: str):
		self.filepath = filepath

	def __enter__(self):
		return self
	
	def __exit__(self,*args,**kwargs):
		return False

class App:
	
	def __init__(self,filename: str):
		self.latex_path = f"{ROOTDIR}/latexfiles/source/{filename}.tex"
		self.output_dir: str | None = OUTPUTDIR
		self.pdf_path: str | None = f"{self.output_dir}{filename}.pdf"
		self.loc, _ = get_file_location(self.latex_path)

	def _write_to_latex(self, s:str):
		self.loc = write_to_latexfile(filepath=self.latex_path, s=s, location=self.loc)

	def _compile_latex(self):
		if self.output_dir is not None:
			subprocess.call([
				'pdflatex',
				f"-output-directory={self.output_dir}",
				self.latex_path
			])
		else:
			raise Exception("Output directory not specified. Not running in container...")

                        
	def loop(self):
		while True:
			dump = input("Anna rivi:\n")
			command, parsed = parse_input(dump)
			match command:
				case "write":
					self._write_to_latex(parsed+"\n")
				case "log":
					print(f"log: {parsed}")
				case  _command if command in ["quit", "compile"]:
					return _command

	def main(self):
		while True:
			action = self.loop()
			if action == "quit":
				break
			elif action == "compile":
				self._compile_latex()
			else:
				raise Exception(f"'{action}' is not recognized action")

	def __call__(self,*args,**kws):
		self.main()


if __name__ == '__main__':
	print("lol")
	filename = "test"
	App(filename=filename)()
	
