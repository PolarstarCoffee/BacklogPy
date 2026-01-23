import backlogObj

#backlog object edit methods

def edit_backlog_title(backlogObj, new_title):
    backlogObj.title = new_title
    return backlogObj
def edit_backlog_description(backlogObj, new_description):
    backlogObj.description = new_description
    return backlogObj