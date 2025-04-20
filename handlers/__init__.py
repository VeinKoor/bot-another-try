from handlers.user.transactions.add_income_handler import router as add_income_router
from handlers.user.transactions.add_expense_handler import router as add_expense_router
from handlers.user.profile.profile_handler import router as profile_router
from .user.start_handler import router as start_router
from handlers.user.profile.statistic_handler import router as statistic_router
from handlers.user.settings.settings_router import router as settings_router
from handlers.user.settings.change_name import router as change_name_router
from handlers.user.settings.set_limit import router as set_limit_router

routers = (
    add_income_router,
    add_expense_router,
    profile_router,
    start_router,
    statistic_router,
    settings_router,
    change_name_router,
    set_limit_router,
)
