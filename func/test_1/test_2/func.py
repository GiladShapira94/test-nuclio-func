def handler(context,event):
    context.logger.info("INFO")
    context.logger.warn("WARN")
    context.logger.debug("DEBUG")
    context.logger.error("ERROR")
    return "nuclio"
