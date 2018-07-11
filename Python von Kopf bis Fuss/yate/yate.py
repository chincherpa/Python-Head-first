
from string import Template

def antwort_anfang(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

def seitenanfang(titel):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def seitenende(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def form_anfang(die_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

def form_ende(submit_txt="Absenden"):
    return('<p></p><input type=submit value="' + submit_txt + '"></form>')

def radio_button(rb_name, rb_wert):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_wert + '"> ' + rb_wert + '<br />')

def u_liste(l_elemente):
    u_string = '<ul>'
    for item in l_elemente:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(h_text, h_ebene=2):
    return('<h' + str(h_ebene) + '>' + h_text +
           '</h' + str(h_ebene) + '>')

def para(p_text):
    return('<p>' + p_text + '</p>') 
