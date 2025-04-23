if __name__ == '__main__':
    import asyncio
    import handlers.command
    import handlers.message
    from ww_casino.bot_related.useful import config


    async def main():
        config.dp.include_router(handlers.command.router)
        config.dp.include_router(handlers.message.router)

        await config.dp.start_polling(config.bot)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
