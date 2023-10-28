import subprocess
import os

ROOTDIR = os.path.dirname(__file__)

class FileWriter:
	
	def __init__(self,filepath: str):
		self.filepath = filepath

	def __enter__(self):
		return self
	
	def __exit__(self,*args,**kwargs):
		return False

class App:
	
	def __init__(self,filename: str):
		self.latex_path = f"{ROOTDIR}/templates/{filename}.tex"
		self.output_dir = f"{ROOTDIR}/output/"
		self.pdf_path = f"{self.output_dir}{filename}.pdf"

	def _compile_latex(self):
                subprocess.call([
                        'pdflatex',
                        f"-output-directory={self.output_dir}",
                        self.latex_path
                ])

                        
	def loop(self):
                with open(self.latex_path,'a') as f:
                        f.seek(2)
                        while True:
                                dump = input("Anna rivi:\n")
                                if dump.strip() == "%q":
                                        return True, None
                                elif dump.strip() == "%c":
                                        return False, "compile"
                                f.write(dump)
	def main(self):
        	while True:
                	isend, action = self.loop()
                	if isend:
                        	break
                	if action == "compile":
                        	self._compile_latex()

	def __call__(self,*args,**kws):
                self.main()


if __name__ == '__main__':
	filename = "test"
	App(filename=filename)()
	
