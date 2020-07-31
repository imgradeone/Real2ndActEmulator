# DDMM SDK v4.0.0-prerelease-CNModTemp

# Initialise the DDMM SDK
init -10 python:
    import urllib2, json
    ddmm_rpc_url = "http://127.0.0.1:41420/"

    def ddmm_check_online():
        try:
            request = urllib2.Request(ddmm_rpc_url, json.dumps({"method": "ping"}))
            urllib2.urlopen(request).read()
            return True
        except:
            return False
        return False

    def ddmm_make_request(payload):
        if ddmm_check_online():
            request = urllib2.Request(ddmm_rpc_url, json.dumps(payload))
            urllib2.urlopen(request).read()

    def ddmm_register_achievement(id, name, description):
        ddmm_make_request({"method": "register achievement", "payload": {"id": id, "name": name, "description": description}})

    def ddmm_earn_achievement(id):
        ddmm_make_request({"method": "earn achievement", "payload": {"id": id}})

    def grant_achievement_all(renpy_desc, ddmm_id):
        achievement.grant(renpy_desc)
        if persistent.ddmm_mode and ddmm_id != "":
            ddmm_earn_achievement(ddmm_id)
        renpy.notify("你达成了一个成就。")

# Register an achievement with Doki Doki Mod Manager
# id = the unique ID of the achievement, can be any string
# name = the user-facing name of the achievement
# description = the user-facing description of the achievement
label ddmm_register_achievement(id, name, description):
    $ ddmm_register_achievement(id, name, description)    
    return

# Earn an achievement
# id = the unique ID of the achievement
label ddmm_earn_achievement(id):
    $ ddmm_earn_achievement(id)        
    return

# label grant_achievement_all(renpy_desc, ddmm_id):
#     python:
#         achievement.grant(renpy_desc)
#         if persistent.ddmm_mode and ddmm_id != "":
#             ddmm_earn_achievement(ddmm_id)
#     show screen notify("达成成就：[renpy_desc]")
#     return



init -10 python:
    def register_achievement_all(name, id, description):
        achievement.register(name)
        ddmm_register_achievement(id, name, description)