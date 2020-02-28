from collections import OrderedDict
import argparse

parser = argparse.ArgumentParser()



parameters = OrderedDict()





parser.add_argument(
    "-perf_file", default="performance.tex",
    help="Output file to store the final latex table"
)


parser.add_argument(
    "-pred_file", default="prediction.txt",
    help="Output file to save all prediction"
)




parser.add_argument(
    "-include_word_features", default="1",
    help="string feature inclusion (0 to disable)"
) 


parser.add_argument(
    "-include_context", default="1",
    help="context feature inclusion (0 to disable)"
) 


parser.add_argument(
    "-context_window_len", default="5",
    help="context window length (default 5)"
) 




parser.add_argument(
    "-include_gazetteer", default="1",
    help="gazetteer feature inclusion (0 to disable)"
) 


parser.add_argument(
    "-print_latex_format", default="0",
    help="if print in latex format (1 to enable)"
) 


opts = parser.parse_args()

parameters["perf_file"]=opts.perf_file
parameters["pred_file"]=opts.pred_file




if opts.include_gazetteer=="0":
    parameters["include_gazetteer"]=False
else:
    parameters["include_gazetteer"]=True

if opts.include_word_features=="0":
    parameters["include_word_features"]=False
else:
    parameters["include_word_features"]=True

if opts.include_context=="0":
    parameters["include_context"]=False
else:
    parameters["include_context"]=True

if opts.print_latex_format=="0":
    parameters["print_latex_format"]=False
else:
    parameters["print_latex_format"]=True



parameters["context_window_len"]=int(opts.context_window_len)

parameters["conll_output_folder"]="Conll_Outputs/"
parameters["standoff_output_folder"]="Standoff_Outputs/"



