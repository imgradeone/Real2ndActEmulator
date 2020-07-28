# MAS-import_ddlc_persistent 68ecb44-dirty-CNModTemp

# This file imports save data from DDLC without changing the original data.
# By default, when this is run all relevant data from DDLC is imported.
# Handling of individual variables can be handled by changing the settings below.
init python:
    def dumpPersistentToFile(dumped_persistent,dumppath):
        """
        Prints a file containing each dictionary element of a persistent variable

        IN:
            dumped_persistent - a renpy persistent variable
            dumppath - a file path to the text file to be created. Must be a valid write location
        """
        dumped_persistent = vars(dumped_persistent)

        fo = open(dumppath, "w")

        for key in sorted(dumped_persistent.iterkeys()):
            fo.write(str(key) + ' - ' + str(type(dumped_persistent[key])) + ' >>> '+ str(dumped_persistent[key]) + '\n\n')

        fo.close()

label import_ddlc_persistent:
    python:
        #NOTE: import glob alone causes a LOT of lag. We're just importing what we need here
        from glob import glob

        # Check for saves in platform-specific location.
        if renpy.macintosh:
            rv = "~/Library/RenPy/"
            check_path = os.path.expanduser(rv)

        elif renpy.windows:
            if 'APPDATA' in os.environ:
                check_path =  os.environ['APPDATA'] + "/RenPy/"
            else:
                rv = "~/RenPy/" # todo: ~/AppData/Roaming/RenPy/ works!
                check_path = os.path.expanduser(rv)

        else:
            rv = "~/.renpy/"
            check_path = os.path.expanduser(rv)

        ddlc_save_path = glob(check_path + 'DDLC/persistent')
        if not ddlc_save_path:
            ddlc_save_path = glob(check_path + 'DDLC-*/persistent')

    #We have something to import
    if ddlc_save_path:
        $ ddlc_save_path = ddlc_save_path[0]
        call screen confirm(message="找到了一份 DDLC 存档。\n你确定要把它导入到 [config.name] 的存档里吗？", yes_action=NullAction(), no_action=Jump("import_ddlc_explict_return"))

    #Nothing to import
    else:
        call screen dialog(message="找不到任何 DDLC 存档。", ok_action=Return())
        jump import_ddlc_explict_return

    #Open the persistent save file as ddlc_persistent
    python:
        ddlc_pfile = file(ddlc_save_path, "rb")
        s = ddlc_pfile.read().decode("zlib")
        ddlc_pfile.close()

        from renpy.loadsave import loads
        ddlc_persistent = loads(s)

        #NOTE: WE ALWAYS ATTEMPT TO MERGE PERSISTENTS, OVERWRITING ONLY IF OLD DATA DOES NOT EXIST

        #These are all of the persistent variables from a DDLC save
        ##Unimportant/unused variables
        #_achievement_progress #Achievements not yet implemented. Might change in the future
        #_achievements
        #_changed #Dictionary tracks when its values were changed
        #_character_volume #Empty
        #_file_folder
        #_file_page
        #_file_page_name
        #_iap_purchases
        #_preference_default
        #_preferences
        #_set_preferences
        #_style_preferences
        #_virtual_size
        #_voice_mute
        #demo
        #first_poem #Unused?
        #menu_bg_m #True if the player opened the main menu
        #monika_back #Unused
        #seen_colors_poem #Unused

        #Update variables
        #These are currently not used, but may be in the future
        #We could also use this to inform players of new versions for MAS
        #_update_last_checked
        #_update_version

        #Anticheat
        #An integer number used for checking if persistent has been tampered with. Don't change this value even if replacing old save
        #anticheat

        #Autoload
        #Label that tells splash.rpy where to go when the game starts. We don't want to carryover that part of the game flow.
        #autoload

        #first_load
        #Used to tell if a specific user tip was shown on startup...seems redundant with #first_run
        #first_load

        #first_run
        #Used to tell if the game has completed a full start-up sequence on this save.
        #Not to be confused with the firstrun file found in the install folder
        #first_run

        #START: Utility transfer functions
        def _updatePersistentDict(key, old_persistent, new_persistent):
            """
            Merges the old persistent dict at the key provided into the new persistent

            IN:
                key - key to update
                old_persistent - persistent to copy data from
                new_persistent - persistent to copy data to

            NOTE: Should only be used to update dicts
            """

            if old_persistent.__dict__[key] is not None:
                if new_persistent.__dict__[key] is not None:
                    new_persistent.__dict__[key].update(old_persistent.__dict__[key])

                else:
                    new_persistent.__dict__[key] = old_persistent.__dict__[key]

        def _updatePersistentBool(key, old_persistent, new_persistent):
            """
            Merges bools from the old persistent at the key provided into the new persistent

            IN:
                key - key to update
                old_persistent - persistent to copy data from
                new_persistent - persistent to copy data to

            NOTE: Should only be used to update bools
            """
            if old_persistent.__dict__[key] is not None:
                if new_persistent.__dict__[key] is not None:
                    new_persistent.__dict__[key] = new_persistent.__dict__[key] or old_persistent.__dict__[key]

                else:
                    new_persistent.__dict__[key] = old_persistent.__dict__[key]


        #START: Transfers
        #_seen_ever: A dict storing all the labels we've seen through the game
        _updatePersistentDict("_seen_ever", ddlc_persistent, persistent)

        #_seen_audio: A dict storing all the audio we've heard through the game
        _updatePersistentDict("_seen_audio", ddlc_persistent, persistent)

        #_seen_images: A dict storing all images the player has seen
        _updatePersistentDict("_seen_images", ddlc_persistent, persistent)

        #clearall: Whether or not the player has achieved the perfect ending
        _updatePersistentBool("clearall", ddlc_persistent, persistent)

        #monika_kill: Whether or not the player has deleted Monika's character file in act 3
        _updatePersistentBool("monika_kill", ddlc_persistent, persistent)

        #tried_skip: Whether or not the player has tried to skip Monika's dialogue in act 3
        _updatePersistentBool("tried_skip", ddlc_persistent, persistent)

        #monika_reload: How many times the player has reloaded into ch30
        if ddlc_persistent.monika_reload is not None:
            persistent.monika_reload = ddlc_persistent.monika_reload

        #clear: A list of 10 booleans marking which CG's were unlocked in play
        if ddlc_persistent.clear is not None:
            if persistent.clear is not None:
                for index in range(len(persistent.clear)-1):
                    persistent.clear[index] = persistent.clear[index] or ddlc_persistent.clear[index]

            else:
                persistent.clear = ddlc_persistent.clear

        #playername: Player's name for the MC in DDLC
        if ddlc_persistent.playername:
            if persistent.playername and persistent.playername != ddlc_persistent.playername:
                renpy.call_in_new_context("ddlc_persistent_merge_unmatched_names")

            else:
                persistent.playername = ddlc_persistent.playername

        player = persistent.playername

        #playthrough: What act did we leave off on? (0: intro, 1: act 1, 2: act 2, 3: act 3, 4: act 4)
        #NOTE: We only carry this over if we've gone farther on the ddlc persist than the current persist
        if ddlc_persistent.playthrough is not None:
            if (
                persistent.playthrough is not None
                and persistent.playthrough < ddlc_persistent.playthrough
            ):
                persistent.playthrough = ddlc_persistent.playthrough

            else:
                persistent.playthrough = ddlc_persistent.playthrough

    call screen dialog(message="存档已合并。", ok_action=Return())
    label import_ddlc_explict_return:
        return

label ddlc_persistent_merge_unmatched_names:
    $ quick_menu_orig = quick_menu
    $ quick_menu = False
    "两个存档之间的玩家名称不相符。如何称呼您？"
    window hide dissolve
    menu:
        "[ddlc_persistent.playername]":
            $ persistent.playername = ddlc_persistent.playername
        "[persistent.playername]":
            pass
    $ quick_menu = quick_menu_orig
    window auto dissolve # checklater
    return
