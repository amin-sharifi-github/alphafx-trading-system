"""
Configuration for OANDA Multi-Timeframe Trading System
Enhanced with research-based optimizations for profitable short-term trading
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file (if exists)
load_dotenv()

# OANDA API Settings
OANDA_API_KEY = os.getenv("OANDA_API_KEY", "API_KEY")
OANDA_ACCOUNT_ID = os.getenv("OANDA_ACCOUNT_ID", "ACCOUNT_ID")
OANDA_ENVIRONMENT = os.getenv("OANDA_ENVIRONMENT", "practice")  # "practice" or "live"

# Trading Parameters - Enhanced based on research
INSTRUMENTS = {
    "EUR_USD": {"enabled": False, "name": "Euro/US Dollar", "weight": 0.5, "pip_value": 0.0001, "volatility_factor": 1.0},  # DISABLED: -$931 single trade loss
    "GBP_USD": {"enabled": True, "name": "British Pound/US Dollar", "weight": 1.5, "pip_value": 0.0001, "volatility_factor": 1.2},  # ENABLED: +$275 winner
    "USD_JPY": {"enabled": False, "name": "US Dollar/Japanese Yen", "weight": 0.8, "pip_value": 0.01, "volatility_factor": 0.8},  # DISABLED: -$401 single trade loss
    "AUD_USD": {"enabled": True, "name": "Australian Dollar/US Dollar", "weight": 3.0, "pip_value": 0.0001, "volatility_factor": 1.1},  # HIGHEST WEIGHT: +$936 major winner
    "USD_CAD": {"enabled": True, "name": "US Dollar/Canadian Dollar", "weight": 1.5, "pip_value": 0.0001, "volatility_factor": 0.9},  # REDUCED: -$111 recent loss
    # Best pairs for automated trading based on research
    "AUD_CAD": {"enabled": True, "name": "Australian Dollar/Canadian Dollar", "weight": 1.2, "pip_value": 0.0001, "volatility_factor": 1.0},
    "AUD_NZD": {"enabled": True, "name": "Australian Dollar/New Zealand Dollar", "weight": 1.2, "pip_value": 0.0001, "volatility_factor": 0.7},
    "NZD_CAD": {"enabled": False, "name": "New Zealand Dollar/Canadian Dollar", "weight": 0.8, "pip_value": 0.0001, "volatility_factor": 0.9},  # DISABLED: -$651 major loss contributor
}

# Default instrument
DEFAULT_INSTRUMENT = "EUR_USD"

# Optimized timeframes for short-term trading
TIMEFRAMES = {
    "M1": {"granularity": "M1", "count": 500, "weight": 0.40},    # Primary signal timeframe
    "M5": {"granularity": "M5", "count": 300, "weight": 0.35},    # Signal confirmation
    "M15": {"granularity": "M15", "count": 200, "weight": 0.25}   # Trend context
}

# Risk Management Parameters - Conservative for consistent profitability
MAX_RISK_PER_TRADE = 0.04  # 4% maximum risk per trade (reduced from 5%)
DEFAULT_RISK_PER_TRADE = 0.025  # 2.5% default risk per trade (reduced from 3%)
DEFAULT_LEVERAGE = 50  # Maximum leverage 50:1 (OANDA's full capacity)
DRAWDOWN_THRESHOLD = 0.03  # 3% max daily drawdown before reducing position size
CRITICAL_DRAWDOWN = 0.05  # 5% max daily drawdown before stopping trading
RECOVERY_MODE_THRESHOLD = 0.10  # 10% account drawdown triggers recovery mode

# Global risk limits - Enhanced correlation management
MAX_TOTAL_RISK = 0.03  # 3% maximum total risk across all instruments
MAX_CORRELATED_RISK = 0.02  # 2% maximum risk for correlated instruments
MAX_CORRELATION_COEFFICIENT = 0.40  # Maximum 40% correlation for simultaneous trades

# Correlation groups - Enhanced
CORRELATION_GROUPS = {
    "USD_GROUP": ["EUR_USD", "GBP_USD", "AUD_USD", "USD_CAD", "USD_JPY"],
    "EUR_GROUP": ["EUR_USD", "EUR_JPY", "EUR_GBP", "EUR_AUD"],
    "COMMODITY": ["AUD_USD", "AUD_CAD", "AUD_NZD", "NZD_CAD", "USD_CAD"],
    "SAFE_HAVEN": ["USD_JPY", "USD_CHF"],
}

# Signal Thresholds - REMOVED (using updated thresholds below)

# Indicator Settings - Optimized based on research
INDICATOR_SETTINGS = {
    # EMA Settings - 5-8-13 ribbon for scalping
    "EMA_FAST": 5,      # Optimized from 8
    "EMA_MEDIUM": 8,    # New addition for ribbon
    "EMA_SLOW": 13,     # Optimized from 21
    
    # RSI Settings - Faster response
    "RSI_PERIOD": 7,    # Optimized from 8 for 5-min charts
    "RSI_PERIOD_1MIN": 4,  # Special setting for 1-min charts
    "RSI_OVERBOUGHT": 80,  # Adjusted from 70 for scalping
    "RSI_OVERSOLD": 20,    # Adjusted from 30 for scalping
    
    # MACD Settings - Optimized for scalping
    "MACD_FAST": 6,     # Optimized from 8
    "MACD_SLOW": 13,    # Optimized from 17
    "MACD_SIGNAL": 4,   # Optimized from 5
    
    # Bollinger Bands - Tighter bands for scalping
    "BBANDS_PERIOD": 14, # Optimized from 20
    "BBANDS_STD": 1.5,   # Tighter bands for ranging markets
    "BBANDS_STD_TREND": 2.0,  # Standard for trending markets
    
    # ADX Settings
    "ADX_PERIOD": 14,    # Standard
    "ADX_THRESHOLD": 25, # Clear trend threshold
    
    # ATR Settings
    "ATR_PERIOD": 14,    # Standard
    "ATR_MULTIPLIER_STOP": 1.5,  # For stop loss
    "ATR_MULTIPLIER_TARGET": 3.0,  # Risk:reward 1:2 for profitable trading
    
    # Stochastic Settings - Fast stochastic for scalping
    "STOCH_K_PERIOD": 5, # Reduced from 8
    "STOCH_D_PERIOD": 3,
    "STOCH_OVERBOUGHT": 80,
    "STOCH_OVERSOLD": 20,
    
    # Volume and Additional Indicators
    "VOLUME_MA_PERIOD": 20,
    "CCI_PERIOD": 14,
}

# Market Condition Thresholds - Enhanced regime detection
MARKET_CONDITION = {
    "TRENDING_ADX_THRESHOLD": 25,    # Clear trend
    "RANGING_ADX_THRESHOLD": 20,     # Below this is ranging
    "VOLATILITY_HIGH": 0.15,         # High volatility threshold
    "VOLATILITY_LOW": 0.08,          # Low volatility threshold
    "REGIME_LOOKBACK": 50,           # Bars for regime detection
}

# Position Management - Enhanced
POSITION_MANAGEMENT = {
    "MAX_POSITIONS_PER_INSTRUMENT": 1,  # Reduced from 3 for better control
    "MAX_TOTAL_POSITIONS": 3,            # Maximum concurrent positions
    "MIN_TIME_BETWEEN_TRADES": 300,      # 5 minutes between trades on same pair
    "PARTIAL_CLOSE_TARGET": 0.5,         # Close 50% at first target
    "TRAILING_STOP_ACTIVATION": 1.0,     # Activate trailing stop at 1R profit
    "TRAILING_STOP_DISTANCE": 0.5,       # Trail by 0.5 ATR
}

# Session Trading Settings
TRADING_SESSIONS = {
    "LONDON": {"start": 8, "end": 16, "weight": 1.2},    # 8 AM - 4 PM GMT
    "NEW_YORK": {"start": 13, "end": 21, "weight": 1.2}, # 1 PM - 9 PM GMT
    "TOKYO": {"start": 0, "end": 8, "weight": 0.8},      # 12 AM - 8 AM GMT
    "SYDNEY": {"start": 22, "end": 6, "weight": 0.8},    # 10 PM - 6 AM GMT
}

# Signal Quality Filters
SIGNAL_FILTERS = {
    "MIN_INDICATOR_AGREEMENT": 3,     # Minimum indicators agreeing
    "SPREAD_FILTER_PIPS": 2.0,        # Maximum spread in pips
    "MIN_VOLATILITY": 0.05,           # Minimum volatility for trading
    "MAX_VOLATILITY": 0.25,           # Maximum volatility (avoid news)
    "VOLUME_THRESHOLD": 1.2,          # Volume must be 20% above average
}

# Weekend Trading Settings
WEEKEND_TRADING = {
    "ENABLED": False,
    "REDUCED_RISK": 0.5,
}

# System Settings
UPDATE_INTERVAL = 60  # Update every 60 seconds
MAX_API_RETRIES = 3
LOGGING_LEVEL = "INFO"
BACKTEST_MODE = False

# Enhanced Logging Configuration
LOGGING_CONFIG = {
    "SUMMARY_INTERVAL": 300,  # Summary every 5 minutes
    "PERFORMANCE_INTERVAL": 900,  # Performance update every 15 minutes
    "REDUCE_OANDA_LOGGING": True,  # Suppress verbose OANDA API logs
    "LOG_SIGNAL_DETAILS": False,  # Only log when signal strength > 0
    "LOG_MARKET_DATA_FETCH": False,  # Don't log successful data fetches
    "LOG_DATA_FETCH_SUCCESS": False,  # Don't log successful data fetch operations
    "MIN_SIGNAL_STRENGTH_TO_LOG": 30,  # Only log signals above this strength
}

# Signal Thresholds for Trade Execution - MAXIMUM EXECUTION RATE
SIGNAL_THRESHOLDS = {
    "NEW_LONG": 12,      # ULTRA-LOW: Maximum execution rate for winners only
    "NEW_SHORT": -12,    # ULTRA-LOW: Maximum execution rate for winners only
    "CLOSE_POSITION": 4, # ULTRA-FAST: Immediate exits on any reversal
    "REVERSE_POSITION": 15, # FAST: Quick position reversals
    "MIN_SIGNAL_STRENGTH": 5, # MINIMUM: Process almost all signals
}

# Risk Management Parameters - ASYMMETRIC OPTIMIZATION
MAX_RISK_PER_TRADE = 0.03            # Reduced to 3% maximum risk per trade  
CRITICAL_DRAWDOWN = 0.12             # Stop trading at 12% drawdown
DRAWDOWN_THRESHOLD = 0.08            # Warning at 8% drawdown
RECOVERY_MODE_THRESHOLD = 0.04       # Enter recovery mode at 4% drawdown
MAX_CORRELATED_RISK = 0.09           # Maximum 9% risk in correlated positions
DEFAULT_RISK_PER_TRADE = 0.02        # REDUCED to 2% default risk per trade
DEFAULT_LEVERAGE = 50                # 50:1 maximum leverage for aggressive trading

# Position Management - ULTRA-TIGHT PROTECTION FOR WINNERS ONLY
POSITION_MANAGEMENT = {
    "MAX_POSITIONS_PER_INSTRUMENT": 1,  # One position per instrument
    "MAX_TOTAL_POSITIONS": 3,           # Focus on top 3 winners only
    "MIN_TIME_BETWEEN_TRADES": 60,      # 1 minute for maximum turnover
    "MAX_POSITION_HOLD_TIME": 1800,     # 30 minutes maximum (ultra-fast)
    "PROFIT_TARGET_CLOSE": 0.005,       # REDUCED to 0.5% profit (fast scalping)
    "STOP_LOSS_CLOSE": -0.003,          # ULTRA-TIGHT: -0.3% loss (maximum protection)
}

# Signal Generation and Filtering - MAXIMUM RELAXATION FOR HIGH TRADE FREQUENCY
SIGNAL_FILTERS = {
    "MIN_INDICATOR_AGREEMENT": 1,      # Keep at 1 - minimum requirement
    "VOLUME_THRESHOLD": 1.02,          # Reduced from 1.05 to 1.02 for easier volume requirements
    "MIN_VOLATILITY": 0.00003,         # Reduced from 0.00005 to allow more market conditions
    "MAX_VOLATILITY": 4.0,             # Increased from 3.0 to 4.0 for volatile market trading
    "TREND_STRENGTH_THRESHOLD": 0.2,   # Reduced from 0.3 to 0.2 for weaker trend requirements
    "RSI_OVERBOUGHT": 68,              # Reduced from 70 for more opportunities
    "RSI_OVERSOLD": 32,                # Increased from 30 for more opportunities
    "MACD_SIGNAL_THRESHOLD": 0.00002,  # Reduced from 0.00003 for weaker MACD signals
}

# Performance Optimization Settings (for high-end hardware)
PERFORMANCE_OPTIMIZATION = {
    "PARALLEL_DATA_FETCH": True,           # Enable parallel data fetching
    "MAX_CONCURRENT_REQUESTS": 6,          # Max concurrent API requests (high-end hardware)
    "BATCH_PROCESSING_SIZE": 1000,         # Process signals in batches
    "ENABLE_VECTORIZED_CALC": True,        # Use vectorized calculations where possible
    "MEMORY_CACHE_SIZE": 10000,            # Cache size for historical data (MB)
    "PROGRESS_REPORTING_INTERVAL": 5,      # Progress reports every N%
    "FAST_MODE_SAMPLE_RATE": 1.0,          # Sample rate for testing (1.0 = all data)
}

# Performance Tracking
PERFORMANCE_TARGETS = {
    "DAILY_PROFIT_TARGET": 0.02,      # 2% daily target
    "WEEKLY_PROFIT_TARGET": 0.08,     # 8% weekly target
    "MONTHLY_PROFIT_TARGET": 0.20,    # 20% monthly target
    "MIN_WIN_RATE": 0.60,            # 60% minimum win rate
    "MIN_PROFIT_FACTOR": 1.5,        # Minimum profit factor
}
