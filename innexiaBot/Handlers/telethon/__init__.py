from InnexiaBot import DEV_USERS, SUDOERS, telethn

IMMUNE_USERS = SUDOERS.union(DEV_USERS)

IMMUNE_USERS = (
    list(SUDOERS) + list(DEV_USERS)
)
