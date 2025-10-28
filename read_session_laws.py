import os
import pymupdf
import csv

folder = '/Users/reci9108/Jupyter/Sessions 2023 Extraordinary/'
files = os.listdir(folder)
data = {"metadata":None}
file_path = []

headers = [
    "title",
    "fulltext_url",
    "filename", 
    "cover_image_url",
    "additional_files",
    "keywords",
    "abstract",
    "author1_fname", 
    "author1_mname",
    "author1_lname",
    "author1_suffix",
    "author1_email",
    "author1_institution",
    "author1_is_corporate",
    "author2_fname",
    "author2_mname",
    "author2_lname",
    "author2_suffix",
    "author2_email",
    "author2_institution",
    "author2_is_corporate",
    "author3_fname",
    "author3_mname",
    "author3_lname",
    "author3_suffix",
    "author3_email",
    "author3_institution",
    "author3_is_corporate",
    "author4_fname",
    "author4_mname",
    "author4_lname",
    "author4_suffix",
    "author4_email",
    "author4_institution",
    "author4_is_corporate",
    "disciplines",
    "chapter",
    "comments",
    "document_type",
    "place_of_publication",
    "publication_date",
    "season",
    "session_law_topics",
    "session_num",
    "session_type",
    "start_page"
]

metadata = {
    "title" : None,
    "fulltext_url" : None,
    "filename" : None, 
    "cover_image_url" : None,
    "additional_files" : None,
    "keywords" : None,
    "abstract" : None,
    "author1_fname" : "Colorado General Assembly", 
    "author1_mname" : None,
    "author1_lname" : None,
    "author1_suffix" : None,
    "author1_email" : None,
    "author1_institution" : None,
    "author1_is_corporate" : "TRUE",
    "author2_fname" : None,
    "author2_mname" : None,
    "author2_lname" : None,
    "author2_suffix" : None,
    "author2_email" : None,
    "author2_institution" : None,
    "author2_is_corporate" : None,
    "author3_fname" : None,
    "author3_mname" : None,
    "author3_lname" : None,
    "author3_suffix" : None,
    "author3_email" : None,
    "author3_institution" : None,
    "author3_is_corporate" : None,
    "author4_fname" : None,
    "author4_mname" : None,
    "author4_lname" : None,
    "author4_suffix" : None,
    "author4_email" : None,
    "author4_institution" : None,
    "author4_is_corporate" : None,
    "disciplines" : None,
    "chapter" : None,
    "comments" : None,
    "document_type" : None,
    "place_of_publication" : "Denver",
    "publication_date" : "01/01/2023", #change this
    "season" : "",
    "session_law_topics" : None, #change this
    "session_num" : "1", #change this
    "session_type" : "Extraordinary" #change this regular, extraordinary, special
}

def create_file_names():
    for file in files:
        x = folder + file
        file_path.append(x)
create_file_names()

def write_csv():
    file_name = "sessions_2023_ext.csv"
    if not os.path.exists(file_name):
         with open(file_name,mode="w",newline='') as y:
             writer = csv.writer(y)
             writer.writerow(headers)
    with open(file_name,mode="a",newline='') as y:
        writer = csv.DictWriter(y,fieldnames=headers)
        writer.writerow(metadata)

def collect_metadata():
    for file in file_path:
        f = pymupdf.open(file)
        font = "1"
        text_content = "placeholder"
        font_size = {font:[text_content]}

        for pagenum in range(f.page_count):
            if pagenum == 0:
                page = f.load_page(pagenum)
                text_dict = page.get_text("dict")
                for block in text_dict["blocks"]:
                    if "lines" in block:
                        for line in block["lines"]:
                            for span in line["spans"]:
                                font = span["size"]
                                text_content = span["text"]
                                if font not in font_size:
                                    font_size[font]=([text_content])
                                else:
                                    font_size[font].extend([text_content])
            metadata["filename"] = file
            metadata["title"] = ("C" + font_size[6.960000038146973][0]+font_size[6.960000038146973][1]+font_size[6.960000038146973][2]+font_size[6.960000038146973][3]).title()
            metadata["chapter"] = font_size[7.980000019073486][0].removeprefix('CHAPTER ')
            if "AN ACT" in font_size[13.979999542236328][0]:
                metadata["document_type"] = "act"
            else:
                metadata["document_type"] = font_size[13.979999542236328][0]
            if "Ch." in font_size[10.979999542236328][0]:
                metadata["start_page"] = font_size[10.979999542236328][2]
            else:
                metadata["start_page"] = font_size[10.979999542236328][0]
        write_csv()
collect_metadata()
