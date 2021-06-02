# Text rendering

import os
import re

def render2Txt(indir, outdir):
    text = ''
    dir_name = indir
    files = os.listdir(dir_name)
    files = [file for file in files if file.find('.txt') > -1]
    # files = ['line1.txt', 'line2.txt', 'line3.txt', 'line4.txt', 
    #          'line5.txt', 'line6.txt', 'line7.txt', 'line8.txt', 
    #          'line9.txt', 'line10.txt', 'line11.txt', 'line12.txt',
    #          'lin13.txt', 'line14.txt', 'line15.txt', 'line16.txt']
    all_text = ''
    
    for idx in range(len(files)):
        print(files[idx])
        file = open(dir_name + '\\' + files[idx], 'r')
        text = file.read()
        text = text.lower()
        text = re.sub(' +', ' ', text)
        text = re.sub(' \n','\n', text)
        text = re.sub('\n ', '\n',text)
        text = re.sub('\n+','\n', text)
        
        all_text += text + '\n'
        file.close()
    
    lines = all_text.split("\n")
    all_text = [line for line in lines if line.strip() != ""]
    
    final_text = ""
    for line in all_text:
          final_text += line + "\n"
        
    
    out_filename = indir.split('\\')[-1] + '.txt'
    out_file = open(outdir + '\\' + out_filename, 'w')
    out_file.write(final_text[:-1])
    out_file.close()
    
    
def render2Html(infile_path):
    filename = infile_path.split('\\')[-1]
    page_num  = filename[-8:-4]
    final_text = '<START>\n<TITLE>' + filename[:-4] + '</TITLE>\n<BODY>\n<p>Page ' + page_num + '</p>\n<p>'
    
    file = open(infile_path, 'r')
    text = file.read()
    
    final_text += re.sub('\n','<br>\n',text)
    
    # final_text = final_text[]
    final_text = final_text + '<br></p>\n</BODY>\n<END>'
    file.close()
    
    html_file = open(infile_path[:-4] + '.html', 'w')
    html_file.write(final_text)
    html_file.close()
    
def renderbulkText2Html(indir):
    dir_name = indir
    files = os.listdir(dir_name)
    files = [file for file in files if file.find('.TXT') > -1]
    
    for idx in range(len(files)):
        print(files[idx])
        file = open(dir_name + '\\' + files[idx], 'r')
        text = file.read()
        text = text.lower()
        text = re.sub(' +', ' ', text)
        text = re.sub(' \n','\n', text)
        text = re.sub('\n ', '\n',text)
        text = re.sub('\n+','\n', text)
        
        lines = text.split("\n")
        text = [line for line in lines if line.strip() != ""]
        
        final_text = ""
        for line in text:
              final_text += line + "\n"
              
        out_filename = files[idx][:-4] + '_new.txt'
        out_file = open(indir + '\\' + out_filename, 'w')
        out_file.write(final_text[:-1])
        out_file.close()
        
        print(out_filename)
        render2Html(indir + '\\' + out_filename)
        
render2Txt('SH10292','SH10292')
render2Html('SH10292\SH10292.txt')
# renderbulkText2Html('8_files')