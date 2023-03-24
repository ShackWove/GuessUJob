import sys
sys.path.insert(0, "../../source_code")
import threading
from tkinter import *
from tkinter import ttk
import customtkinter
import os
from PIL import Image
from business_logic.Data import Data
from business_logic.Model import Model
#import time

# TODO Provare a rendere tutto con anche la progress bar
#class progressive(customtkinter.CTk):
#    def __init__(self, progress_window):
#        self.progress_window = progress_window
#        self.prog_label = customtkinter.CTkLabel(self.progress_window, text=self.bold_font)
#        self.prog_label.grid(row=0, sticky="nsew", pady=10)
#        
#        self.prog_bar = customtkinter.CTkProgressBar(master=self.progress_window, mode='indeterminate')
#        self.prog_bar.grid(row=1, sticky="nsew", pady=10)
#                    
#        def start_scan(self):
#            self.prog_bar.start(10)
#            time.sleep(10)
#            self.finished_scan()
#
#        def finished_scan(self):
#            self.prog_bar.stop()
#            self.prog_label.destroy()
#            self.prog_bar.destroy()

class gui_ai(customtkinter.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.title("UGotTheJob")
        self.geometry(f"700x800")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=4)
        self.resizable(False, False)
        
        # icon path
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), ("../../documentation"))
        logo_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), ("/logos"))
        
        # icon implementation path
        self.logo_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "job_seeking.png")), size=(100, 100))
        self.search_logo = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "search_light.png")), size=(30, 30))
        
        # main font and dim
        main_font = customtkinter.CTkFont(size=18)
        
        def top_research():
            top_font = customtkinter.CTkFont(size=15)
            bold_font = customtkinter.CTkFont(size=16, weight="bold")
            
            var1 = float(self.ssc_percentage.get())
            
            var2 = self.ssc_board.get()
            if var2 == 'Others':
                var2 = int(1)
            else:
                var2 = int(0)
                 
            var3 = float(self.hsc_percentage.get())
            
            var4 = self.hsc_subject.get()
            if var4 == 'Others':
                var4 = int(1)
            else:
                var4 = int(0)
                    
            var5 = self.button_subject.get()
            if var5 == 'Commerce':
                var5 = int(1)
            if var5 == 'Science':
                var5 = int(2)
            else:
                var5 = int(0)
            
            var6 = float(self.degree_entry.get())
            
            var7 = self.button_subject_laurea.get()
            # ["Sci&tech", "Comm&Mgmt", "Others"]
            if var7 == 'Sci&tech':
                var7 = int(2)
            if var7 == 'Others':
                var7 = int(1)
            else:
                var7 = int(0)
                
            var8 = self.button_subject_work.get()
            if var8 == 'Si':
                var8 = int(1)
            else:
                var8 = int(0)
            
            var9 = self.button_subject_specialization.get()
            # ["Mkt&HumanR","Mkt&Finance"]
            if var9 == 'Mkt&HumanR':
                var9 = int(1)
            else:
                var9 = int(0)
            
            var_label_1 = "SSC %: "
            var_label_2 = "SSC board: "
            var_label_3 = "HSC %: "
            var_label_4 = "HSC board: "
            var_label_5 = "Subject: "
            var_label_6 = "Degree %: "
            var_label_7 = "Undergrad: "
            var_label_8 = "Work ExP: "
            var_label_9 = "Specialization: "
            
            print(var1, var2, var3, var4, var5, var6, var7, var8, var9)
            print(type(var1), type(var2), type(var3), type(var4), type(var5), type(var6), type(var7), type(var8), type(var9))
            
            top_research_window = customtkinter.CTkToplevel()
            top_research_window.geometry(f"700x800")
            top_research_window.title("Scan profile")
            
            self.frame_resec = customtkinter.CTkFrame(top_research_window, fg_color="transparent")
            self.frame_resec.grid(sticky="nsew")
            self.frame_resec.place(relx=0.5, rely=0.5, anchor="c")
            
            # label data
            label_data = customtkinter.CTkLabel(self.frame_resec, text="Dati inseriti:", font=customtkinter.CTkFont(size=18, weight="bold"))
            label_data.grid(row=0, sticky="nsw", pady=10)
            
            # dati inseriti frame
            data_frame = customtkinter.CTkFrame(self.frame_resec)
            data_frame.grid(row=1, sticky="new", padx=10, pady=10)
            
            # ssc frame 1
            ssc_1_frame = customtkinter.CTkFrame(data_frame)
            ssc_1_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=10)
            
            ssc_label_1 = customtkinter.CTkLabel(ssc_1_frame, text=var_label_1, font=bold_font)
            ssc_label_1.grid(row=0, column=0)
            
            ssc_label_2 = customtkinter.CTkLabel(ssc_1_frame, text=var1, font=top_font)
            ssc_label_2.grid(row=0, column=1)
            
            # ssc frame 2
            ssc_2_frame = customtkinter.CTkFrame(data_frame)
            ssc_2_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=10)
            
            ssc_label_3 = customtkinter.CTkLabel(ssc_2_frame, text=var_label_2, font=bold_font)
            ssc_label_3.grid(row=0, column=0)
            
            ssc_label_4 = customtkinter.CTkLabel(ssc_2_frame, text=var2, font=top_font)
            ssc_label_4.grid(row=0, column=1)
            
            # hsc frame 1
            hsc_1_frame = customtkinter.CTkFrame(data_frame)
            hsc_1_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=10)
            
            hsc_label_1 = customtkinter.CTkLabel(hsc_1_frame, text=var_label_3, font=bold_font)
            hsc_label_1.grid(row=0, column=0)
            
            hsc_label_2 = customtkinter.CTkLabel(hsc_1_frame, text=var3, font=top_font)
            hsc_label_2.grid(row=0, column=1)
            
            #hsc frame 2
            hsc_2_frame = customtkinter.CTkFrame(data_frame)
            hsc_2_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=10)
            
            hsc_label_3 = customtkinter.CTkLabel(hsc_2_frame, text=var_label_4, font=bold_font)
            hsc_label_3.grid(row=0, column=0)
            
            hsc_label_4 = customtkinter.CTkLabel(hsc_2_frame, text=var4, font=top_font)
            hsc_label_4.grid(row=0, column=1)
            
            # hsc frame 3
            hsc_3_frame = customtkinter.CTkFrame(data_frame)
            hsc_3_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=10)
            
            hsc_label_3 = customtkinter.CTkLabel(hsc_3_frame, text=var_label_5, font=bold_font)
            hsc_label_3.grid(row=0, column=0)
            
            hsc_label_4 = customtkinter.CTkLabel(hsc_3_frame, text=var5, font=top_font)
            hsc_label_4.grid(row=0, column=1)
            
            # deg frame
            deg_frame = customtkinter.CTkFrame(data_frame)
            deg_frame.grid(row=2, column=1, sticky="nsew", padx=5, pady=10)
            
            deg_label = customtkinter.CTkLabel(deg_frame, text=var_label_6, font=bold_font)
            deg_label.grid(row=0, column=0)
            
            deg_label_1 = customtkinter.CTkLabel(deg_frame, text=var6, font=top_font)
            deg_label_1.grid(row=0, column=1)
            
            # undergrad frame
            und_frame = customtkinter.CTkFrame(data_frame)
            und_frame.grid(row=0, column=2, sticky="nsew", padx=5, pady=10)
            
            und_label = customtkinter.CTkLabel(und_frame, text=var_label_7, font=bold_font)
            und_label.grid(row=0, column=0)
            
            und_label_1 = customtkinter.CTkLabel(und_frame, text=var7, font=top_font)
            und_label_1.grid(row=0, column=1)
            
            # work frame
            work_frame = customtkinter.CTkFrame(data_frame)
            work_frame.grid(row=1, column=2, sticky="nsew", padx=5, pady=10)
            
            work_label = customtkinter.CTkLabel(work_frame, text=var_label_8, font=bold_font)
            work_label.grid(row=0, column=0)
            
            work_label_1 = customtkinter.CTkLabel(work_frame, text=var8, font=top_font)
            work_label_1.grid(row=0, column=1)
            
            # specialization frame
            speck_frame = customtkinter.CTkFrame(data_frame)
            speck_frame.grid(row=2, column=2, sticky="nsew", padx=5, pady=10)
            
            spec_label = customtkinter.CTkLabel(speck_frame, text=var_label_9, font=bold_font)
            spec_label.grid(row=0, column=0)
            
            spec_label_1 = customtkinter.CTkLabel(speck_frame, text=var9, font=top_font)
            spec_label_1.grid(row=0, column=1)
            
            # progress bar
            #self.frame_prog = customtkinter.CTkFrame(self.progress_window)
            #self.frame_prog.grid(row=3, sticky="nsew", padx=10, pady=10)
            
            #action = progressive(self.frame_prog)
            
            #tread = threading.Thread(target=action.start_scan())
            #tread.start()
            data = Data.prepare_data(var1, var2, var3, var4, var5, var6, var7, var8, var9)
            print(Model.prediction_model(data))
            print("\n\n")

        
        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(sticky="nsew")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="c")
        
        self.main_frame_label = customtkinter.CTkLabel(self.main_frame, text=" UGotTheJob", image=self.logo_icon,
                                                       compound="left",
                                                       font=customtkinter.CTkFont(size=40, weight="bold"))
        self.main_frame_label.grid(row=0, column=0, sticky="nsew")
        
        self.center_frame = customtkinter.CTkFrame(self.main_frame)
        self.center_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=20)
        
        # voti frame form SSC
        self.ssc_percentage_frame = customtkinter.CTkFrame(self.center_frame, fg_color="transparent")
        self.ssc_percentage_frame.grid(row=0, column=0, sticky="nsew", padx=20)
        
        self.label_ssc_percentage = customtkinter.CTkLabel(self.ssc_percentage_frame, text="Inserire Voto SSC: ", font=main_font)
        self.label_ssc_percentage.grid(row=0, column=0, pady=10, sticky="nsew")
        
        self.ssc_percentage = customtkinter.CTkEntry(master=self.ssc_percentage_frame, placeholder_text="0-100%", font=main_font)
        self.ssc_percentage.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # ssc board liceo
        self.ssc_board_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.ssc_board_frame.grid(row=1, column=0, sticky="nsew", padx=20)
        
        self.ssc_board_frame_label = customtkinter.CTkLabel(self.ssc_board_frame, text="Inserire una delle materie HSC: ", font=main_font)
        self.ssc_board_frame_label.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.ssc_var_subject = customtkinter.StringVar(value="Central")
        self.ssc_board = customtkinter.CTkSegmentedButton(master=self.ssc_board_frame, values=["Central", "Others"], font=main_font, variable=self.ssc_var_subject)
        self.ssc_board.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # voti frame form
        self.hsc_percentage_frame = customtkinter.CTkFrame(self.center_frame, fg_color="transparent")
        self.hsc_percentage_frame.grid(row=2, column=0, sticky="nsew", padx=20)
        
        self.label_hsc_percentage = customtkinter.CTkLabel(self.hsc_percentage_frame, text="Inserire Voto HSC: ", font=main_font)
        self.label_hsc_percentage.grid(row=0, column=0, pady=10, sticky="nsew")
        
        self.hsc_percentage = customtkinter.CTkEntry(master=self.hsc_percentage_frame, placeholder_text="0-100%", font=main_font)
        self.hsc_percentage.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # Hsc board
        self.hsc_board_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.hsc_board_frame.grid(row=3, column=0, sticky="nsew", padx=20)
        
        self.hsc_board_frame_label = customtkinter.CTkLabel(self.hsc_board_frame, text="Inserire una delle materie HSC: ", font=main_font)
        self.hsc_board_frame_label.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.hsc_var_subject = customtkinter.StringVar(value="Central")
        self.hsc_subject = customtkinter.CTkSegmentedButton(master=self.hsc_board_frame, values=["Central", "Others"], font=main_font, variable=self.hsc_var_subject)
        self.hsc_subject.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # subject liceo
        self.subject_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.subject_frame.grid(row=4, column=0, sticky="nsew", padx=20)
        
        self.subject_label = customtkinter.CTkLabel(self.subject_frame, text="Inserire una delle materie HSC: ", font=main_font)
        self.subject_label.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.button_var_subject = customtkinter.StringVar(value="Commerce")
        self.button_subject = customtkinter.CTkSegmentedButton(master=self.subject_frame, values=["Commerce", "Science", "Arts"], font=main_font, variable=self.button_var_subject)
        self.button_subject.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # laurea degree
        self.degree_mark_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.degree_mark_frame.grid(row=5, column=0, sticky="nsew", padx=20)
        
        self.degree_label = customtkinter.CTkLabel(self.degree_mark_frame, text="Inserire voto Degree: ", font=main_font)
        self.degree_label.grid(row=0, column=0, pady=10, sticky="nsew")
        
        self.degree_entry = customtkinter.CTkEntry(master=self.degree_mark_frame, placeholder_text="0-100%", font=main_font)
        self.degree_entry.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # laurea soggetto
        self.degree_object_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.degree_object_frame.grid(row=6, column=0, sticky="nsew", padx=20)
        
        self.laurea_subject = customtkinter.CTkLabel(self.degree_object_frame, text="Inserire in cosa si è laureati: ", font=main_font)
        self.laurea_subject.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.button_var_laurea = customtkinter.StringVar(value="Sci&tech")
        self.button_subject_laurea = customtkinter.CTkSegmentedButton(master=self.degree_object_frame, values=["Sci&tech", "Comm&Mgmt", "Others"], font=main_font, variable=self.button_var_laurea)
        self.button_subject_laurea.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # work exp
        self.work_object_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.work_object_frame.grid(row=7, column=0, sticky="nsew", padx=20)
        
        self.work_subject = customtkinter.CTkLabel(self.work_object_frame, text="Inserire si è lavorato in passato: ", font=main_font)
        self.work_subject.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.button_var_work = customtkinter.StringVar(value="Si")
        self.button_subject_work = customtkinter.CTkSegmentedButton(master=self.work_object_frame, values=["Si","No"], font=main_font, variable=self.button_var_work)
        self.button_subject_work.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # specialistica
        self.specialization_object_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.specialization_object_frame.grid(row=8, column=0, sticky="nsew", padx=20)
        
        self.specialization_subject = customtkinter.CTkLabel(self.specialization_object_frame, text="Inserire si è lavorato in passato: ", font=main_font)
        self.specialization_subject.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.button_var_specialization = customtkinter.StringVar(value="Mkt&HumanR")
        self.button_subject_specialization = customtkinter.CTkSegmentedButton(master=self.specialization_object_frame,
                                                                              values=["Mkt&HumanR","Mkt&Finance"], font=main_font, variable=self.button_var_specialization)
        self.button_subject_specialization.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        self.scan_button = customtkinter.CTkButton(master=self.main_frame, text="Ricerca ", image=self.search_logo,
                                                       compound="right", command=top_research,
                                                       font=customtkinter.CTkFont(size=30, weight="bold"))
        self.scan_button.grid(row=3, column=0, sticky="ns")
        
if __name__ == "__main__":
    
    app = gui_ai()
    app.mainloop()