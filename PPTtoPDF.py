import comtypes.client
import os


def init_ppt():
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    return powerpoint


def ppt_to_pdf(powerpoint, inputFile, outputFile):
    file = powerpoint.Presentations.Open(inputFile)
    file.SaveAs(outputFile, 32)
    file.Close()


def convert_ppts_in_folder(powerpoint, inputfolder, outputfolder):
    if os.path.exists(inputfolder) and os.path.exists(outputfolder):
        files = os.listdir(inputfolder)
        pptfiles = [f for f in files if f.endswith((".ppt", ".pptx", ".PPT"))]
        for pptfile in pptfiles:
            inputFile = os.path.join(inputfolder, pptfile)

            outFileName = ""
            if pptfile.endswith(("ppt", "PPT")):
                outFileName = pptfile[:-3] + "pdf"
            elif pptfile.endswith("pptx"):
                outFileName = pptfile[:-4] + "pdf"
            outputFile = os.path.join(outputfolder, outFileName)

            ppt_to_pdf(powerpoint, inputFile, outputFile)

        return True
    else:
        return False


if __name__ == '__main__':
    ppt = init_ppt()
    cwd = "E:\\code\\test"
    convert_ppts_in_folder(ppt, cwd, cwd)
    ppt.Quit()
