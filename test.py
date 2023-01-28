from aiogram.dispatcher.fsm.context import FSMContext

@router.message(Command(commands=["test"]))
async def cmd_test(message: Message, state: FSMContext):
    await message.answer(
        text="Когда вы рассказываете дома о своей работе, вы обычно употребляете?:",
        reply_markup=make_row_keyboard(available_answer_options)
    )
    await state.set_state(ChooseAnswer.choosing_answer)

