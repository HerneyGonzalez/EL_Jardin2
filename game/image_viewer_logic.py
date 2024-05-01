# image_viewer_logic.py

def filter_image_name(filter_string):
    filtered_list = []
    filter_elements = filter_string.split()
    if filter_elements:
        for name in get_image_name_candidates():
            if name[0].startswith(filter_elements[0]):
                if len(filter_elements) == 1:
                    filtered_list.append(" ".join(name))
                else:
                    for e in filter_elements[1:]:
                        if e in name:
                            continue
                        else:
                            for e2 in name[1:]:
                                if e2.startswith(e):
                                    break
                            else:
                                break
                            continue
                    else:
                        filtered_list.append(" ".join(name))
    else:
        filtered_list = list({name[0] for name in renpy.display.image.images})
    return filtered_list

def put_clipboard_text(s):
    from pygame import scrap, locals
    scrap.put(locals.SCRAP_TEXT, s.encode("utf-8"))
    renpy.notify("'{}'\nis copied to clipboard".format(s))

def tag_completion(filter_string, filtered_list):
    if filter_string and filter_string[-1] != " ":
        completed_string = filter_string.split()[-1]
        candidate = []
        if len(filter_string.split()) == 1:
            for es in filtered_list:
                candidate.append(es.split()[0])
        else:
            for es in filtered_list:
                for e in es.split()[1:]:
                    if e.startswith(completed_string):
                        candidate.append(e)
        cs = renpy.current_screen()
        cs.scope["filter_string"] += candidate[0][len(completed_string):] + " "
        input = renpy.get_displayable("_image_selecter", "input_filter_strings")
        input.caret_pos = len(cs.scope["filter_string"])

def _image_viewer_hide():
    renpy.hide("preview", layer="screens")
    renpy.restart_interaction()

class ShowImage:
    def __init__(self, image_name_tuple):
        self.string = " ".join(image_name_tuple)
        self.check = None

    def __call__(self):
        if self.check is None:
            for n in get_image_name_candidates():
                if set(n) == set(self.string.split()) and n[0] == self.string.split()[0]:
                    self.string = " ".join(n)
                    try:
                        for fn in renpy.display.image.images[n].predict_files():
                            if not renpy.loader.loadable(fn):
                                self.check = False
                                break
                        else:
                            self.check = True
                    except:
                        self.check = True #text displayable or Live2D
        try:
            if self.check:
                renpy.show(self.string, at_list=[renpy.store.truecenter], layer="screens", tag="preview")
            else:
                renpy.show("preview", what=renpy.text.text.Text("No files", color="#F00"), at_list=[renpy.store.truecenter], layer="screens")
        except:
            renpy.show("preview", what=renpy.text.text.Text("No files", color="#F00"), at_list=[renpy.store.truecenter], layer="screens")
        renpy.restart_interaction()

class Add_tag_or_Return:
    def __init__(self, image_name_tuple):
        self.image_name_tuple = image_name_tuple
        self.string = " ".join(image_name_tuple)
        self.check = None

    def __call__(self):
        if self.check is None:
            for n in get_image_name_candidates():
                if set(n) == set(self.string.split()) and n[0] == self.string.split()[0]:
                    self.string = " ".join(n)
                    try:
                        for fn in renpy.display.image.images[n].predict_files():
                            if not renpy.loader.loadable(fn):
                                self.check = False
                                break
                        else:
                            self.check = True
                    except:
                        self.check = False #text displayable or Live2D
        if self.check:
            if in_editor:
                return self.image_name_tuple
            else:
                put_clipboard_text(self.string)

        else:
            cs = renpy.current_screen()
            cs.scope["filter_string"] = self.string + " "
            input = renpy.get_displayable("_image_selecter", "input_filter_strings")
            input.caret_pos = len(cs.scope["filter_string"])
            renpy.restart_interaction()
