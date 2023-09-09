import streamlit as st
import streamlit.components.v1 as components

    
def construct_block_html(item_header, item_list):
    """create a block of html codes which render as following

    item_header
    - item_list_element#1
    - item_list_element#2
    - item_list_element#3

    Args:
        item_header (str): Header of a list of elements
        item_list (list): List of text strings

    Returns:
        str: html code snippet as string
    """
    item_list_html = "".join(["<li>"+item+"</li>" for item in item_list])
    html_content = f""" 
    <div class="custom-content-block">
        <h2 class="custom-list-header">{item_header}</h2>
        <ul>
            {item_list_html}
        </ul>
    </div>
    """
    return html_content

def construct_result_html(item_dict: dict) -> str:
    """
    creates the code snippet to copy the content blocks into the clipboard
    and paste for later usage 

    Args:
        item_dict (dict): {item_header : item_list} in key-value pair

    Returns:
        str: html code snippet as string. includes css and js functions.
    """
    html_blocks_component = ""
    for item_header, item_list in item_dict.items():
        html_blocks_component += construct_block_html(item_header, item_list)

    js_component = """
    <script>
        let cblocks = document.querySelectorAll('.custom-content-block');
        let text = "";
        for (let i=0; i<cblocks.length; i++)
            {text = text + cblocks[i].innerText.replace(/(\n)/, String.raw'\n- ') + String.raw'\n\n'};
        const copyContent = async () => {
            try {
                await navigator.clipboard.writeText(text);
                let popup = document.getElementById('popup-text');
                popup.style.visibility = 'visible';
                setTimeout(() => {
                    popup.style.visibility = 'hidden';
                },800);
            } catch (err) {
                console.error('Failed to copy: ', err);
            }
        }
    </script>
    """
    with open('style.css') as f:
        css_component = f.read()
    
    html_component = f"""
    <meta charset="UTF-8">
    <style>{css_component}</style>
    <div>
        To Copy the text below, Click on
        <a style="margin-left: 1px; cursor: pointer; font-size: large;" onclick="copyContent()">&#128203;</a>
        <span id="popup-text" style="visibility: hidden;"><small>Copied !!</small></span>
    </div>
    <div data-stale="false" width="704" class="custom-element-container">
        <div class="stMarkdown" style="width: 704px;">
            {html_blocks_component}
        </div>
    </div>
    """
    return html_component+js_component

if __name__ == "__main__":
    item_header="This is header text" 
    item_list=["first","second","third","fourth","fifth","sixth"]
    item_dict = {
        "This is number list":["one - 1","two - 2","three - 3","four - 4","five - 5","six - 6"],
        "This is ordered list":["first","second","third","fourth","fifth","sixth"]
        }
    # page content header
    st.title("Welcome to Copy Testing")
    ## render the content
    test_html = construct_result_html(item_dict)
    components.html(test_html, width= 750, height=700, scrolling=True)

    ## for markdown only 
    markdown_content = f"## {item_header}\n- " + "\n- ".join(item_list) 
    st.markdown(markdown_content)