import PIL.Image
import PIL.ImageTk
from find_fundamental import fundamental_matrix
from prewarp import find_prewarp
from morph import delaunay_triangulation, transform_points
from pointCorrespondences import automatic_point_correspondences, getPointCorrespondences
from numpy.linalg import inv
from postwarp import getRectangle, getLines, homography, getPoints, homography_points
import cv2
import numpy as np


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter.filedialog import askopenfilename

from tkinter import messagebox

import UI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = View_Morphing (root)
    UI_support.init(root, top)
    root.mainloop()

w = None
def create_View_Morphing(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = View_Morphing (w)
    UI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_View_Morphing():
    global w
    w.destroy()
    w = None


class View_Morphing:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+428+145")
        top.title("View Morphing")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=-0.02, rely=0.0, relheight=1.01, relwidth=0.52)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=313)

        self.Entry1 = Entry(self.Canvas1)
        self.Entry1.place(relx=0.1, rely=0.2,height=20, relwidth=0.59)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label1 = Label(self.Canvas1)
        self.Label1.place(relx=0.1, rely=0.13, height=21, width=48)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Image 1''')

        self.Button1 = Button(self.Canvas1)
        self.Button1.place(relx=0.73, rely=0.2, height=24, width=78)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=self.button1comm)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Select Image''')

        self.Label2 = Label(self.Canvas1)
        self.Label2.place(relx=0.1, rely=0.35, height=21, width=48)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Image 2''')

        self.Entry2 = Entry(self.Canvas1)
        self.Entry2.place(relx=0.1, rely=0.42,height=20, relwidth=0.59)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Button2 = Button(self.Canvas1)
        self.Button2.place(relx=0.73, rely=0.42, height=24, width=78)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=self.button2comm)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Select Image''')

        self.Button3 = Button(self.Canvas1)
        self.Button3.place(relx=0.45, rely=0.68, height=24, width=95)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=self.start)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Start Processing''')

        #Output Canvas
        self.Canvas2 = Canvas(top)
        self.Canvas2.place(relx=0.5, rely=0.0, relheight=1.01, relwidth=0.51)
        self.Canvas2.configure(background="#d9d9d9")
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(highlightbackground="#d9d9d9")
        self.Canvas2.configure(highlightcolor="black")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(relief=RIDGE)
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(selectforeground="black")
        self.Canvas2.configure(width=303)
        
        
        
        
    def button1comm(self):
        filename = askopenfilename(filetypes=(("JPEG Files","*.jpg"),("PNG Files","*.png")))
        self.Entry1.delete(0,END)
        self.Entry1.insert(0,filename)
        
    def button2comm(self):
        filename = askopenfilename(filetypes=(("JPEG Files","*.jpg"),("PNG Files","*.png")))
        self.Entry2.delete(0,END)
        self.Entry2.insert(0,filename)

    def start(self):


        if len(self.Entry1.get()) == 0 or len(self.Entry2.get()) == 0:
            messagebox.showerror(title="View Morphing", message="Please Select a Image")
        else:

            image1 = cv2.imread(self.Entry1.get())
            image2 = cv2.imread(self.Entry2.get())

            # Find fundamental matrix
            F = fundamental_matrix(image1, image2)

            # Get homographies from the fundamental matrix
            H0, H1 = find_prewarp(F)

            # Use homographies to warp images
            new_size = int(np.sqrt(np.power(image1.shape[0], 2) + np.power(image1.shape[1], 2)))
            prewarp_1 = cv2.warpPerspective(image1, H0, (new_size, new_size))
            prewarp_2 = cv2.warpPerspective(image2, H1, (new_size, new_size))

            # Save result
            # cv2.imwrite('prewarp1.png', prewarp_1)
            # cv2.imwrite('prewarp2.png', prewarp_2)

            # Show result on screen. Click on any button to continue
            cv2.imshow('Prewarped image 1', prewarp_1)
            cv2.imshow('Prewarped image 2', prewarp_2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Morph the prewarped images
            points1, points2 = automatic_point_correspondences(prewarp_1, prewarp_2)

            #points1, points2 = automatic_point_correspondences(prewarp_1, prewarp_2)
            morphshape = np.shape(image1)
            morph = delaunay_triangulation(prewarp_1, prewarp_2, points1, points2, morphshape, removepoints=True)

            # save result
            # cv2.imwrite('morph.png', morph)

            # Show result on screen
            cv2.imshow('morph', morph)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Postwarp. Select point correspondences manually using mask, find homography and morph
            m_points = getPoints(morph)
            im = cv2.imread('E:/major/view-morphing-master/view-morphing-master/data/mask_einstein.jpg')
            p_points = getPoints(np.array(im).astype(np.uint8))

            # Find homography using the points
            H_s = homography_points(m_points, p_points)
            h, w, _ = image1.shape

            # warp image to desired plane
            final_morph = cv2.warpPerspective(morph, H_s, (h, w))

            cv2.imwrite('final_morph.png', final_morph)

            self.Canvas2.delete("all")

            showImg = PIL.ImageTk.PhotoImage(PIL.Image.open("final_morph.png"))

            # self.Canvas2.create_image(20, 20, image=showImg, anchor=NW)

            l = Label(self.Canvas2,image=showImg)
            l.image = showImg
            l.grid(row=2)

            # cv2.imshow('window', final_morph)

            # cv2.waitKey(0)
            # cv2.destroyAllWindows()



if __name__ == '__main__':
    vp_start_gui()