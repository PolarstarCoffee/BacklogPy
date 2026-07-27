import backlogObj

#backlog object edit methods

def edit_backlog_title(backlogObj, new_title):
    backlogObj.title = new_title
    return backlogObj
def edit_backlog_description(backlogObj, new_description):
    backlogObj.description = new_description
    return backlogObj

def edit_backlog_status(backlogObj, new_status):
    backlogObj.status = new_status
    return backlogObj

def edit_backlog_thumbnail(backlogObj, new_thumbnail):
    backlogObj.thumbnail = new_thumbnail
    return backlogObj

def edit_backlog_rating(backlogObj, new_rating):
    backlogObj.rating = new_rating
    return backlogObj
