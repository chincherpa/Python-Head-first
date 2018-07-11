from string import Template


def antwort_anfang():
    """
    High level support for doing this and that.

    high level support for doing this and that.
    """
    return('Content-type: text/html\n\n')


def seitenanfang(titel):
    """
    High level support for doing this and that.

    high level support for doing this and that.
    """
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=titel))


def seitenende(the_links):
    """
    High level support for doing this and that.

    high level support for doing this and that.
    """
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))


def form_anfang(the_url, form_type="POST"):
    """
    High level support for doing this and that.

    high level support for doing this and that.
    """
    return('<form action="' + the_url + '" method="' + form_type + '">')


def form_ende(submit_txt="Absenden"):
    """
    High level support for doing this and that.

    high level support for doing this and that.
    """
    return('<p></p><input type=submit value="' + submit_txt + '"></form>')


def radio_button(rb_name, rb_wert):
    """
    High level support for doing this and that.

    high level support for doing this and that.
    """
    return('<input type="radio" name="' + rb_name +
        '" value="' + rb_wert + '"> ' + rb_wert + '<br />')


def u_liste(l_elemente):
    """
    High level support for doing this and that.

    high level support for doing this and that.
    """
    u_string = '<ul>'
    for item in l_elemente:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)


def header(h_text, h_ebene=2):
    """
    High level support for doing this and that.

    high level support for doing this and that.
    """
    return('<h' + str(h_ebene) + '>' + h_text +
           '</h' + str(h_ebene) + '>')


def para(p_text):
    """
    High level support for doing this and that.

    high level support for doing this and that.
    """
    return('<p>' + p_text + '</p>')
