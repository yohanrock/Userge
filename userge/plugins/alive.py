from userge import userge
from pyrogram.errors.exceptions import FileIdInvalid, FileReferenceEmpty

LOGO_STICKER_ID, LOGO_STICKER_REF = None, None


@userge.on_cmd("alive", about="__This command is just for fun XD__")
async def alive(_, message):
    await message.delete()

    try:
        if LOGO_STICKER_ID:
            await sendit(LOGO_STICKER_ID, message)

        else:
            await refresh_id()
            await sendit(LOGO_STICKER_ID, message)
            
    except FileIdInvalid:
        await refresh_id()
        await sendit(LOGO_STICKER_ID, message)
    except FileReferenceEmpty:
        await refresh_id()
        await sendit(LOGO_STICKER_ID, message)

    await userge.send_message(message.chat.id, "`USERGE is Up and Running`")


async def refresh_id():
    global LOGO_STICKER_ID, LOGO_STICKER_REF
    sticker = (await userge.get_messages('theUserge', 8)).sticker
    LOGO_STICKER_ID = sticker.file_id
    LOGO_STICKER_REF = sticker.file_ref


async def sendit(fileid, message):
    await userge.send_sticker(message.chat.id, fileid, file_ref=LOGO_STICKER_REF)